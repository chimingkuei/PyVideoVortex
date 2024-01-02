import cv2
import numpy as np
from utils.DataTransformer import DataTransformer, VideoTransformer
from utils.ImageHandler import ImageHandler



class VideoVortex:
    def __init__(self, input_video, output_video, points, adjust_video_size):
        self.input_video = input_video
        self.output_video = output_video
        self.points = points
        self.adjust_video_size = adjust_video_size

    def DetectVideo(self):
        video_capture = cv2.VideoCapture(self.input_video)
        DT = DataTransformer()
        VT = VideoTransformer(video_capture)
        IH = ImageHandler()
        VT.VideoIsOpened()
        ROI_video = VT.WriteVideo(self.output_video, VT.GetVideoInfo()['fps'], VT.GetROIVideoSize(self.points))
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            # Show original video(include ROI range)
            IH.ShowROI(frame, self.adjust_video_size, self.points)

            # Handle image
            resize_frame = cv2.resize(frame, self.adjust_video_size, interpolation=cv2.INTER_AREA)
            ROI = IH.GetROI(resize_frame , self.points, DT.GetExtremum(self.points), "Color")
            DT.IndicatorLight(ROI, (350, 50), "Green")
            gray_ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
            binary = IH.Binarization(gray_ROI, 170) #2.mp4 128 #1.mp4 170 
            cnts, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            for i in range(0,len(cnts)):  
                x, y, w, h = cv2.boundingRect(cnts[i]) 
                #if y>250 and x<100 and w>5 and h>5: #2.mp4
                #   cv2.rectangle(draw, (x-20,y-20), (x+w,y+h), (0,0,255), 3)
                #   DT.IndicatorLight(draw, (50, 50), "Red")
                if y>200 and w>10 and w>10: #1.mp4
                   cv2.rectangle(ROI, (x-50,y-5), (x+w+5,y+h+50), (0,0,255), 1)
                   DT.IndicatorLight(ROI, (350, 50), "Red")
            cv2.imshow("Detect", ROI)
            ROI_video.write(ROI)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        video_capture.release()
        ROI_video.release()
        cv2.destroyAllWindows()

    
if __name__ == '__main__':
    input_video = r"E:\DIP Temp\Image Temp\1_target.mp4"
    output_video = r"E:\DIP Temp\Image Temp\output_video.mp4"
    points = [(1063, 390), (1398, 641), (1505, 536), (1167, 331)] #1.mp4
    adjust_video_size = (1920, 1080)
    #points = [(416, 426), (529, 539), (913, 311), (791, 224)] #2.mp4
    Object = VideoVortex(input_video, output_video, points, adjust_video_size)
    Object.DetectVideo()
    #test

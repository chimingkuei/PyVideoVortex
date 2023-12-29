# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 00:23:11 2019

@author: User
"""

import cv2
import numpy as np
from utils import DataTransformer, ImageHandler


class VideoVortex:
    def __init__(self, input_video, output_video, points, video_storage_width, video_storage_height):
        self.input_video = input_video
        self.output_video = output_video
        self.points = points
        self.video_storage_width = video_storage_width
        self.video_storage_height = video_storage_height



    def DetectVideo(self):
        video_capture = cv2.VideoCapture(self.input_video)
        DT = DataTransformer.DataTransformer()
        IH = ImageHandler.ImageHandler()
        DT.VideoIsOpened(video_capture)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_video = cv2.VideoWriter(self.output_video, fourcc, DT.GetVideoInfo(video_capture)['fps'], (self.video_storage_width, self.video_storage_height))
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            original_image = cv2.resize(frame , (self.video_storage_width, self.video_storage_height), interpolation=cv2.INTER_AREA)
            show_image = IH.ShowROI(original_image, np.array(self.points))
            cv2.circle(show_image, (150, 50), 30, (0, 255, 0), -1)

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(gray_frame , (self.video_storage_width, self.video_storage_height), interpolation=cv2.INTER_AREA)
            ROI = IH.GetROI(image, np.array(self.points), DT.GetExtremum(np.array(self.points)), "Mono")
            draw = IH.GetROI(original_image, np.array(self.points), DT.GetExtremum(np.array(self.points)), "Color")
            binary = IH.Binarization(ROI, 128) #2.mp4 150 #1.mp4 170 
            cnts, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            for i in range(0,len(cnts)):  
                x, y, w, h = cv2.boundingRect(cnts[i]) 
                if y>250 and x<100 and w>5 and h>5: #2.mp4
                   cv2.rectangle(draw, (x-20,y-20), (x+w,y+h), (0,0,255), 1)
                   cv2.circle(show_image, (150, 50), 30, (0, 0, 255), -1)
                # if y>200 and w>10 and w>10: #1.mp4
                #     cv2.rectangle(draw, (x-50,y-5), (x+w+5,y+h+50), (0,0,255), 1)
            cv2.imshow('Original Video(Include ROI Range)', show_image)
            cv2.imshow("DIP", binary)
            cv2.imshow("Detect", draw)
            output_video.write(draw)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        video_capture.release()
        output_video.release()
        cv2.destroyAllWindows()

    
if __name__ == '__main__':
    input_video = r"E:\DIP Temp\Image Temp\2_target.mp4"
    output_video = r"E:\DIP Temp\Image Temp\output_video.mp4"
    # points = [(1063, 390), (1398, 641), (1505, 536), (1167, 331),] #1.mp4
    points = [(416, 426), (529, 539), (913, 311), (791, 224)] #2.mp4
    Object = VideoVortex(input_video, output_video, points, 1920, 1080)
    Object.DetectVideo()


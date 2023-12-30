import cv2
import numpy as np


class DataTransformer:
    def GetExtremum(self, points):
        x_values = np.array(points)[:, 0]
        y_values = np.array(points)[:, 1]
        dict = {
        'x_max': np.max(x_values), 
        'x_min': np.min(x_values),
        'y_max': np.max(y_values),  
        'y_min': np.min(y_values),
        }
        return dict
    
    def IndicatorLight(self, image, position, type):
        if type =="Red":
            cv2.circle(image, (position[0], position[1]), 30, (0, 0, 255), -1)
            cv2.circle(image, (position[0], position[1]), 33, (128, 128, 128), 5)
        elif type =="Green":
            cv2.circle(image, (position[0], position[1]), 30, (0, 255, 0), -1)
            cv2.circle(image, (position[0], position[1]), 33, (128, 128, 128), 5)

class VideoTransformer:
    def __init__(self, video):
        self.video = video

    def VideoIsOpened(self):
        if not self.video.isOpened():
            print("Error: Unable to open video file.")
            exit()

    def GetVideoInfo(self):
        dict = {
        'fps': int(self.video.get(cv2.CAP_PROP_FPS)), 
        'width': int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'height': int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        }
        return dict
    
    def GetROIVideoSize(self, points):
         DT = DataTransformer()
         dict = DT.GetExtremum(points)
         width = dict['x_max'] - dict['x_min']
         height = dict['y_max'] - dict['y_min']
         return (width, height)
    
    def WriteVideo(self, output_video, fps, size):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        return cv2.VideoWriter(output_video, fourcc, fps, size)
import cv2
import numpy as np


class DataTransformer:
    def GetExtremum(self, points):
        x_values = points[:, 0]
        y_values = points[:, 1]
        dict = {
        'x_max': np.max(x_values), 
        'x_min': np.min(x_values),
        'y_max': np.max(y_values),  
        'y_min': np.min(y_values),
        }
        return dict
    
    def VideoIsOpened(self,video):
        if not video.isOpened():
            print("Error: Unable to open video file.")
            exit()

    def GetVideoInfo(self, video):
        fps = int(video.get(cv2.CAP_PROP_FPS))
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        dict = {
        'fps': int(video.get(cv2.CAP_PROP_FPS)), 
        'width': int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'height': int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        }
        return dict
    
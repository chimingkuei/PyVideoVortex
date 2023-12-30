import cv2
import numpy as np


class ImageHandler:
    def ShowROI(self, image, size, points):
        resize_image = cv2.resize(image , size, interpolation=cv2.INTER_AREA)
        mask = np.zeros(resize_image.shape, np.uint8)
        mask = cv2.fillPoly(mask, [np.array(points)], (0, 255, 0))
        show_image = cv2.addWeighted(src1=resize_image, alpha=0.8, src2=mask, beta=0.2, gamma=0)
        cv2.namedWindow('Original Video(Include ROI Range)', cv2.WND_PROP_FULLSCREEN)
        cv2.imshow('Original Video(Include ROI Range)', show_image)
        return show_image

    def GetROI(self, image, points, dict, image_type):
        mask = np.zeros(image.shape, np.uint8)
        if image_type == "Mono":
            red_color = 255
        elif image_type == "Color":
            red_color = (255, 255, 255)
        cv2.fillPoly(mask, [np.array(points)], red_color)
        ROI = cv2.bitwise_and(mask, image)
        crop_ROI = ROI[dict['y_min']:dict['y_max'], dict['x_min']:dict['x_max']]
        return crop_ROI
    
    def Binarization(self, image, threshold):
        ret, dst = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        return dst
    
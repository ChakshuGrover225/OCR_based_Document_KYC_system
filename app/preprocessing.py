''' 
def image_preprocessing(raw_img_path, dir_id):
    realigned_img_path = realign_img(raw_img_path, dir_id)
    cropped_img_path = cropped_img(realigned_img_path, dir_id)
    grey_img_path = img_to_grey(cropped_img_path, dir_id)
    return grey_img_path
'''

import cv2
import numpy as np
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True



def preprocess_image(image_path):
    temp_image_path = realign_img(image_path)
    temp_image_path = cropped_img(temp_image_path)
    temp_image_path = img_to_grey(temp_image_path)
    return temp_image_path
    pass


def realign_img(input_img_path):

    print('realign_img')
    image = cv2.imread(input_img_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help with edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detector to find edges in the image
    edges = cv2.Canny(blurred, 50, 150)

    # Use HoughLinesP to detect lines in the image
    # Use HoughLinesP to detect lines in the image
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    # Find the angle of the longest line detected
    angles = [np.arctan2(y2 - y1, x2 - x1) for line in lines for x1, y1, x2, y2 in line]
    angle = np.degrees(np.median(angles))

    # Rotate the image to correct the skew
    rotated = cv2.warpAffine(image, cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), angle, 1), (image.shape[1], image.shape[0]), flags=cv2.INTER_NEAREST)

    cv2.imwrite(input_img_path, rotated)
    return input_img_path



def cropped_img(input_img_path):
    print('cropped_img')
    return input_img_path

def img_to_grey(input_image_path):
    return "image preprocessed"




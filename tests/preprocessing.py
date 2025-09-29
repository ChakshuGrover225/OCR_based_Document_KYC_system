''' 
take images as input
greyscale it
constrast it
straigten it 

'''
from PIL import Image
from PIL import ImageFile
import cv2
import numpy as np  
ImageFile.LOAD_TRUNCATED_IMAGES = True



def realign_img(input_img_path):
    print('realign image')
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


def cropped_img(image):
    pass


def img_to_grey(image):
    pass








def preprocess_image(image_path):
    
    temp_image_path = realign_img(image_path)
    print("after realign", temp_image_path)
    return temp_image_path
    
preprocess_image(r'uploaded_images\image-test_unaligned.png')

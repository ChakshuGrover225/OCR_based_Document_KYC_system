''' 
take images as input
greyscale it
constrast it
straigten it 

'''
import os
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

    input_img_path = input_img_path[:-4]+"_realigned.jpg"
    cv2.imwrite(input_img_path, rotated)
    return input_img_path


def img_to_grey(input_image_path):
    print('img_to_grey')
    img = Image.open(input_image_path).convert('L')
    input_image_path = input_image_path[:-4]+"_grey.jpg"
    img.save(input_image_path)
    return input_image_path
    pass


def contrast_change(input_image_path, threshold):
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    _, mono = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imwrite(input_image_path[:-4]+"_monochrome.jpg", mono)
    return input_image_path[:-4]+"_monochrome.jpg"


def processed_image(input_image_path):

    img = Image.open(input_image_path)
    img.save("uploaded_images/processed_image.jpg")

    directory = r"uploaded_images"  # your folder path
    keep_files = ["processed_image.jpg", "11.jpg"]  # files to keep
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename not in keep_files:
            os.remove(file_path)
            print(f"Deleted: {filename}")






def preprocess_image(image_path):
    
    aligned_image_path = realign_img(image_path)
    print("after realign", aligned_image_path)
    grey_image_path = img_to_grey(aligned_image_path)
    print("after img to grey")
    #contrasted_image_path = contrast_change(grey_image_path, 150)
    processed_image(grey_image_path)
    print("after image preprocessed")





    
preprocess_image(r'uploaded_images\11.jpg')

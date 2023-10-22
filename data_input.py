import cv2
import numpy as np
import sqlite3 as sql
import os
import math

# Load the image
image = cv2.imread('./Clean_Data/Worlds_Edge/WE_Game30_Ring5.jpg')

# Assuming it's a rectangle, calculate width and height percentages
width_percentage = 0.52  # 52% of the original width
height_percentage = 0.94  # 94% of the original height

# Calculate the pixel values for cropping
width = image.shape[1]
height = image.shape[0]

left_crop = int((1 - width_percentage) * width / 2)
right_crop = int(width - left_crop)
bottom_crop = int((1 - height_percentage) * height)

# Crop the image
cropped_image = image[0:height - bottom_crop, left_crop:right_crop]

# Define the color for the filled circle
target_color = (251, 255, 140)  # BGR format

# Create a mask to find pixels within the color range of the filled circle
mask = cv2.inRange(cropped_image, target_color, target_color)

# Find the center of the filled circle
moments = cv2.moments(mask, binaryImage=True)
center_x = math.floor(int(moments["m10"] / moments["m00"]))
center_y = math.floor(int(moments["m01"] / moments["m00"]))

# Draw a red dot at the center
cv2.circle(cropped_image, (center_x, center_y), 5, (0, 0, 255), -1)  # Use (0, 0, 255) for red color

# Save or display the image with the filled circle's center marked
cv2.imwrite('image_with_filled_circle_center.jpg', cropped_image)
center_x = math.floor((int(moments["m10"] / moments["m00"])/1332)*100)
center_y = math.floor((int(moments["m01"] / moments["m00"])/1354)*100)
print(f"Center of the filled circle (x, y): ({center_x}, {center_y})")
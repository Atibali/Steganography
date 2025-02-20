import cv2
import numpy as np
import os

# Read the image
img = cv2.imread("mypic.jpg")  # Ensure correct path

if img is None:
    print("Error: Unable to read the image. Check the file path.")
    exit()

height, width, _ = img.shape

msg = input("Enter secret message: ") + "~"  # '~' as termination marker
password = input("Enter a passcode: ")

key = sum(ord(char) for char in password) % 256

flat_img = img.flatten()

for i in range(len(msg)):
    if i >= len(flat_img):
        print("Error: Message too long for this image!")
        exit()
    
    flat_img[i] = (ord(msg[i]) ^ key) 

img = flat_img.reshape(height, width, 3)

cv2.imwrite("encryptedImage.png", img)

print("Encryption complete! Image saved as 'encryptedImage.png'.")
import cv2
import numpy as np

img = cv2.imread("encryptedImage.png")

if img is None:
    print("Error: Unable to read the encrypted image.")
    exit()

height, width, _ = img.shape

password = input("Enter passcode for Decryption: ")

key = sum(ord(char) for char in password) % 256

flat_img = img.flatten()

# Decode message
message = ""
for i in range(len(flat_img)):
    char = chr(flat_img[i] ^ key)
    if char == "~":  
        break
    message += char

# Output the decrypted message
if message:
    print("Decryption successful! Message:", message)
else:
    print("Failed to decrypt. Check the passcode or image.")

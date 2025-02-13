import cv2
from pyzbar.pyzbar import decode

# Load the image using OpenCV
image = cv2.imread('/scan.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Decode the QR code
qr_codes = decode(gray_image)

data = qr_codes.data.decode('utf-8')
print(data)

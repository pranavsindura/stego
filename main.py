import stego
import cv2
from PIL import Image
# images are stored in src/
# Retrieve host image host_img
# Retrieve secret image secret_img
host_img = cv2.imread('src/lena.png')
secret_img = cv2.imread('src/baboon.png')

# Encrypt
stego_img, key = stego.encrypt(host_img, secret_img)
im = Image.fromarray(stego_img)
im.show()
im.save("result.png")
# Save the stego_img and key

# Decrypt
# host_img, secret_img = stego.decrypt(stego_img, key)

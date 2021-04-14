import stego
import cv2
import numpy as np
from PIL import Image
# images are stored in src/
# Retrieve host image host_img
# Retrieve secret image secret_img

host_img = np.array(Image.open('src/lena.png'))
secret_img = np.array(Image.open('src/baboon.png'))

# Encrypt
stego_img, key = stego.encrypt(host_img, secret_img)
im = Image.fromarray(host_img)
im.show()
im.save("result.jpg")
# Save the stego_img and key

# Decrypt
# host_img, secret_img = stego.decrypt(stego_img, key)

import stego
import cv2
import numpy as np
from PIL import Image

# images are stored in src/
# Retrieve host image host_img
# Retrieve secret image secret_img

host_img = Image.open('src/lena512.bmp')
host_img = host_img.resize((512, 512))
secret_img = Image.open('src/general_test_pattern.png')
secret_img = secret_img.resize((256, 256))

host_img = np.array(host_img)
secret_img = np.array(secret_img)

print('Host',host_img.shape)
print('Secret',secret_img.shape)
# Encrypt
stego_img, key = stego.encrypt(host_img, secret_img)
im = Image.fromarray(stego_img)
im.show()
im.save("result.png")
# Save the stego_img and key

# Decrypt
# host_img, secret_img = stego.decrypt(stego_img, key)

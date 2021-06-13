import stego
import cv2
import numpy as np
from PIL import Image

# images are stored in src/
# Retrieve host image host_img
# Retrieve secret image secret_img

host_img = np.array(Image.open('src/lenna-256.png'))[:, :, 0]
secret_img = np.array(Image.open('src/baboon-64.png'))[:, :, 0]
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

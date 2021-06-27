from embedder import embed
from psnr import psnr
import stego
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# images are stored in src/
# Retrieve host image host_img
# Retrieve secret image 

host_img = np.array(Image.open('src/lena512.bmp').convert('L').resize((512, 512)))
secret_img = np.array(Image.open('src/general_test_pattern.png').convert('L').resize((256, 256)))

print('Host', host_img.shape)
print('Secret', secret_img.shape)

# Encrypt
chromosome = 23163660186
stego_img = embed(host_img, secret_img, chromosome)
im = Image.fromarray(stego_img)
print(psnr(stego_img, host_img))
imshow(host_img, stego_img, secret_img)
im.save("result.png")
# Save the stego_img and key

# Decrypt
# host_img, secret_img = stego.decrypt(stego_img, key)

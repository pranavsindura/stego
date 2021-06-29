import stego
import numpy as np
from PIL import Image
from psnr import psnr
from matplotlib import pyplot as plt

# images are stored in src/
# Retrieve host image host_img
# Retrieve secret image secret_img

def imshow(host, stego, secret):
    """Show the images with matplotlib"""
    fig, axes = plt.subplots(1,3)

    axes[0].set_title('Host')
    axes[1].set_title('Stego')
    axes[2].set_title('Secret')

    axes[0].imshow(host, cmap='gray', aspect='equal')
    axes[1].imshow(stego, cmap='gray', aspect='equal')
    axes[2].imshow(secret, cmap='gray', aspect='equal')

    plt.setp(axes, xticklabels=[], yticklabels=[], xticks=[], yticks=[])

    plt.show()


host_img = np.array(Image.open('src/lena512.bmp').convert('L').resize((512, 512)))
secret_img = np.array(Image.open('src/general_test_pattern.png').convert('L').resize((256, 256)))

print('Host', host_img.shape)
print('Secret', secret_img.shape)

# Encrypt
stego_img, key = stego.encrypt(host_img, secret_img)
im = Image.fromarray(stego_img)

print('Key:', key)
print('PSNR:', psnr(stego_img, host_img))
imshow(host_img, stego_img, secret_img)

im.save("result.png")
# Save the stego_img and key

# Decrypt
# host_img, secret_img = stego.decrypt(stego_img, key)

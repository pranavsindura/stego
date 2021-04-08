import stego
# images are stored in src/
# Retrieve host image host_img
# Retrieve secret image secret_img

# Encrypt
stego_img, key = stego.encrypt(host_img, secret_img)
# Save the stego_img and key

# Decrypt
host_img, secret_img = stego.decrypt(stego_img, key)

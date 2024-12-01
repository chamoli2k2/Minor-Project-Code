import numpy as np
import cv2
import os

def encrypt_image_with_key(image, key):
    """
    Encrypt the image using XOR operation with the provided key.
    """
    return np.bitwise_xor(image, key)

def moth_flame_optimization_encryption(image, key):
    """
    Encrypt the image using Moth Flame Optimization logic with the provided key.
    """
    return encrypt_image_with_key(image, key)

if __name__ == "__main__":
    image = cv2.imread("/home/chamoli/Desktop/minor project/CODE/dataset/lena.png", cv2.IMREAD_GRAYSCALE)
    os.makedirs("mfoImages", exist_ok=True)

    # Define your binary key as a string
    key_str = "1000110001100101111010011001110111001110"
    
    # Convert the binary string to an array of uint8
    key = np.array([int(bit) for bit in key_str], dtype=np.uint8) * 255  # Scale to 0-255

    # Repeat or tile the key to match the image size
    key = np.tile(key, (image.size // len(key) + 1))[:image.size].reshape(image.shape)

    # Encrypt the image
    encrypted_image = moth_flame_optimization_encryption(image, key)
    cv2.imwrite("mfoImages/encrypted_lena.png", encrypted_image)

    print("MFO Encryption completed! Image saved in mfoImages folder.")

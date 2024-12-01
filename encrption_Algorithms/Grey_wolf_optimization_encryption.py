import numpy as np
import cv2
import os

def encrypt_image_with_key(image, key):
    """
    Encrypt the image using XOR operation with the provided key.
    """
    return np.bitwise_xor(image, key)

def grey_wolf_optimization_encryption(image, key):
    """
    Encrypt the image using Grey Wolf Optimization logic with the provided key.
    """
    return encrypt_image_with_key(image, key)

if __name__ == "__main__":
    image = cv2.imread("/home/chamoli/Desktop/minor project/CODE/dataset/lena.png", cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        raise FileNotFoundError("Image not found. Check the file path.")

    os.makedirs("gwoImages", exist_ok=True)

    # Define your binary key as a string (40 bits)
    key_str = "1000110001100101111010011001110111001110"  # Example binary key

    # Convert the binary string to an array of uint8
    key = np.array([int(bit) for bit in key_str], dtype=np.uint8) * 255  # Scale to 0-255

    # Ensure key is expanded to match image size
    key = np.tile(key, (image.size // len(key) + 1))[:image.size].reshape(image.shape)

    # Encrypt the image
    encrypted_image = grey_wolf_optimization_encryption(image, key)
    cv2.imwrite("gwoImages/encrypted_lena.png", encrypted_image)

    print("GWO Encryption completed! Image saved in gwoImages folder.")

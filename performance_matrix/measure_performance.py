import numpy as np
import cv2

def calculate_npcr(original, encrypted):
    """
    Calculate Number of Pixels Change Rate (NPCR).
    """
    diff = original != encrypted
    npcr = np.sum(diff) / diff.size * 100
    return npcr

def calculate_uaci(original, encrypted):
    """
    Calculate Unified Average Changing Intensity (UACI).
    """
    intensity_diff = np.abs(original.astype(np.float64) - encrypted.astype(np.float64))
    uaci = np.mean(intensity_diff / 255) * 100
    return uaci

def calculate_entropy(image):
    """
    Calculate Information Entropy (IE).
    """
    pixel_counts = np.bincount(image.flatten(), minlength=256)
    probabilities = pixel_counts / np.sum(pixel_counts)
    return -np.sum(probabilities * np.log2(probabilities + 1e-10))  # Add small value to avoid log(0)

if __name__ == "__main__":
    original_image = cv2.imread("/home/chamoli/Desktop/minor project/CODE/dataset/lena.png", cv2.IMREAD_GRAYSCALE)
    encrypted_image = cv2.imread("/home/chamoli/Desktop/minor project/CODE/gaImages/encrypted_lena.png", cv2.IMREAD_GRAYSCALE)

    # Calculate NPCR
    npcr = calculate_npcr(original_image, encrypted_image)
    print(f"NPCR: {npcr:.2f}%")

    # Calculate UACI
    uaci = calculate_uaci(original_image, encrypted_image)
    print(f"UACI: {uaci:.2f}%")

    # Calculate Entropy
    entropy_value = calculate_entropy(encrypted_image)
    print(f"Entropy: {entropy_value:.2f}")

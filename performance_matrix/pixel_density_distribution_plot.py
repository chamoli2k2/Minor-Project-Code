import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

def plot_histograms(original, encrypted):
    """
    Plot histograms for the original and encrypted images.
    :param original: Original image (numpy array).
    :param encrypted: Encrypted image (numpy array).
    """
    # Create a histogram for the original image
    hist_original, bins_original = np.histogram(original.flatten(), bins=256, range=[0, 256])
    # Create a histogram for the encrypted image
    hist_encrypted, bins_encrypted = np.histogram(encrypted.flatten(), bins=256, range=[0, 256])

    # Plot the histograms
    plt.figure(figsize=(12, 6))
    plt.title("Pixel Distribution: Original vs Encrypted")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    
    # Plot original histogram
    plt.plot(bins_original[0:-1], hist_original, color='blue', label='Original', alpha=0.6)
    # Plot encrypted histogram
    plt.plot(bins_encrypted[0:-1], hist_encrypted, color='red', label='Encrypted', alpha=0.6)
    
    plt.legend()
    plt.grid()
    
    # Save the plot
    os.makedirs("histogramPlots", exist_ok=True)
    plt.savefig("histogramPlots/pixel_distribution_comparison.png")
    plt.close()

if __name__ == "__main__":
    # Load the original and encrypted images
    original_image = cv2.imread("/home/chamoli/Desktop/minor project/CODE/dataset/lena.png", cv2.IMREAD_GRAYSCALE)
    encrypted_image = cv2.imread("/home/chamoli/Desktop/minor project/CODE/gaImages/encrypted_lena.png", cv2.IMREAD_GRAYSCALE)

    if original_image is None or encrypted_image is None:
        raise FileNotFoundError("One or both images not found. Check the file paths.")

    # Plot and save histograms
    plot_histograms(original_image, encrypted_image)

    print("Histogram comparison saved in 'histogramPlots' folder.")

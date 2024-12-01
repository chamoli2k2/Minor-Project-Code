# Repeat or tile the key to match the image size
    key = np.tile(key, (image.size // len(key) + 1))[:image.size].reshape(image.shape)
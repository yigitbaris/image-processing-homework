import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_gaussian_smoothing(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Apply Gaussian smoothing
    smoothed_img = cv2.GaussianBlur(img, (5, 5), 0)

    # Display the original and smoothed images
    plt.imshow(img)
    plt.title('Original Image')
    plt.show()

    plt.imshow(smoothed_img)
    plt.title('Image after Gaussian Smoothing')
    plt.show()

def apply_image_sharpening(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Create a sharpening kernel
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    # Apply image sharpening using the kernel
    sharpened_img = cv2.filter2D(img, -1, kernel)

    # Display the original and sharpened images
    plt.imshow(img)
    plt.title('Original Image')
    plt.show()

    plt.imshow(sharpened_img)
    plt.title('Image after Sharpening')
    plt.show()

if __name__ == '__main__':
    image_path = "path/to/your/image.jpg"  # Replace with the actual path to your image

    # Gaussian Smoothing
    apply_gaussian_smoothing(image_path)

    # Image Sharpening
    apply_image_sharpening(image_path)
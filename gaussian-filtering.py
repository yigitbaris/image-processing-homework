import cv2
import matplotlib.pyplot as plt
image_path = "imagepath/image.jpg"
def apply_gaussian_filter(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Apply Gaussian filtering
    gaussian_img = cv2.GaussianBlur(img, (5, 5), 0)

    # Display the original and filtered images
    plt.imshow(img)
    plt.title('Original Image')
    plt.show()

    plt.imshow(gaussian_img)
    plt.title('Image after Gaussian Filtering')
    plt.show()

if __name__ == '__main__':
    image_path = "imagepath/image.jpg"  # Replace with the actual path to your image
    apply_gaussian_filter(image_path)
import cv2
import matplotlib.pyplot as plt
import numpy as np
image_path = "imagepath/image.jpg"
def sobel_filter():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not read the image from the path: {image_path}")
    else:
        filtered_img = np.zeros_like(img)
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        for j in range(img.shape[0] - 2):
            for i in range(img.shape[1] - 2):
                pixval_x = np.sum(sobel_x * img[j:j + 3, i:i + 3])
                pixval_y = np.sum(sobel_y * filtered_img[j:j + 3, i:i + 3])
                sum_val = abs(pixval_x) + abs(pixval_y)
                sum_val = min(sum_val, 255)
                filtered_img[j, i] = sum_val
        plt.subplot(1, 2, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Orijinal görüntü')
        plt.subplot(1, 2, 2)
        plt.imshow(filtered_img, cmap='gray')
        plt.title('Sobel filtered')
        plt.show()
if __name__ == "__main__":
    print("Starting Sobel Filter")
    sobel_filter()
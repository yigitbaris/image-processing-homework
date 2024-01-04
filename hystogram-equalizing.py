import cv2
import matplotlib.pyplot as plt

image_path = "imagepath/image.jpg"

def histogram_equalization_gray():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    equalized_img = cv2.equalizeHist(img)
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(equalized_img, cmap='gray')
    plt.title('Equalized Image')
    plt.show()

def histogram_equalization_colorful():
    img = cv2.imread(image_path)
    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab_img)
    equ = cv2.equalizeHist(l)
    updated_lab_img = cv2.merge((equ, a, b))
    hist_eq_img = cv2.cvtColor(updated_lab_img, cv2.COLOR_LAB2BGR)
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(hist_eq_img, cv2.COLOR_BGR2RGB))
    plt.title('Histogram Equalized Image')
    plt.show()

if __name__ == '__main__':
    histogram_equalization_gray()
    histogram_equalization_colorful()

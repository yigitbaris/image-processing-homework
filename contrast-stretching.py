import cv2
import matplotlib.pyplot as plt
import numpy as np
image_path = "imagepath/image.jpg"
def contrast_stretching():
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    norm_img1 = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    norm_img2 = cv2.normalize(img, None, alpha=0, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    norm_img1 = (255 * norm_img1).astype(np.uint8)
    norm_img2 = np.clip(norm_img2, 0, 1)
    norm_img2 = (255 * norm_img2).astype(np.uint8)
    plt.imshow(img)
    plt.title('Orjinal Görüntü')
    plt.show()
    plt.imshow(norm_img1)
    plt.title('Kontrast Gerilmiş Görüntü 1')
    plt.show()
    plt.imshow(norm_img2)
    plt.title('Kontrast Gerilmiş Görüntü 2')
    plt.show()
if __name__ == '__main__':
    contrast_stretching()
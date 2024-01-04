import cv2
import matplotlib.pyplot as plt
import numpy as np
image_path = "imagepath/image.jpg"
def gamma_correction(gamma):
    img = cv2.imread(image_path)
    invGamma = 1 / gamma
    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    gammaImg = cv2.LUT(img, table)
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Orijinal görüntü')
    plt.subplot(1,2, 2)
    plt.imshow(gammaImg)
    plt.title('Gamma değiştirilmiş görüntü')
    plt.show()
if __name__ == '__main__':
    gamma_correction(2.2)
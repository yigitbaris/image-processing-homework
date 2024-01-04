import cv2
import matplotlib.pyplot as plt
image_path = "imagepath/image.jpg"
def laplacian_blur_detection(img):
    grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    isBlured = cv2.Laplacian(grey_image,cv2.CV_64F).var()
    if isBlured < 120:
        print(f"Image is blurred : {isBlured}")
    else:
        print(f"Image is not blurred : {isBlured}")
def color_average_blur(kernel_size):
    img = cv2.imread(image_path)
    blurred_blue = cv2.blur(img[:, :, 0], (kernel_size, kernel_size))
    blurred_green = cv2.blur(img[:, :, 1], (kernel_size, kernel_size))
    blurred_red = cv2.blur(img[:, :, 2], (kernel_size, kernel_size))
    blurred_img = cv2.merge([blurred_blue, blurred_green, blurred_red])
    plt.figure(figsize=(24 ,12))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
    plt.title(f'Average Blurred Image (Kernel Size = {kernel_size})')
    plt.show()
    return blurred_img
if __name__ == "__main__":
    kernel_size = 3
    test_img = color_average_blur(kernel_size)
    laplacian_blur_detection(test_img)
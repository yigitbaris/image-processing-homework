import cv2
import matplotlib.pyplot as plt
image_path = "imagepath/image.jpg"

def bit_plane_slice(bit):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    bit_plane = (img >> bit) & 1
    plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Source Image')
    plt.subplot(1, 2, 2)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit-Plane {bit}')
    plt.show()
if __name__ == '__main__':
    print("Bit-Plane Image: Choose the bit-plane (0 to 8) you want to visualize (To see al bit-planes, type:9)")
    bit_slice_number =input(">> ")
    if not bit_slice_number.isdigit():
        print("invalid input \nvisualize all bit-slice positions as default")
        bit_slice_number = 9
    bit_slice_number = int(bit_slice_number) % 9
    if bit_slice_number == 9:
        for i in range(9):
            bit_plane_slice(i)
            print("bit-plane position: ", i)
    else:
        bit_plane_slice(bit_slice_number)
        print("bit-plane position: ", bit_slice_number)
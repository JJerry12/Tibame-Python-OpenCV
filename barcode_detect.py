"""
Name: Jerry
-----------------
This program can read QR codes within an image.
"""

import cv2
from pyzbar import pyzbar


def main():
    img = cv2.imread('barcode_demo.png', 1)
    r = pyzbar.decode(img)

    for i, d in enumerate(r):
        print("第" + str(i+1) + "個條碼, 類型: " + d.type + ", 內容: " + d.data.decode("UTF-8"))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

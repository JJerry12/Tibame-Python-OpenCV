"""
Name: Jerry
-----------------
This program applies the camera to implement a QR code scanner.
"""

import cv2
from pyzbar import pyzbar


p = cv2.VideoCapture(0)                         # 讀取當前電腦的攝影機
w, h = (200, 200)                               # 讀取方框大小

while True:                                     # 持續產生無數照片，造成動態的畫面
    ret, m1 = p.read()
    if ret:                                     # 只有變數一為True(有讀到畫面)，變數二才有內容
        x, y = (int((m1.shape[1]-w)*0.5), int((m1.shape[0]-h)*0.5))
        cv2.rectangle(m1, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow("Image 1", m1)
        r = pyzbar.decode(m1[y:y+h, x:x+w])     # 只讀取進到方框中的QRcode
        if len(r) == 1:
            print("類型：", r[0].type, "，內容：", end="")

            # 日本人寫的library的中文字bug，先將編碼轉成日文編碼，再轉換回UTF-8
            try:
                print(r[0].data.decode("UTF-8").encode("sjis").decode("UTF-8"))
            except:
                print(r[0].data.decode("UTF-8"))
        elif len(r) >= 2:
            print("存在多個QR Code")

    cv2.waitKey(50)
cv2.destroyAllWindows()
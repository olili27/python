from PIL import Image
import cv2
import numpy as np
import pprint

grayscalePath = "/tmp/grayscale-image.png"
grayscalePath2 = "/tmp/grayscale-image2.png"

img = cv2.imread("/tmp/tom-back.jpeg")
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h,w, channels = img.shape

croppedImage = img[:900, 220:600]

# cv2.imwrite(grayscalePath, croppedImage)

flag = False

chunkwidth = 2
stop = 0
for start in range(0, 5, chunkwidth):
    end = start + chunkwidth
    stop += chunkwidth
    chunk = grayImage[:, start:end]

    pprint.pprint(chunk)

    # chunk.da
    # if stop == 220:
    #     pprint.pprint(chunk)
    #     for e in chunk:
    #         val1, val2 = e
    #         statement = f"val1:{val1} val2:{val2}"
    #         print(statement)
    #     break

    # print(chunk)
    # for e in chunk:
    #     val1, val2 = e
    #     if val1 < 80 and val2 < 80:
    #         print(val1, val2)
    #         print(stop)
    #         croppedImage = img[:, stop:]
    #         cv2.imwrite(grayscalePath, croppedImage)
    #         flag =True
    #         break
    
    # if flag: break

        

    
        

# print("width:", w, "height:",h)
# C:/Users/ivanm/Downloads/res (2)/res/shapes2.png

import cv2
import numpy as np

switch = False # x

font = cv2.FONT_HERSHEY_DUPLEX

image = cv2.imread('./7Ptkifa.png') # https://imgur.com/a/g1tT1Kb - Ссылка на фото

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

mask = np.zeros((image.shape[0] + 2, image.shape[1] + 2), dtype=np.uint8)
cv2.floodFill(thresh, mask, (0, 0), 255)
thresh = cv2.bitwise_not(thresh)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    epsilon = 0.04*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    lined = approx.ravel ()
    print(approx)
    M = cv2.moments(c)
    
    if M['m00'] != 0:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])
        center = (cX, cY)
        
    # print("///")
    # for i in approx:
    #     # print(f"i = {i}")
    #     noSpace = ' '.join(str(x) for x in i).strip("[]")
    #     splitNums = noSpace.split()
    #     xS.append(int(splitNums[0]))
    #     yS.append(int(splitNums[1]))
    cv2.drawContours(image, [c], -1, (0,255,255), 3)
    cv2.drawContours(image, [approx], -1, (0,0,255), 3)
    if len(approx) == 3:
        cv2.putText(image, "Triangle", center, font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(image, "Rectangle", center, font, 1, (0))
    elif len(approx) == 5:
        cv2.putText(image, "Pentagon", center, font, 1, (0))
    else:
        cv2.putText(image, "Round figure", center, font, 1, (0))
    
cv2.imshow('out', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

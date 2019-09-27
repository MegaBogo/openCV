import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/2.jpg', cv2.IMREAD_GRAYSCALE)

ret, origin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thr1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# cv2.imshow('global threshold', origin)
cv2.imshow('GAUSSIAN_C', thr1)
# cv2.imshow('MEAN_C', thr2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 1. 모든 윤곽을 찾는다.
# 2. 경계 상자 목록을 만든다. (각 윤곽선마다 하나의 상자)
# 3. 가장 오른쪽 테두리 상자인지 확인한다.
# 4. 다른 모든 상자의 (x, y, 너비, 높이) 정보를 사용하여 ROI를 만들고 숫자 만 자릅니다.


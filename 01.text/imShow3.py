import cv2
import matplotlib.pyplot as plt

# , cv2.IMREAD_GRAYSCALE
img = cv2.imread('./images/4.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, origin = cv2.threshold(img_gray, 127, 255, 0)
thr1 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
thr2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# 필요없는 변수는 _로 지정 가능
# _, contours, _ = cv2.findContours(origin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# image, contours, hierarchy = cv2.findContours(origin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# 윤곽선으로 상자 만들기
contours, hierachy = cv2.findContours(thr2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
cv2.imshow('contour', img)

# thr1 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# thr2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imshow('global threshold', img_gray)
# cv2.imshow('GAUSSIAN_C', thr1)
# cv2.imshow('MEAN_C', thr2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 1. 모든 윤곽을 찾는다.
# 2. 경계 상자 목록을 만든다. (각 윤곽선마다 하나의 상자)
# 3. 가장 오른쪽 테두리 상자인지 확인한다.
# 4. 다른 모든 상자의 (x, y, 너비, 높이) 정보를 사용하여 ROI를 만들고 숫자 만 자릅니다.


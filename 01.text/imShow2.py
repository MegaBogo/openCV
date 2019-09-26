import cv2

img = cv2.imread('./images/3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('thresh', thresh)

im2, ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)

    roi = img[y:y + h, x:x + w]

    area = w*h

    if 250 < area < 900:
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('rect', rect)

cv2.waitKey(0)

# 출처 https://codeday.me/ko/qa/20190503/448210.html
import cv2
import matplotlib.pyplot as plt

#회색
grayImg = cv2.imread('./images/1.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(grayImg, cmap='gray', interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()

cv2.waitKey(0) #아무키나 누르면 지나감 안에 값이 1이면 그냥 지나가지만 키를 눌렀을때 반응함
cv2.destroyAllWindows()
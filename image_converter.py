import cv2

vid = cv2.VideoCapture("stored.mp4")
ret, frame = vid.read()
i = 0
while ret:
    cv2.imwrite('images/pic%d.png'%i, frame)
    ret, frame = vid.read()
    i += 1

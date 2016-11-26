import cv2

# Make image into grayscale
image = cv2.imread("randomPic.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect Face with HAAR cascades
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
rects = detector.detectMultiScale(gray, scaleFactor=2.05, minNeighbors=9,
	minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

# loop the face & draw a rectangle
for (x, y, w, h) in rects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show the drawn rectangle
cv2.imshow("Faces", image)
cv2.waitKey(0)

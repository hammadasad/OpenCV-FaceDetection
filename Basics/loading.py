import argparse
import cv2

#parse cmd arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

#show the image & display properties
image = cv2.imread(args["image"])
print "width: %d pixels" % (image.shape[1])
print "height: %d pixels" % (image.shape[0])
print "channels: %d" % (image.shape[2])

#show the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("image.jpg", image)

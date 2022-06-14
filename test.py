import ObjectDetection as objd
import cv2
#from Communication import *
from videoProcessor import upload2s3
img = cv2.imread("test.jpeg")
r = objd.person(img)

inf = objd.plot_many_box(img,r["bb"],label="person")
cv2.imwrite("inf.jpeg", inf)
url = upload2s3.upload_simple("inf.jpeg")
#producer.publish_message({"inference":url})

print(url)
print("________________DONE____________________")




import ObjectDetection as objd
import cv2
#from Communication import *
from Upload import upload_simple
import YouGet

url = "https://drive.google.com/file/d/1dBapERKYoeaalXm40a4ytNKr6q5Lprn7/view?usp=sharing"
path, s = YouGet.download(url,"test",objd.config.workin_dir+"/Data", ".jpg")
img = cv2.imread(path)
r = objd.person(img)

inf = objd.plot_many_box(img,r["bb"],label=["person"]*len(r["bb"]))
cv2.imwrite("inf.jpeg", inf)
url = upload_simple("inf.jpeg")
#producer.publish_message({"inference":url})

print(url)
print("________________DONE____________________")



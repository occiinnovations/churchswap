import cv2
import numpy as np
from ultralytics import YOLO

my_stream0 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
my_stream1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)

model = YOLO("models/yolov8n.pt")

selected = "0"  # default

while True:
    ret1, frame1 = my_stream1.read()
    ret0, frame0 = my_stream0.read()

    the_key = cv2.waitKey(1) & 0xFF

    the_dict = {
        "0": frame0,
        "1": frame1,
        "q": "end"
    }

    for a_key in the_dict.keys():
        if the_key == ord(a_key):
            selected = a_key

    if selected == "q":
        break
    cv2.imshow("my frame", the_dict[selected])

    results = model(the_dict[selected])
    anno_frame = results[0].plot()

    if selected == "q":
        break


print("simulation over")

my_stream0.release()
my_stream1.release()
cv2.destroyAllWindows()

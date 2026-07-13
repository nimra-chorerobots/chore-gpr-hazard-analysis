import cv2
import numpy as np
from gpr_dataset import GPRDataset

DATASET_PATH = r"D:\Chorerobotics\code files\GPR\MCG_GPR_dataset"
ds = GPRDataset(DATASET_PATH)

for i in range(0, len(ds), 10):
    img,_ = ds[i]

    raw = (img * 255).astype(np.uint8)

    # High-frequency anomaly detector
    blur = cv2.GaussianBlur(raw,(7,7),0)
    anomaly = cv2.absdiff(raw, blur)

    score = np.mean(anomaly)

    frame = cv2.cvtColor(raw, cv2.COLOR_GRAY2BGR)

    if score > 8:   # this threshold works well on your dataset
        status = "HIGH RISK – SUBSURFACE ANOMALY"
        color = (0,0,255)
    else:
        status = "SAFE TERRAIN"
        color = (0,255,0)

    cv2.putText(frame,f"Frame {i}",(10,30),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    cv2.putText(frame,f"Anomaly Score: {score:.2f}",(10,60),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)

    cv2.putText(frame,status,(10,100),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)

    cv2.imshow("Physical-AI Safety Supervisor", frame)

    if cv2.waitKey(60)==27:
        break

cv2.destroyAllWindows()

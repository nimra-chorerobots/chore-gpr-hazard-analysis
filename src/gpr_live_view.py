import time
import cv2
from gpr_dataset import GPRDataset

DATASET_PATH = r"D:\Chorerobotics\code files\GPR\MCG_GPR_dataset"

ds = GPRDataset(DATASET_PATH)

for i in range(0, len(ds), 5):
    img, _ = ds[i]
    cv2.imshow("GPR Sensor Feed - Subsurface Radar", img)
    if cv2.waitKey(50) & 0xFF == 27:
        break

cv2.destroyAllWindows()

import cv2
import numpy as np
from gpr_dataset import GPRDataset

ds = GPRDataset(r"D:\Chorerobotics\code files\GPR\MCG_GPR_dataset")

for i in range(0, len(ds), 20):
    img,_ = ds[i]

    edges = cv2.Canny((img*255).astype(np.uint8),40,120)
    features = cv2.applyColorMap(edges, cv2.COLORMAP_JET)

    cv2.imshow("Raw GPR", img)
    cv2.imshow("Encoded Subsurface Features", features)

    if cv2.waitKey(80) == 27:
        break

cv2.destroyAllWindows()

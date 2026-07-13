import cv2, numpy as np
from gpr_dataset import GPRDataset

ds = GPRDataset(r"D:\Chorerobotics\code files\GPR\MCG_GPR_dataset")

for i in range(0, len(ds), 30):
    img,_ = ds[i]

    heat = cv2.GaussianBlur(img,(0,0),3)
    heat = cv2.normalize(heat,None,0,255,cv2.NORM_MINMAX)
    heat = cv2.applyColorMap(heat.astype(np.uint8), cv2.COLORMAP_JET)

    cv2.imshow("GPR Hazard Intensity Map", heat)

    if cv2.waitKey(80)==27:
        break
cv2.destroyAllWindows()

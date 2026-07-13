import cv2
import matplotlib.pyplot as plt

def draw_bounding_boxes(img, boxes):
    h, w = img.shape
    img_rgb = cv2.cvtColor((img*255).astype("uint8"), cv2.COLOR_GRAY2RGB)

    for b in boxes:
        cls, x, y, bw, bh = b
        x1 = int((x - bw/2) * w)
        y1 = int((y - bh/2) * h)
        x2 = int((x + bw/2) * w)
        y2 = int((y + bh/2) * h)
        cv2.rectangle(img_rgb, (x1,y1), (x2,y2), (0,255,0), 2)

    return img_rgb


def show(img, title="GPR Subsurface Perception"):
    plt.figure(figsize=(6,6))
    plt.imshow(img)
    plt.title(title)
    plt.axis("off")
    plt.show()

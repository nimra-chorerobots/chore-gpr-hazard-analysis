from gpr_dataset import GPRDataset
from visualize_gpr import draw_bounding_boxes, show

DATASET_PATH = r"D:\Chorerobotics\code files\GPR\MCG_GPR_dataset"

dataset = GPRDataset(DATASET_PATH)

print("Total Frames:", len(dataset))

for i in range(5):
    img, boxes = dataset[i]
    overlay = draw_bounding_boxes(img, boxes)
    show(overlay, title=f"GPR Frame {i} – Subsurface Object Detection")

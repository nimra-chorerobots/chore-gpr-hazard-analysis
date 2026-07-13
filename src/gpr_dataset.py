import os
import cv2
import numpy as np

class GPRDataset:
    def __init__(self, root):
        self.image_paths = []
        self.ann_paths = []

        img_root = os.path.join(root, "images")
        ann_root = os.path.join(root, "annotations")

        print("Scanning GPR dataset at:", img_root)

        for root_dir, subdirs, files in os.walk(img_root):
            for file in files:
                if file.lower().endswith((".png", ".jpg", ".jpeg")):
                    img_path = os.path.join(root_dir, file)

                    # match annotation path automatically
                    rel = os.path.relpath(img_path, img_root)
                    ann_path = os.path.join(ann_root, os.path.splitext(rel)[0] + ".txt")

                    self.image_paths.append(img_path)
                    self.ann_paths.append(ann_path)

        print("Total valid GPR frames found:", len(self.image_paths))

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        ann_path = self.ann_paths[idx]

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise RuntimeError(f"Failed to load image: {img_path}")

        img = cv2.resize(img, (256, 256))
        img = img.astype("float32") / 255.0

        if os.path.exists(ann_path):
            boxes = np.loadtxt(ann_path)
        else:
            boxes = np.empty((0,5))

        return img, boxes

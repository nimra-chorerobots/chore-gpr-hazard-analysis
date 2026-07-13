# Chore GPR Hazard Analysis

### Real-Time Ground Penetrating Radar (GPR) Visualization, Feature Extraction, and Subsurface Hazard Analysis

This repository implements a real-time **Ground Penetrating Radar (GPR) perception pipeline** for robotics and infrastructure inspection. It processes GPR B-scan data to visualize underground reflections, extract meaningful subsurface features, estimate anomaly levels, and provide interpretable terrain hazard analysis through an interactive visualization dashboard.

Unlike conventional perception systems that focus only on above-ground obstacles, this pipeline analyzes subsurface radar reflections to help identify buried utilities, cavities, and other underground anomalies before robotic or engineering operations.

---

# 📌 Overview

Ground Penetrating Radar (GPR) is a non-destructive sensing technology that transmits electromagnetic waves into the ground and records reflected signals from buried objects, material boundaries, and subsurface structures.

This repository demonstrates a complete perception workflow consisting of:

- Raw GPR B-scan visualization
- Signal preprocessing
- Feature extraction
- Encoded feature representation
- Hazard score estimation
- Terrain safety assessment
- Live visualization dashboard

The repository is intended for:

- Robotics research
- Infrastructure inspection
- Underground utility detection
- Construction monitoring
- Civil engineering
- Subsurface perception research
- Educational demonstrations

---

# 🚀 Features

- Real-time GPR visualization
- B-scan processing
- Feature extraction
- Encoded subsurface representation
- Hazard score estimation
- Terrain safety assessment
- Live visualization windows
- Modular processing pipeline

---

# 📂 Dataset

The project processes Ground Penetrating Radar (GPR) B-scan images organized into multiple semantic classes.

```text
gpr_dataset/
├── intact/
├── utilities/
├── cavities/
├── augmented_intact/
├── augmented_utilities/
└── augmented_cavities/
```

Dataset classes represent:

- **Intact** — Normal subsurface reflections
- **Utilities** — Buried pipes, conduits, and underground infrastructure
- **Cavities** — Underground voids and anomalous structures
- **Augmented** — Synthetic variations for improved dataset diversity

---

# 🔄 Processing Pipeline

```text
Ground Penetrating Radar
            │
            ▼
Raw B-Scan Formation
            │
            ▼
Signal Preprocessing
            │
            ▼
Feature Extraction
            │
            ▼
Encoded Feature Representation
            │
            ▼
Hazard Score Estimation
            │
            ▼
Terrain Safety Assessment
            │
            ▼
Interactive Visualization Dashboard
```

---

# 🏗 Perception Architecture

```text
Ground Penetrating Radar
        │
        ▼
Raw B-Scan
        │
        ▼
Signal Preprocessing
        │
        ▼
Feature Extraction
        │
        ▼
Feature Encoding
        │
        ▼
Hazard Analysis
        │
        ▼
Terrain Safety Assessment
        │
        ▼
Visualization Dashboard
```

---

# 🖥 Visualization Outputs

The following figures illustrate each stage of the GPR perception and hazard analysis pipeline.

---

## Figure 1 — Raw GPR B-Scan: Subsurface Reflection Profile

Displays the original subsurface radar reflection profile before processing.

<img width="321" height="360" alt="Screenshot_1" src="https://github.com/user-attachments/assets/60e7a4f1-8d41-4973-80d5-31134525650e" />

---

## Figure 2 — High-Frequency Radar Texture

Highlights clutter, micro-reflections, and enhanced radar structures after preprocessing.

<img width="315" height="358" alt="Screenshot_2" src="https://github.com/user-attachments/assets/f0e0d51f-e7b7-469d-b128-ad630cec2350" />

---

## Figure 3 — Encoded Subsurface Feature Map

Displays the encoded feature representation emphasizing important underground structures.

<img width="511" height="547" alt="Screenshot_3" src="https://github.com/user-attachments/assets/3f7de418-f9de-4d8d-9085-d419face5589" />

---

## Figure 4 — Raw GPR vs Encoded Feature Representation

Comparison between the original radar reflections and the encoded feature map.

<img width="633" height="354" alt="Screenshot_4" src="https://github.com/user-attachments/assets/56e2eac9-5145-4590-bedb-fdfa2cf73744" />

---

## Figure 5 — Terrain Safety Assessment: SAFE TERRAIN

Example of a radar frame with a relatively low anomaly score indicating stable subsurface conditions.

<img width="322" height="359" alt="Screenshot_5" src="https://github.com/user-attachments/assets/b53fb331-c278-410f-89a8-c20cf87a5f47" />

---

## Figure 6 — Terrain Safety Assessment: HIGH-RISK Subsurface Anomaly

Example of a radar frame with an elevated anomaly score highlighting suspicious underground reflections.

<img width="319" height="355" alt="Screenshot_6" src="https://github.com/user-attachments/assets/9e10eab1-8adc-44bd-85ae-b13656a474dc" />

---

*All visualization windows are generated live while processing the GPR data.*

---

# 📈 Representative Capabilities

The pipeline demonstrates:

- Live GPR visualization
- Signal preprocessing
- Feature enhancement
- Encoded feature-map generation
- Qualitative anomaly estimation
- Hazard-score visualization
- Terrain safety assessment
- Interactive subsurface perception

---

# 📂 Repository Structure

<img width="297" height="239" alt="Repository Structure" src="https://github.com/user-attachments/assets/c3301540-e897-4944-b3b1-0ebf2eb73784" />

---

# 🔧 File Responsibilities

| Script | Description |
|---------|-------------|
| `gpr_dataset.py` | Multi-folder GPR dataset loader |
| `gpr_live_view.py` | Live GPR B-scan visualization |
| `gpr_feature_map.py` | Subsurface feature extraction and encoding |
| `gpr_hazard_map.py` | Hazard-score estimation and visualization |
| `gpr_safety_supervisor.py` | Terrain safety assessment based on anomaly levels |
| `main_demo.py` | Main demonstration pipeline integrating all processing stages |

---

# 🚀 Project Status

🟢 **Prototype**

### Current Features

- Live GPR visualization
- Signal preprocessing
- Feature extraction
- Encoded feature maps
- Hazard-score estimation
- Terrain safety assessment
- Interactive visualization dashboard

### Planned Improvements

- ROS 2 integration
- NVIDIA Isaac Sim integration
- Machine-learning-based anomaly detection
- Multi-sensor perception
- Real-time deployment
- Quantitative hazard estimation

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/nimra-chorerobots/chore-gpr-hazard-analysis.git

cd chore-gpr-hazard-analysis
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install numpy opencv-python matplotlib
```

---

# 📦 Requirements

- Python 3.9+
- NumPy
- OpenCV
- Matplotlib

Example `requirements.txt`

```text
numpy
opencv-python
matplotlib
```

---

# ▶️ Running the Project

Run the complete demonstration:

```bash
python src/main_demo.py
```

The application will open multiple visualization windows showing:

- Raw GPR B-scans
- Feature maps
- Encoded representations
- Hazard analysis
- Terrain safety assessment

---

# 💡 Applications

This repository can be used for:

- Ground Penetrating Radar research
- Underground utility inspection
- Infrastructure monitoring
- Construction analysis
- Civil engineering
- Robotics perception research
- Educational demonstrations
- Subsurface hazard visualization

---

# 🔮 Future Work

Future versions will include:

- Machine-learning-based anomaly detection
- ROS 2 integration
- NVIDIA Isaac Sim integration
- Multi-sensor fusion
- Interactive dashboard improvements
- Real-time deployment optimization

 

# Chore GPR Hazard Analysis

### Real-Time Ground Penetrating Radar (GPR) Visualization, Feature Extraction, and Subsurface Hazard Analysis

This repository implements a real-time Ground Penetrating Radar (GPR) perception pipeline for qualitative subsurface inspection. It processes radar B-scan data to visualize underground reflections, enhance meaningful features, estimate anomaly levels, and provide interpretable hazard analysis for robotics and infrastructure applications.

The project demonstrates how raw GPR signals can be transformed into useful perception outputs through signal preprocessing, feature extraction, hazard scoring, and visualization.

---

# 📌 Overview

Ground Penetrating Radar (GPR) is a non-destructive sensing technology capable of detecting buried objects and subsurface structures by transmitting electromagnetic waves into the ground and analyzing reflected signals.

This repository focuses on qualitative subsurface perception by providing visualization and feature analysis tools that help identify underground anomalies before further processing or robotic deployment.

The pipeline performs:

- Raw GPR B-scan visualization
- Signal preprocessing
- Feature extraction
- Encoded feature-map generation
- Hazard-score estimation
- Live visualization
- Terrain interpretation

The repository is intended for:

- Robotics research
- GPR signal analysis
- Infrastructure inspection
- Underground utility detection
- Construction monitoring
- Educational demonstrations
- Subsurface perception research

---

# 🚀 Features

- Multi-folder GPR dataset processing
- Real-time B-scan visualization
- Feature enhancement
- Encoded subsurface representation
- Hazard-score estimation
- Live anomaly visualization
- Modular processing pipeline
- Interpretable visualization outputs

---

# 📂 Dataset

The project processes Ground Penetrating Radar B-scan images organized into multiple semantic classes.

Example dataset structure:

```text
gpr_dataset/
├── intact/
├── utilities/
├── cavities/
├── augmented_intact/
├── augmented_utilities/
└── augmented_cavities/
```

Dataset categories represent:

- **Intact** — Normal subsurface reflections
- **Utilities** — Buried pipes and underground infrastructure
- **Cavities** — Underground voids and anomalous structures
- **Augmented** — Synthetic variations for improved dataset diversity

---

# 🔄 Processing Pipeline

```text
Ground Penetrating Radar
            │
            ▼
Raw B-Scan Acquisition
            │
            ▼
Signal Preprocessing
            │
            ▼
Feature Extraction
            │
            ▼
Encoded Feature Map
            │
            ▼
Hazard Score Estimation
            │
            ▼
Live Visualization
            │
            ▼
Subsurface Interpretation
```

---

# ⚙️ Core Components

## 1️⃣ Raw GPR Visualization

Displays the original radar B-scan reflections captured from the subsurface.

Purpose:

- Reflection inspection
- Layer identification
- Signal quality assessment

---

## 2️⃣ Feature Extraction

Enhances meaningful radar reflections while suppressing background clutter.

Generated outputs include:

- Enhanced reflections
- High-frequency texture
- Reflection edges
- Buried-object signatures

---

## 3️⃣ Encoded Feature Representation

Transforms processed radar signals into encoded feature maps that emphasize important subsurface structures.

These representations simplify interpretation while preserving important underground information.

---

## 4️⃣ Hazard Score Estimation

Each radar frame is analyzed to estimate an anomaly score representing the likelihood of unusual subsurface reflections.

Higher scores generally indicate stronger anomalies such as:

- Buried utilities
- Cavities
- Strong reflection regions
- Unusual underground structures

---

## 5️⃣ Live Visualization

The pipeline continuously updates visualization windows during execution.

Generated outputs include:

- Raw GPR B-scan
- Processed radar image
- Feature map
- Hazard visualization
- Encoded representation

The visualization is intended for qualitative analysis rather than automated decision-making.

---

# 🖥 Visualization Outputs

The project generates several visualization stages throughout execution.

## Figure 1 — Raw GPR B-Scan

Displays the original subsurface reflection profile.

*(Insert existing Figure 1)*

---

## Figure 2 — High-Frequency Texture

Highlights clutter and micro-reflection structures.

*(Insert existing Figure 2)*

---

## Figure 3 — Encoded Feature Map

Displays encoded subsurface representations used for qualitative inspection.

*(Insert existing Figure 3)*

---

## Figure 4 — Raw vs Encoded Comparison

Compares original radar reflections with encoded feature maps.

*(Insert existing Figure 4)*

---

## Figure 5 — Hazard Visualization (Low Anomaly)

Illustrates radar frames containing relatively normal subsurface structures.

*(Insert existing Figure 5)*

---

## Figure 6 — Hazard Visualization (High Anomaly)

Shows frames containing stronger anomalous reflections and elevated hazard scores.

*(Insert existing Figure 6)*

---

# 📈 Representative Capabilities

The pipeline demonstrates:

- Continuous GPR visualization
- Subsurface feature enhancement
- Encoded radar representations
- Qualitative anomaly estimation
- Hazard-score visualization
- Real-time perception workflow

The project is intended for visualization and interpretation of GPR signals rather than automated underground classification.

---

# 🏗 Architecture

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
Hazard Score Estimation
        │
        ▼
Visualization Dashboard
```

---

# 🚀 Project Status

🟢 **Prototype**

### Current Features

- Live GPR visualization
- Signal preprocessing
- Feature extraction
- Encoded feature maps
- Hazard-score estimation
- Modular visualization pipeline

### Planned Improvements

- ROS 2 integration
- NVIDIA Isaac Sim integration
- Machine-learning-based anomaly detection
- Multi-sensor perception
- Quantitative hazard estimation
- Real-time deployment optimization

---

# 📂 Repository Structure

```text
chore-gpr-hazard-analysis/
│
├── src/
│   ├── gpr_dataset.py
│   ├── gpr_live_view.py
│   ├── gpr_feature_map.py
│   ├── gpr_hazard_map.py
│   ├── gpr_safety_supervisor.py
│   └── main_demo.py
│
├── assets/
│   ├── input/
│   ├── output/
│   └── examples/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── CHANGELOG.md
└── CITATION.cff
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/nimra-chorerobots/chore-gpr-hazard-analysis.git

cd chore-gpr-hazard-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
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

Run the main demonstration:

```bash
python src/main_demo.py
```

The application will open multiple visualization windows that update continuously while processing the GPR data.

---

# 💡 Applications

This repository can be used for:

- Ground Penetrating Radar research
- Subsurface visualization
- Underground utility inspection
- Infrastructure monitoring
- Construction analysis
- Educational demonstrations
- Robotics perception research
- Hazard visualization

---

# 🔮 Future Work

Future versions of this repository will include:

- Machine-learning-based anomaly detection
- Quantitative hazard scoring
- ROS 2 integration
- NVIDIA Isaac Sim integration
- Multi-sensor fusion
- Interactive visualization dashboard
- Real-time deployment
- Automated subsurface interpretation

 

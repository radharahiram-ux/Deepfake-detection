<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=1000&color=00BFFF&center=true&vCenter=true&width=700&lines=Deepfake+Detection+using+Deep+Learning;ResNext+%2B+LSTM+%7C+93%25+Accuracy;Transfer+Learning+%7C+Django+%7C+Docker" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)

[![Stars](https://img.shields.io/github/stars/abhijitjadhav1998/Deepfake_detection_using_deep_learning?style=social)](https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning/stargazers)
[![Forks](https://img.shields.io/github/forks/abhijitjadhav1998/Deepfake_detection_using_deep_learning?style=social)](https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning/network/members)
[![Issues](https://img.shields.io/github/issues/abhijitjadhav1998/Deepfake_detection_using_deep_learning?style=social)](https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning/issues)

</div>

---

## 🚀 Latest Update

> **Docker support is live!**
> The [Django Application](https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning/tree/master/Django%20Application) is now fully Dockerised — spin up the entire stack in seconds with zero dependency headaches.

```bash
docker-compose up --build
```

---

## 📋 Table of Contents

<details open>
<summary><b>Click to expand / collapse</b></summary>

- [Introduction](#-introduction)
- [Directory Structure](#-directory-structure)
- [System Architecture](#-system-architecture)
- [Demo](#-demo)
- [Results](#-results)
- [Roadmap & Contributions](#-roadmap--open-source-contributions)
- [License](#-license)

</details>

---

## 🧠 Introduction

This project detects **video deepfakes** using a hybrid deep learning pipeline combining **ResNext CNN** and **LSTM**:

| Step | Component | Role |
|------|-----------|------|
| 1 | **ResNext CNN** (pretrained) | Extracts rich spatial feature vectors per frame |
| 2 | **LSTM** | Learns temporal patterns across frame sequences |
| 3 | **Classifier** | Outputs Real / Fake prediction with confidence |

> Transfer learning on ResNext enables strong generalisation even with limited training data. The LSTM captures temporal inconsistencies that single-frame models miss.

<details>
<summary><b>📚 Read more & resources</b></summary>

<br/>

- 📄 [Full Documentation](https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning/tree/master/Documentation)
- 🎥 [Project Walkthrough — YouTube](https://www.youtube.com/watch?v=_q16aJTXVRE)
- 📺 [Step-by-step Installation Playlist](https://www.youtube.com/watch?v=quJ8Rv84oA0&list=PLNIj0dkfMA1FsD5xR4IEc8vdwr66_WExl)
- ✍️ [Medium Article](https://abhijithjadhav.medium.com/deepfake-video-detection-using-long-short-term-memory-df3674f83ecc)

</details>

---

## 📁 Directory Structure

```
Deepfake_detection_using_deep_learning/
│
├── 🌐 Django Application/     ← Web app for video upload & live prediction
│
├── 🔬 Model Creation/         ← Training pipeline, notebooks & scripts
│
└── 📄 Documentation/          ← Architecture docs, reports & references
```

<details>
<summary><b>What's inside each folder?</b></summary>

<br/>

**🌐 Django Application**
A fully functional web application where users can upload a video file and get a real/fake prediction rendered on screen. Supports Docker deployment.

**🔬 Model Creation**
Step-by-step Jupyter notebooks and scripts covering data preprocessing, feature extraction with ResNext, LSTM training, and model evaluation.

**📄 Documentation**
All project documentation including system design, methodology, results analysis, and references.

</details>

---

## 🏗️ System Architecture

<p align="center">
  <img src="https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning/blob/master/github_assets/System%20Architecture.png" alt="System Architecture" width="85%"/>
</p>

<details>
<summary><b>Architecture breakdown</b></summary>

<br/>

```
Input Video
    │
    ▼
Frame Extraction (N frames sampled uniformly)
    │
    ▼
ResNext-50 CNN  ──►  Feature Vector (per frame)
    │
    ▼
LSTM Layer  ──►  Temporal sequence modelling
    │
    ▼
Fully Connected + Softmax
    │
    ▼
Output: REAL / FAKE + Confidence %
```

</details>

---

## 🎬 Demo

<p align="center">
  <img src="https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning/blob/master/github_assets/fakegif.gif" alt="Demo GIF" width="80%"/>
</p>

<div align="center">

▶️ **[Watch Full Demo on YouTube](https://www.youtube.com/watch?v=_q16aJTXVRE&t=823s)**

</div>

---

## 📊 Results

All models trained on **6,000 videos**. Accuracy increases with more frames — at the cost of compute.

| Model | Frames | Accuracy | Performance |
|-------|--------|----------|-------------|
| `model_84_acc_10_frames_final_data.pt` | 10 | 84.21% | `████████░░` |
| `model_87_acc_20_frames_final_data.pt` | 20 | 87.79% | `████████░░` |
| `model_89_acc_40_frames_final_data.pt` | 40 | 89.35% | `█████████░` |
| `model_90_acc_60_frames_final_data.pt` | 60 | 90.59% | `█████████░` |
| `model_91_acc_80_frames_final_data.pt` | 80 | 91.50% | `█████████░` |
| `model_93_acc_100_frames_final_data.pt` | 100 | **93.59%** | `█████████▉` |

> **Best model:** `model_93_acc_100_frames_final_data.pt` — **93.59% accuracy** at 100 frames.

<details>
<summary><b>Choosing the right model for your use case</b></summary>

<br/>

| Use Case | Recommended Model | Why |
|----------|-------------------|-----|
| Real-time / low latency | 10–20 frames | Fast inference |
| Balanced performance | 40–60 frames | Good accuracy, moderate compute |
| Maximum accuracy | 100 frames | Best results, higher GPU cost |

</details>

---

## 🗺️ Roadmap & Open Source Contributions

We welcome contributions! Here's the current roadmap:

### ✅ Completed

- [x] Dockerising the Django application
- [x] Support for non-CUDA machines (CPU / AMD GPU)

### 🔧 Open Issues — Help Wanted!

- [ ] Deploy application to free cloud (e.g. Render, Railway, HuggingFace Spaces)
- [ ] Create an open source REST API for deepfake detection
- [ ] Batch-process entire videos instead of only the first `x` frames
- [ ] Optimise inference pipeline for faster execution

<details>
<summary><b>How to contribute</b></summary>

<br/>

1. Fork this repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add: your feature description'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

New ideas are always appreciated — open an [Issue](https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning/issues) to discuss!

</details>

---

## 🐳 Quick Start with Docker

```bash
# 1. Clone the repository
git clone https://github.com/abhijitjadhav1998/Deepfake_detection_using_deep_learning.git
cd Deepfake_detection_using_deep_learning

# 2. Navigate to Django Application
cd "Django Application"

# 3. Build and run with Docker
docker-compose up --build

# 4. Visit http://localhost:8000
```

<details>
<summary><b>Manual setup (without Docker)</b></summary>

<br/>

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

See the [installation playlist](https://www.youtube.com/watch?v=quJ8Rv84oA0&list=PLNIj0dkfMA1FsD5xR4IEc8vdwr66_WExl) for a full walkthrough.

</details>

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)

---

<div align="center">

### ⭐ If this project helped you, please star the repo — it really helps!

[![Star History Chart](https://api.star-history.com/svg?repos=abhijitjadhav1998/Deepfake_detection_using_deep_learning&type=Date)](https://star-history.com/#abhijitjadhav1998/Deepfake_detection_using_deep_learning&Date)

</div>

# 🎨 AI Creative Design Assistant

> Generate social-media-ready posters in minutes — powered by computer vision, automated design intelligence, and platform-aware rendering.

**[Live Demo →](https://ai-creative-design-assistant.streamlit.app/)** | Built with Python & Streamlit

---

## 📌 What It Does

Upload any image, add your title and subtitle — the app analyzes your image and generates three ready-to-post poster variants with automatically optimized typography, layout, and contrast. No design skills needed.

---

## 🧠 How It Works — Technical Overview

This isn't a template filler. The app makes real design decisions based on image analysis:

- **Scene Classification** — pretrained ResNet18 classifies the image into scene categories (nature, city, indoor) to inform layout strategy
- **Dominant Color Extraction** — KMeans clustering extracts color palette and detects warm/cool tone
- **Contrast & Brightness Analysis** — computes luminance using weighted RGB decomposition to auto-select black/white font
- **Texture Gradient Analysis** — finds low-noise image regions for safe, readable text placement
- **Rule-based Design Engine** — chains all features into layout decisions (position, shadow, emphasis)
- **3 Design Variants** — distinct typography and spacing combinations with explainable reasoning
- **Platform-optimized Export** — correct dimensions for LinkedIn, Instagram, and YouTube

---

## ✨ Features

- Upload custom background image or select from curated samples
- Title and subtitle input with font selection
- Auto font color and size selection based on image analysis
- 3 poster variants with design decision explanations
- Live preview in LinkedIn, Instagram, YouTube dimensions
- Download in all three platform sizes

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend & Deployment | Streamlit, Streamlit Cloud |
| Image Processing & CV | OpenCV, Pillow (PIL), NumPy |
| Deep Learning | PyTorch, ResNet18 (pretrained) |
| Clustering | Scikit-learn (KMeans) |
| Language | Python |

---

## 📸 Screenshots

*(Drag and drop your screenshots here)*

---

## 🚀 Run Locally
```bash
git clone https://github.com/yourusername/your-repo-name
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
```

---

## 🗺️ Roadmap

- [ ] Prompt-to-image background generation via API
- [ ] Drag-and-drop text positioning
- [ ] Template system with pre-designed layouts
- [ ] Batch export as ZIP

---

*Built by [Nisha Kumari](https://www.linkedin.com/in/nisha-kumari-41b69125b/))*

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

### App Interface
<img width="700" alt="Screenshot 2026-03-27 154729" src="https://github.com/user-attachments/assets/a5b958c1-b2ef-497f-9d39-313c1f1dfba7" />

### Generated Poster Outputs

**Custom Content Example**

<img width="350" alt="composed_1774606864" src="https://github.com/user-attachments/assets/446be2fb-530a-4098-a3c3-6c5f23e0db32" />



| LinkedIn Format | Instagram Format |
|---|---|
| <img width="350" alt="LinkedIn Poster" src="https://github.com/user-attachments/assets/d5180116-a80f-4037-8250-443d6442c24a" /> | <img width="270" alt="Instagram Poster" src="https://github.com/user-attachments/assets/f6e91c13-589c-415d-b4bd-63138dd20cf4" /> |

*Same poster automatically adapted for different platform dimensions*

---

## 🚀 Run Locally
```bash
git clone https://github.com/nishak05/AI-Creative-Design-Assistant
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
```

---

## 🗺️ Roadmap

- [ ] Prompt-to-image background generation via API
- [ ] Advanced typography positioning — refine scene-aware text placement for edge cases to ensure consistent readability across all image types and aspect ratios
- [ ] Drag-and-drop text positioning
- [ ] Template system with pre-designed layouts
- [ ] Batch export as ZIP

---

*Built by [Nisha Kumari](https://www.linkedin.com/in/nisha-kumari-41b69125b/)*

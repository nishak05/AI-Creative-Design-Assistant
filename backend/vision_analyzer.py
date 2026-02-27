import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import cv2
import requests
import json

# Load pretrained ResNet once (global)
_scene_model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
_scene_model.eval()

# ImageNet class labels
with requests.get("https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt") as r:
    IMAGENET_CLASSES = r.text.strip().split("\n")


# Preprocessing transform
_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def classify_scene(image: Image.Image):
    """
    Returns high-level scene category + confidence
    """

    img_tensor = _transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = _scene_model(img_tensor)
        probs = torch.nn.functional.softmax(outputs[0], dim=0)

    top_prob, top_catid = torch.topk(probs, 1)
    label = IMAGENET_CLASSES[top_catid.item()]
    confidence = float(top_prob.item())

    # Map to simplified categories
    label_lower = label.lower()

    if any(word in label_lower for word in ["forest", "mountain", "valley", "beach", "lake", "river", "desert"]):
        scene = "nature"
    elif any(word in label_lower for word in ["building", "street", "tower", "bridge", "city"]):
        scene = "city"
    elif any(word in label_lower for word in ["office", "room", "library", "studio"]):
        scene = "indoor"
    elif any(word in label_lower for word in ["night", "dark"]):
        scene = "night"
    elif any(word in label_lower for word in ["abstract", "pattern"]):
        scene = "abstract"
    else:
        scene = "general"

    return {
        "scene": scene,
        "confidence": round(confidence, 3),
        "raw_label": label
    }

def normalize_scene(scene_info):
    """
    Makes scene usable only if confidence is meaningful.
    """

    confidence = scene_info["confidence"]

    # If confidence too low → ignore model guess
    if confidence < 0.20:
        return {
            "scene": "unknown",
            "confidence": confidence,
            "usable": False,
            "raw_label": scene_info["raw_label"]
        }

    return {
        "scene": scene_info["scene"],
        "confidence": confidence,
        "usable": True,
        "raw_label": scene_info["raw_label"]
    }

def extract_dominant_colors(image: Image.Image, k=5):
    """
    Returns dominant color palette using KMeans
    """

    img = image.resize((200, 200))
    img_np = np.array(img)
    img_np = img_np.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(img_np)

    colors = kmeans.cluster_centers_
    colors = colors.astype(int)

    palette = [list(map(int, color)) for color in colors]


    return palette

def compute_image_metrics(image: Image.Image):
    """
    Computes brightness & contrast
    """

    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    brightness = float(np.mean(gray))
    contrast = float(np.std(gray))

    if contrast < 40:
        contrast_level = "low"
    elif contrast < 80:
        contrast_level = "medium"
    else:
        contrast_level = "high"

    return {
        "brightness_mean": round(brightness, 2),
        "contrast_std": round(contrast, 2),
        "contrast_level": contrast_level
    }

def compute_texture_density(image: Image.Image):
    """
    Measures how visually busy the image is using edge detection.
    """

    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Sobel edges
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = np.sqrt(sobelx**2 + sobely**2)
    density = float(np.mean(magnitude))

    if density < 20:
        level = "smooth"
    elif density < 50:
        level = "moderate"
    else:
        level = "busy"

    return {
        "texture_density": round(density, 2),
        "texture_level": level
    }

def detect_color_temperature(palette):
    """
    Estimates warm / cool / neutral tone from dominant colors.
    """

    avg_r = np.mean([c[0] for c in palette])
    avg_g = np.mean([c[1] for c in palette])
    avg_b = np.mean([c[2] for c in palette])

    if avg_r > avg_b + 15:
        tone = "warm"
    elif avg_b > avg_r + 15:
        tone = "cool"
    else:
        tone = "neutral"

    return {
        "avg_rgb": [int(avg_r), int(avg_g), int(avg_b)],
        "color_tone": tone
    }

def design_decision_engine(analysis, title, subtitle):
    """
    AI-style decision layer based on vision signals.
    """

    scene = analysis["scene_info"]["scene"]
    brightness = analysis["brightness_mean"]
    contrast = analysis["contrast_level"]
    texture = analysis["texture_level"]
    tone = analysis["color_tone"]

    has_subtitle = bool(subtitle.strip())
    title_length = len(title)

    # Text color decision
    if brightness < 110:
        text_color = "white"
    elif brightness > 180:
        text_color = "black"
    else:
        text_color = "white" if contrast == "low" else "black"

    # Layout bias
    if texture == "busy":
        layout = "lower-third"
    elif texture == "smooth":
        layout = "center"
    else:
        layout = "top-balanced"

    # Emphasis decision
    if scene == "nature":
        emphasis = "clean"
    elif scene == "city":
        emphasis = "bold"
    else:
        emphasis = "balanced"

    # Shadow intensity
    if texture == "busy":
        shadow = "strong"
    else:
        shadow = "soft"

    return {
        "ai_text_color": text_color,
        "ai_layout": layout,
        "ai_emphasis": emphasis,
        "ai_shadow": shadow
    }

def analyze_image(image: Image.Image):
    """
    Main Vision Intelligence Function
    """
    raw_scene = classify_scene(image)
    scene_info = normalize_scene(raw_scene)

    palette = extract_dominant_colors(image)
    metrics = compute_image_metrics(image)
    texture = compute_texture_density(image)
    temperature = detect_color_temperature(palette)

    analysis = {
        "scene_info": scene_info,
        "dominant_colors": palette,
        **metrics,
        **texture,
        **temperature
    }

    decision = design_decision_engine(analysis, "", "")

    analysis["design_decision"] = decision
    
    return analysis


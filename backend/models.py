from dotenv import load_dotenv
load_dotenv()
from diffusers import StableDiffusionPipeline
import torch
import requests
from io import BytesIO
from PIL import Image
import os
# print("HF_API_TOKEN loaded:", bool(os.getenv("HF_API_TOKEN")))


def load_sd_model(model_name="runwayml/stable-diffusion-v1-5", device="cuda"):
    """
    Load a Stable Diffusion pipeline. Returns the pipe object.
    """
    pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
    if device:
        pipe = pipe.to(device)
    return pipe

def generate_background(pipe, prompt, guidance_scale=7.5, num_steps=28):
    """
    Generate a single image from prompt using the provided pipeline.
    Returns a PIL Image.
    """
    result = pipe(prompt, guidance_scale=guidance_scale, num_inference_steps=num_steps)
    return result.images[0]

VARIANTS = [
    {
        "name": "Bold Title",
        "title_scale": 0.085,
        "subtitle_scale": 0.038,
        "layout": "top-heavy",
    },
    {
        "name": "Balanced",
        "title_scale": 0.075,
        "subtitle_scale": 0.035,
        "layout": "center-balanced",
    },
    {
        "name": "Compact",
        "title_scale": 0.065,
        "subtitle_scale": 0.030,
        "layout": "compact",
    },
]


# HF_ENDPOINT = "https://router.huggingface.co/api-inference/models/runwayml/stable-diffusion-v1-5"


# def generate_background_from_prompt_api(prompt: str) -> Image.Image:
#     hf_token = os.getenv("HF_API_TOKEN")
#     if not hf_token:
#         raise RuntimeError("HF_API_TOKEN not set")

#     headers = {
#         "Authorization": f"Bearer {hf_token}",
#         "Accept": "image/png",
#     }

#     payload = {
#         "inputs": prompt,
#         "options": {"wait_for_model": True},
#     }

#     response = requests.post(
#         HF_ENDPOINT,
#         headers=headers,
#         json=payload,
#         timeout=180,
#     )

#     if response.status_code != 200:
#         raise RuntimeError(
#             f"Hugging Face API error {response.status_code}: {response.text}"
#         )

#     content_type = response.headers.get("content-type", "")
#     if content_type.startswith("application/json"):
#         try:
#             error_msg = response.json().get("error", "Unknown HF error")
#         except Exception:
#             error_msg = "HF returned JSON instead of image"
#         raise RuntimeError(f"Hugging Face API error: {error_msg}")

#     try:
#         img = Image.open(BytesIO(response.content))
#         img.verify()
#         return Image.open(BytesIO(response.content)).convert("RGB")
#     except Exception:
#         raise RuntimeError("HF did not return a valid image")
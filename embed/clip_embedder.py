import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from io import BytesIO
import base64

device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def generate_multimodal_embeddings(prompt=None, image=None):
    if not prompt and not image:
        raise ValueError("Provide either a text prompt or base64 image")

    if prompt and not image:
        inputs = clip_processor(text=prompt, return_tensors="pt", padding=True, truncation=True).to(device)
        with torch.no_grad():
            features = clip_model.get_text_features(**inputs)
        return features[0].cpu().tolist()

    elif image and not prompt:
        img = Image.open(BytesIO(base64.b64decode(image))).convert("RGB")
        inputs = clip_processor(images=img, return_tensors="pt").to(device)
        with torch.no_grad():
            features = clip_model.get_image_features(**inputs)
        return features[0].cpu().tolist()

    else:
        img = Image.open(BytesIO(base64.b64decode(image))).convert("RGB")
        inputs = clip_processor(text=prompt, return_tensors="pt", padding=True, truncation=True).to(device)
        with torch.no_grad():
            outputs = clip_model(**inputs)
        combined = (outputs.text_embeds[0] + outputs.image_embeds[0]) / 2
        return combined.cpu().tolist()

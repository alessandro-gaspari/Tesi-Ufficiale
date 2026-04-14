from PIL import Image
import os

for filename in os.listdir("assets"):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join("assets", filename)
        img = Image.open(path).convert("RGB")
        img.save(path)
        print(f"Convertito: {filename}")    
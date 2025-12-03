import cv2
import numpy as np
from PIL import Image

def apply_twilight_tone(image: Image.Image):
    """
    Apply twilight color grading:
    - Cooler shadows
    - Warm highlights
    - Softened contrast
    """
    img = np.array(image).astype(np.float32) / 255.0

    # Simple gradient tone mapping
    img[:, :, 0] *= 0.9  # reduce blue slightly
    img[:, :, 2] *= 1.05 # enhance red highlights

    # Clip to 0-1
    img = np.clip(img, 0, 1)
    img = (img * 255).astype(np.uint8)
    return Image.fromarray(img)

from PIL import Image, ImageDraw, ImageFilter
import numpy as np

def add_window_light(image: Image.Image, window_mask: np.ndarray):
    """
    Add warm light to window regions
    """
    img = image.convert("RGB")
    overlay = Image.new("RGB", img.size, (0,0,0))
    overlay_np = np.array(overlay)

    # Add warm glow
    overlay_np[window_mask > 0] = [255, 200, 150]

    overlay = Image.fromarray(overlay_np)
    result = Image.blend(img, overlay, alpha=0.4)
    result = result.filter(ImageFilter.GaussianBlur(2))
    return result

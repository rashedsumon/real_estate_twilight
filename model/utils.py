from PIL import Image
import numpy as np

def mask_to_pil(mask: np.ndarray):
    """
    Convert numpy mask to PIL Image
    """
    return Image.fromarray((mask*255).astype(np.uint8))

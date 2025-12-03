from diffusers import StableDiffusionInpaintPipeline
import torch
from PIL import Image

class SkyGenerator:
    def __init__(self, device='cuda'):
        self.device = device
        # Load SDXL inpainting pipeline
        self.pipe = StableDiffusionInpaintPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-inpainting",
            torch_dtype=torch.float16
        ).to(self.device)

    def generate_twilight_sky(self, image: Image.Image, sky_mask: Image.Image, prompt="Twilight sky purple-orange gradient"):
        """
        Replace sky region with twilight sky
        """
        result = self.pipe(prompt=prompt, image=image, mask_image=sky_mask).images[0]
        return result

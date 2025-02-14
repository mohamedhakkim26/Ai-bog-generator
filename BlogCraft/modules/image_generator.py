import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_images(title, num_images):
    images_gallery = []
    for i in range(num_images):
        try:
            response = openai.Image.create(
                prompt=f"Generate an image related to '{title}'",
                n=1,
                size="1024x1024",
            )
            image_url = response["data"][0]["url"]
            images_gallery.append({"title": f"Image {i+1}", "text": title, "img": image_url})
        except Exception as e:
            print(f"Failed to generate image {i+1}: {e}")
    return images_gallery

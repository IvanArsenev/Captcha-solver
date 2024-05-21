import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def generate_random_text(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def create_image_with_text(base_image_path, output_folder, num_images):
    base_image = Image.open(base_image_path)
    base_width, base_height = base_image.size
    
    font_path = r'arial.ttf'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i in range(num_images):
        image = base_image.copy()
        
        text = generate_random_text(random.randint(3, 6))
        
        font_size = 95
        
        font = ImageFont.truetype(font_path, font_size)

        text_width, text_height = font.getmask(text).getbbox()[-2:]

        x = random.randint(0, base_width - text_width)
        y = random.randint(0, base_height - text_height)
        
        draw = ImageDraw.Draw(image)
        draw.text((x, y), text, fill=(180, 180, 180, 180), font=font)
        
        output_path = os.path.join(output_folder, f"{text}.png")
        
        image = image.filter(ImageFilter.GaussianBlur(3))
        
        image.save(output_path)
        print(f"Изображение сохранено: {output_path}")

base_image_path = r'base-img.png'

output_folder = r'dataset'

num_images = 10

create_image_with_text(base_image_path, output_folder, num_images)
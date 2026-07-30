import os
from PIL import Image

image_dir = 'assets/images'
converted_count = 0

for root, _, files in os.walk(image_dir):
    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(root, filename)
            # Create webp path
            base_name = os.path.splitext(filename)[0]
            webp_path = os.path.join(root, f"{base_name}.webp")
            
            try:
                # Convert
                with Image.open(file_path) as img:
                    img.save(webp_path, 'WEBP')
                # Delete original
                os.remove(file_path)
                print(f"Converted: {filename} -> {base_name}.webp")
                converted_count += 1
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

print(f"\nSuccessfully converted {converted_count} images to .webp")

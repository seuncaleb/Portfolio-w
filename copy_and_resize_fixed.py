import os
import re
from PIL import Image

src_dir = "/Users/seuncaleb/Desktop/Project/portfolio/images"
dest_dir = "/Users/seuncaleb/Desktop/Project/portfolio/images/web"

target_images = [
    "seuncaleb_1.jpg", "seuncaleb_2.jpg", "seuncaleb_3.jpg", "seuncaleb_6.jpg", "seuncaleb9.jpg",
    "seuncaleb_7.jpg", "lagos_IMG_5691.jpg", "lagos_IMG_5692.jpg", "lagos_IMG_5784.jpg", "lagos_IMG_5785.jpg",
    "lagos_IMG_5786.jpg", "lagos_IMG_5787.jpg", "lagos_IMG_5788.jpg", "lagos_IMG_5802.jpg", "lagos_session3_IMG_9604.jpg",
    "lagos_session4_IMG_9701.jpg", "lagos_session5_IMG_9576.jpg", "lagos_session5_IMG_9583.jpg", "glasgow_IMG_3113.jpg",
    "glasgow_IMG_3114.jpg", "glasgow_IMG_3115.jpg", "glasgow_IMG_3128.jpg", "glasgow_IMG_3143.jpg", "glasgow_IMG_3144.jpg",
    "glasgow_IMG_3145.jpg", "glasgow_IMG_3146.jpg", "glasgow_IMG_3147.jpg", "glasgow_IMG_3129.jpg", "glasgow_IMG_3142.jpg",
    "lagos_session2_IMG_9649.jpg", "seuncaleb_4.jpg", "seuncaleb_5.jpg", "lagos_session2_IMG_9659.jpg", "lagos_session3_IMG_9619.jpg",
    "glasgow_IMG_3138.jpg"
]

def get_base_name(target_name):
    # Extracts the base IMG_XXXX.jpg or seuncaleb_X.jpg from the descriptive names
    match = re.search(r'(IMG_\d+(?:-\d+)?\.jpg|seuncaleb_?\d+\.jpg|seuncaleb9\.jpg)', target_name)
    if match:
        return match.group(1)
    return target_name

# Build a map of base_name -> target_name
needed_base_names = {}
for t in target_images:
    needed_base_names[get_base_name(t)] = t

found_images = {} # maps base_name -> full path to source image
for root, dirs, files in os.walk(src_dir):
    if root == dest_dir: continue
    for file in files:
        if file in needed_base_names:
            if file not in found_images: # Keep first found
                found_images[file] = os.path.join(root, file)
        elif file.lower().endswith('.heic'):
            base_jpg = file[:-5] + '.jpg'
            if base_jpg in needed_base_names and base_jpg not in found_images:
                found_images[base_jpg] = os.path.join(root, file)

for base_name, img_path in found_images.items():
    dest_filename = needed_base_names[base_name]
    try:
        dest_path = os.path.join(dest_dir, dest_filename)
        if os.path.exists(dest_path): continue
        with Image.open(img_path) as img:
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            img.thumbnail((1200, 1200))
            img.save(dest_path, 'JPEG', quality=85)
            print(f"Restored: {img_path} -> {dest_filename}")
    except Exception as e:
        print(f"Error on {dest_filename}: {e}")


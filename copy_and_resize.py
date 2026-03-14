import os
from PIL import Image

src_dir = "/Users/seuncaleb/Desktop/Project/portfolio/images"
dest_dir = "/Users/seuncaleb/Desktop/Project/portfolio/images/web"

# Create destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# List of all images referenced in the HTML file to selectively process just what we need:
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

found_images = {}
for root, dirs, files in os.walk(src_dir):
    if root == dest_dir: continue
    for file in files:
        if file in target_images:
             found_images[file] = os.path.join(root, file)

for dest_filename, img_path in found_images.items():
    try:
        dest_path = os.path.join(dest_dir, dest_filename)
        if os.path.exists(dest_path): continue
        with Image.open(img_path) as img:
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            img.thumbnail((1200, 1200))
            img.save(dest_path, 'JPEG', quality=85)
            print(f"Restored: {dest_filename}")
    except Exception as e:
        print(f"Error on {dest_filename}: {e}")


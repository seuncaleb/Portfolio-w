import os
import re
import subprocess

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
    match = re.search(r'(IMG_\d+(?:-\d+)?\.jpg|seuncaleb_?\d+\.jpg|seuncaleb9\.jpg)', target_name)
    if match: return match.group(1)
    return target_name

needed_base_names = {get_base_name(t): t for t in target_images}

found_images = {}
for root, dirs, files in os.walk(src_dir):
    if root == dest_dir: continue
    for file in files:
        if file in needed_base_names:
            if file not in found_images:
                found_images[file] = os.path.join(root, file)
        elif file.lower().endswith('.heic'):
            base_jpg = file[:-5] + '.jpg'
            if base_jpg in needed_base_names and base_jpg not in found_images:
                found_images[base_jpg] = os.path.join(root, file)

for base_name, img_path in found_images.items():
    dest_filename = needed_base_names[base_name]
    dest_path = os.path.join(dest_dir, dest_filename)
    if os.path.exists(dest_path): continue
    
    try:
        # Use macOS 'sips' command for all image processing to handle HEIC seamlessly
        print(f"Converting/resizing: {os.path.basename(img_path)} -> {dest_filename}")
        subprocess.run(['sips', '-s', 'format', 'jpeg', '-Z', '1200', img_path, '--out', dest_path], check=True, capture_output=True)
    except Exception as e:
        print(f"Error on {dest_filename}: {e}")


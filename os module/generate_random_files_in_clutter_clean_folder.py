import os
import random
import string

# 📂 Target folder to clutter (feel free to change)
target_dir = "G:\Projects\Python Learn 2024\os module\clutter_clean"

# 🔤 Function to generate messy/random file names
def generate_random_name(length=8):
    chars = string.ascii_letters + string.digits + "-_@!$"
    return ''.join(random.choices(chars, k=length))

# 🚀 Main function: clears old files & generates new ones
def generate_files(num_files):
    extensions = ['.txt', '.pdf', '.jpg', '.docx', '.csv', '.py', '.mp3']

    # 🏗️ Ensure the directory exists
    os.makedirs(target_dir, exist_ok=True)

    # 🧹 Clear all files in target_dir
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isfile(item_path):
            os.remove(item_path)

    # 🧪 Generate random files
    for _ in range(num_files):
        name = generate_random_name(random.randint(5, 12))
        ext = random.choice(extensions)
        filename = name + ext
        file_path = os.path.join(target_dir, filename)

        # 📄 Create empty file
        with open(file_path, 'w') as f:
            pass

    print(f"✅ Cleared folder and generated {num_files} new files in → {target_dir}")


generate_files(20)
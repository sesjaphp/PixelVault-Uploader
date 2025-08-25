import subprocess
import requests
import os
import dotenv
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
PIXELVAULT_URL = os.getenv("PIXELVAULT_URL")
SAVE_FOLDER = os.getenv("SAVE_FOLDER")

os.makedirs(SAVE_FOLDER, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
screenshot_path = os.path.join(SAVE_FOLDER, f"Screenshot from {timestamp}.png")

subprocess.run(["gnome-screenshot", "-a", "-f", screenshot_path])

if not os.path.exists(screenshot_path):
    exit()

files = {"file": (os.path.basename(screenshot_path), open(screenshot_path, "rb"), "image/png")}
headers = {"Authorization": API_KEY}

response = requests.post(PIXELVAULT_URL, headers=headers, files=files)

if response.status_code == 200:
    data = response.json()
    image_url = data.get("resource")
    subprocess.run(f'echo "{image_url}" | xclip -selection clipboard', shell=True)

# PixelVault Screenshot Uploader

This script allows you to take a screenshot, upload it to PixelVault, and automatically copy the image URL to your clipboard. **Note: This script is only for GNOME environments.**

## Setup

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd <repo-directory>
```

2. **Install dependencies**:

```bash
python3 -m pip install --user -r requirements.txt
```

3. **Configure environment variables**:

* Copy `example.env` to `.env`:

```bash
cp example.env .env
```

* Edit `.env` and add your PixelVault API key, URL, and screenshot save folder:

```
API_KEY=your_pixelvault_key
PIXELVAULT_URL=https://pixelvault.co/
SAVE_FOLDER=/home/username/Pictures/Screenshots
```

4. **Test the script**:

```bash
python3 main.py
```

5. **Setup a GNOME keybind**:

* Open **Settings → Keyboard → Keyboard Shortcuts → Custom Shortcuts**.
* Click **Add Custom Shortcut**:

  * **Name**: PixelVault Screenshot
  * **Command**:

    ```bash
    /home/username/path-to-repo/run_pixelvault.sh
    ```
  * **Shortcut**: Press your desired key combination (e.g., `CTRL + \`).
* Save.

Now, pressing your chosen shortcut will run the script, take a selection screenshot, upload it to PixelVault, and copy the URL to your clipboard automatically.

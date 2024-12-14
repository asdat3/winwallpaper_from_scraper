# Wallpaper Web Scraping Manager

A Python application that allows you to update your desktop wallpaper dynamically based on a screenshot of a webpage. The wallpaper is updated when a keyboard event is triggered, and the application enforces a cooldown period between updates. This project is ideal for creating a dynamic and customizable desktop experience.

---

## Features

- Captures a screenshot of a specified webpage using Puppeteer.
- Updates the desktop wallpaper with the captured screenshot.
- Enforces a cooldown period between updates to prevent excessive changes.
- Runs in the background and listens for keyboard events to trigger updates.
- Easy to host as a persistent background service using PM2.

---

## Requirements

### Software Dependencies
- **Python 3.7+**
- [Node.js](https://nodejs.org/) (for PM2 hosting, optional but recommended)
- Python libraries:
  - `playwright`
  - `asyncio`
  - `ctypes` (standard library)
  - `datetime` (standard library)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/asdat3/winwallpaper_from_scraper.git
   cd winwallpaper_from_scraper
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Node.js and PM2 are installed (optional but recommended for background hosting):
   ```bash
   npm install -g pm2
   ```

4. Install playwright (it will prompt you once you run the script)

---

## Usage

### Running the Application

1. Start the Python script:
   ```bash
   python main.py
   ```

2. Press any key to trigger the wallpaper update process.

### Hosting with PM2

Hosting the application using PM2 allows it to run seamlessly in the background and even start automatically on system boot.

1. Start the application with PM2:
   ```bash
   pm2 start main.py --interpreter python3 --name "WallpaperManager"
   ```

2. Save the PM2 process list to start on system boot:
   ```bash
   pm2 save
   pm2 startup
   ```

3. Check the application status:
   ```bash
   pm2 status
   ```

4. Stop the application:
   ```bash
   pm2 stop WallpaperManager
   ```

---

## How It Works

1. **Capture Screenshot**: The application uses Puppeteer to navigate to a webpage and capture a screenshot.
2. **Set Wallpaper**: The screenshot is saved locally and set as the desktop wallpaper using the `ctypes` library.
3. **Keyboard Event Listener**: The `keyboard` library listens for keypress events, which trigger the screenshot and wallpaper update process.
4. **Cooldown Enforcement**: A cooldown period prevents frequent updates, ensuring smooth operation.

---

## Future Enhancements (will never happen)

- Add support for customizable hotkeys.
- Allow users to specify the webpage URL dynamically.
- Implement better error handling for system-specific wallpaper settings.
- Add an interactive GUI for non-technical users.

---

## Disclaimer

This tool is intended for personal use only. Ensure compliance with the terms of service of any website accessed using this tool.

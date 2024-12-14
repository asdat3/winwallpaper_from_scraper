import asyncio
import ctypes
import os
from playwright.async_api import async_playwright

class WallpaperManager:
    def __init__(self):
        self.screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
        self.update_interval = 300  # 5 minutes
        self.website_load_time = 5
        
    async def capture_screenshot(self) -> None:
        """Captures a screenshot of the specified webpage using Firefox."""
        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=True)
            page = await browser.new_page()
            await page.set_viewport_size({"width": 1920, "height": 1080})
            await page.goto("https://www.google.com/search?q=minecraft")
            await asyncio.sleep(self.website_load_time)
            await page.screenshot(path=self.screenshot_path, full_page=True)
            await browser.close()
            print("Screenshot captured successfully")

    def set_wallpaper(self) -> bool:
        """Sets the wallpaper using the captured screenshot."""
        try:
            success = ctypes.windll.user32.SystemParametersInfoW(20, 0, self.screenshot_path, 3)
            if success:
                print("Wallpaper set successfully")
                return True
            print("Failed to set wallpaper")
            return False
        except Exception as e:
            print(f"Error setting wallpaper: {e}")
            return False

    async def update_wallpaper_loop(self):
        """Main loop to update wallpaper periodically."""
        while True:
            try:
                print("Updating wallpaper...")
                await self.capture_screenshot()
                self.set_wallpaper()
                print(f"Waiting {self.update_interval} seconds until next update...")
                await asyncio.sleep(self.update_interval)
            except Exception as e:
                print(f"Error in update loop: {e}")
                await asyncio.sleep(60)

async def main():
    """Main async function."""
    manager = WallpaperManager()
    await manager.update_wallpaper_loop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
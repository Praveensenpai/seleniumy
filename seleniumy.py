from selenium import webdriver
from selenium_stealth import stealth


class SeleniumDriver:
    def __init__(self, headless: bool = True) -> None:
        self.headless: bool = headless

    def __enter__(self) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        if self.headless:
            options.add_argument("--headless")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(
            options=options, executable_path="chromedriver.exe")

        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.driver:
            print("Cleaning up...")
            self.driver.quit()

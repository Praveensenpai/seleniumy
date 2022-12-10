from seleniumy import SeleniumDriver


with SeleniumDriver() as driver:
    url = "https://httpbin.org/ip"
    driver.get(url)

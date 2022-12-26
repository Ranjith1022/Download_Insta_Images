import requests
from datetime import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver')
driver.get("https://downloadgram.org/")

links = [
'https://www.instagram.com/p/CfTHxBuIP-E/',
'https://www.instagram.com/p/CfQp9tBD6ZO/',
'https://www.instagram.com/p/CfIe_GHJWCf/',
'https://www.instagram.com/p/CfG44idp5bo/',
'https://www.instagram.com/p/CfBp4ZZI2Xp/'
]

for index, linked in enumerate(links):
    driver.find_element("xpath", "//*[@id='url']").clear()
    driver.find_element("xpath", "//*[@id='url']").send_keys(linked)
    driver.find_element("xpath", "//*[@id='submit']").click()
    division = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[3]")
    images_count = len(division.find_elements(By.TAG_NAME, "img"))
    video_count = len(division.find_elements(By.TAG_NAME, "video"))
    if images_count > 0:
        for count in range(images_count):
            src = driver.find_element("xpath", f"/html/body/div[1]/div/div/div/div[3]/img[{count + 1}]").get_attribute(
                "src")
            now = datetime.now()
            time_now = now.strftime("%S")
            file_name = linked[28:39]
            response = requests.get(src, stream=True)
            if response.status_code == 200:
                with open(f"Sidecar/{file_name},{time_now}.jpg", 'wb') as f:
                    f.write(response.content)
    print(f"Download Completed Links: {linked} (Completed Count: {index + 1})")
    driver.refresh()
    if video_count > 0:
        for counts in range(video_count):
            src = driver.find_element("xpath",
                                      f"//*[@id='downloadhere']/video/source").get_attribute(
                "src")
            now = datetime.now()
            time_now = now.strftime("%S")
            files = linked[28:39]
            r = requests.get(src, stream=True)
            file_name = f'Sidecar/{files},{time_now}.mp4'
            with open(file_name, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
    else:
        continue

    print(f"Download Completed Links: {linked} (Completed Count: {index + 1})")
    driver.refresh()

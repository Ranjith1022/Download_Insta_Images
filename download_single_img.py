# Required Packages
from selenium import webdriver
from time import sleep
from datetime import datetime

#Define Date and Time
now = datetime.now()
# Define Chrome Driver
browser = webdriver.Chrome("chromedriver")
browser.implicitly_wait(1)
Image_Link = input("Enter Image Link: ")
browser.get(Image_Link)
sleep(1)
username_input = browser.find_element('name','username')
password_input = browser.find_element('name','password')
Username = input("Enter Instagram Username: ")
Password = input("Enter Instagram Password: ")
username_input.send_keys(Username)
password_input.send_keys(Password)
login_button = browser.find_element("xpath","//button[@type='submit']")
login_button.click()
sleep(5)
not_now = browser.find_element("xpath","//button[@type='button']").click()
# Get Image Link
sleep(3)
soup = BeautifulSoup(browser.page_source, 'lxml')
sleep(1)
img = soup.find('img', class_='pytsy3co buh8m867 s8sjc6am ekq1a7f9 f14ij5to mfclru0v')
img_url = img['src']
# Download Image File 
r = requests.get(img_url)
current_time = now.strftime(" %H%M%S")
# File Save as instagram + current_time.png
with open("instagram"+str(current_time)+".png",'wb') as f: 
    f.write(r.content)
print('Image file download successfully')

from selenium import webdriver
from time import sleep
from datetime import datetime

#Define Date and Time
now = datetime.now()
# Define Chrome Driver
browser = webdriver.Chrome("chromedriver")
browser.implicitly_wait(1)
notify = input("Goto Edit this python file give multi link as in links variable")
links = [] # Insert your download link Example: ['https://www.instagram.com/image_path','https://www.instagram.com/image_path']
for i in range(0, len(links)):    
    browser.get(links[i])
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
    with open("instagram"+str(current_time)+".png",'wb') as f: 
        f.write(r.content)
    print('Image file download successfully'+i)

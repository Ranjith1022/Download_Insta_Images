from selenium import webdriver
from time import sleep
from datetime import datetime

#Define Date and Time
now = datetime.now()
# Define Chrome Driver
browser = webdriver.Chrome("chromedriver")
browser.implicitly_wait(1)
notify = input("Goto Edit this python file give multi link as links variable")
links = ['https://www.instagram.com/p/CipPY9XBVP9/','https://www.instagram.com/p/CipPJzWB0Mu/','https://www.instagram.com/p/CipO_SSB3Bi/','https://www.instagram.com/p/CipO4mYhD3T/','https://www.instagram.com/p/CipOwwnBWs5/','https://www.instagram.com/p/CipOn03huwf/','https://www.instagram.com/p/CiiFL3rMIoY/','https://www.instagram.com/p/CiWzXs8pK3M/','https://www.instagram.com/p/CiVkuS9rTaF/','https://www.instagram.com/p/CiSFxKOvf7x/','https://www.instagram.com/p/CiPT8S-sMLJ/','https://www.instagram.com/p/CiMhBRWvHBb/','https://www.instagram.com/p/CiIpBl5rBJa/','https://www.instagram.com/p/CiFngw7hLSw/','https://www.instagram.com/p/CiFnQRPhCsQ/','https://www.instagram.com/p/CiFm_oThuT8/','https://www.instagram.com/p/CiFm1jKh3tu/','https://www.instagram.com/p/Ch6eCMgI1RQ/','https://www.instagram.com/p/Ch3_f93PC9I/','https://www.instagram.com/p/Ch1z-VsBNAm/','https://www.instagram.com/p/Ch1zJRpBrWn/','https://www.instagram.com/p/Ch1y7R3hikp/','https://www.instagram.com/p/Ch1yxwGBNhs/','https://www.instagram.com/p/Ch1yqrXhAoh/','https://www.instagram.com/p/Ch1yf6YB2Xb/','https://www.instagram.com/p/Ch1yaryB62y/','https://www.instagram.com/p/Ch1yRsehFIf/','https://www.instagram.com/p/Ch1yHAJBBJj/','https://www.instagram.com/p/Ch1x8w6hwM9/','https://www.instagram.com/p/Ch1x16eBDLX/','https://www.instagram.com/p/Ch1xvMAhDEl/','https://www.instagram.com/p/Ch1xfDVBQgA/','https://www.instagram.com/p/ChropMqJzFx/','https://www.instagram.com/p/ChoYkMBh2oz/','https://www.instagram.com/p/Chh1kXEh8GV/','https://www.instagram.com/p/Chh1gl4hsxU/','https://www.instagram.com/p/Chh1SaWBcmF/','https://www.instagram.com/p/Chh1LuPBbrJ/','https://www.instagram.com/p/Chh1F5eBFN8/','https://www.instagram.com/p/Chh095tBmPu/','https://www.instagram.com/p/Chh0x80B5X4/','https://www.instagram.com/p/ChhumBtJ3mr/','https://www.instagram.com/p/ChbezNQhySF/','https://www.instagram.com/p/ChZxZzdrYrv/','https://www.instagram.com/p/ChYxuN_v2za/','https://www.instagram.com/p/ChWkSfBrQk6/','https://www.instagram.com/p/ChWag1CrSDT/','https://www.instagram.com/p/ChT6HrMhsdF/','https://www.instagram.com/p/ChTra4cL44r/','https://www.instagram.com/p/ChR7pn8BQEm/','https://www.instagram.com/p/ChR7cfHB83D/','https://www.instagram.com/p/ChR7LHxhEvu/','https://www.instagram.com/p/ChR7CzABaQ7/','https://www.instagram.com/p/ChR66INhd9W/','https://www.instagram.com/p/ChR6ovEBfmK/','https://www.instagram.com/p/ChRgi0asL7o/','https://www.instagram.com/p/ChMI6n1sW0P/','https://www.instagram.com/p/ChJYkrtPNuT/','https://www.instagram.com/p/ChFK7xzocXs/','https://www.instagram.com/p/Cg_GM2thcTj/','https://www.instagram.com/p/Cg-RdTqPwwb/','https://www.instagram.com/p/Cg9H4RdB8Lm/','https://www.instagram.com/p/Cg9HTH8BV6z/','https://www.instagram.com/p/Cg9G_iNhvay/','https://www.instagram.com/p/Cg9GzqEh6Sr/','https://www.instagram.com/p/Cg9Gj94hfLB/','https://www.instagram.com/p/Cg9GbHTh_wY/','https://www.instagram.com/p/Cg9GVbQBv2q/','https://www.instagram.com/p/Cg9GF3KhNxB/','https://www.instagram.com/p/Cg7BG29j4_j/','https://www.instagram.com/p/Cg6rCPnBBp9/','https://www.instagram.com/p/Cg6q_iAh5jO/','https://www.instagram.com/p/Cg6HWNGMCNz/','https://www.instagram.com/p/Cg5vALgBW0h/','https://www.instagram.com/p/Cg3-8YWhDvX/','https://www.instagram.com/p/Cg3-313hquf/','https://www.instagram.com/p/Cg3oZRkAagZ/','https://www.instagram.com/p/Cg3YVMpvo7l/','https://www.instagram.com/p/Cg1kVyrB857/','https://www.instagram.com/p/CgzKLL9BQ_7/','https://www.instagram.com/p/CgvYnevv0u8/','https://www.instagram.com/p/CgrXMjQBK47/','https://www.instagram.com/p/Cgq8FQdhQqQ/','https://www.instagram.com/p/Cgq7W85hOg8/','https://www.instagram.com/p/Cgq7QA-hZnW/','https://www.instagram.com/p/Cgq7JSQh1SY/','https://www.instagram.com/p/Cgq68EuB-nW/','https://www.instagram.com/p/Cgq627whM-C/','https://www.instagram.com/p/Cgq6k_Zhopv/','https://www.instagram.com/p/Cgq6UjKBGVK/','https://www.instagram.com/p/CgoydwVBHqc/','https://www.instagram.com/p/Cgmud-Phxs8/','https://www.instagram.com/p/CgmKLKfhIcj/','https://www.instagram.com/p/CglSH-zvw6W/','https://www.instagram.com/p/Cgj2i2ZhVrr/','https://www.instagram.com/p/CggKXcGv6f2/','https://www.instagram.com/p/Cgdlq-Nvivs/','https://www.instagram.com/p/CgZ84gjPwUs/','https://www.instagram.com/p/CgZPdWhjvkC/']
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

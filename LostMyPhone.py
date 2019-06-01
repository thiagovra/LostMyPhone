#   PROJECT NAME: LostMyPhone
#    Thiago Varella Rahmi
#    Start date: 27/05/2019
#    Last Change: 01/06/2019
#    Version: 0.1.0
#    PATCH NOTES:fixed
#        -
#    Stopped in:
#    Line:
#    Solve:
#    Add:

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Thiag\Documents\codes\pycodes\chromedriver")
# Chromedriver.exe address

options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(chrome_options=options)
# New option so i don't need to scan the QR code every time i run the code(remember me auth)

driver.get('https://web.whatsapp.com/')
# Open's Chrome at the url above

xtimes = 3
# how many times the loop to run
time.sleep(10)
# time that takes WhatsApp to load +-10seconds(depends on internet connection)

for i in range(xtimes):
    # Loop start
    name = "myoi"
    # The name of the contact you want to send a msg
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_13mgZ')
    msg = "unmute"
    # The message that you want to send
    count = 2
    # The amount of times you want to send your message
    for i in range(count):
        msg_box.send_keys(msg)
        # Message written
        time.sleep(0.4)
        # Waiting for the button to appear
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
        # Message sent
    # Loop end
time.sleep(1)
# 1s of downtime just in case
driver.close()
# Close Chrome window

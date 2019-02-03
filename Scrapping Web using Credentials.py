from selenium import webdriver
from bs4 import BeautifulSoup

Email = "@username"
Password = "@password"

Driver  = webdriver.Chrome(executable_path = r"C:\Chromedriver_win32\chromedriver.exe")
Driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")

username_field = Driver.find_element_by_id("email")
password_field = Driver.find_element_by_id("password")
# login_button = Driver.find_element_by_id("submit-button")

username_field.send_keys(Email)
password_field.send_keys(Password)
login_button = Driver.find_element_by_id("submit-button")
# login_button.click()
login_button.submit()
Driver.get("https://stackoverflow.com/questions/50799375/addition-function-in-python-is-not-working-as-expected/50799757#50799757")
DB = Driver.page_source

soup = BeautifulSoup(DB, 'lxml')
div = soup.find('div', class_= "inner-content clearfix")

for i in div.find_all('div', class_= "post-text"):
    print(i.text)

Driver.close()




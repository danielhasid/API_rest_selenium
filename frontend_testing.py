from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

user_id = input("Type user ID to locate the User name :")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service("c://DevOps/Python/webDriver/chromedriver"),options=options)
driver.get(f"http:127.0.0.1:5000/users/{user_id}")
driver.implicitly_wait(10)
user_name = driver.find_element(By.ID,user_id)
print(user_name.text)






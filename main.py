from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import tomli

with open("config.toml", mode="rb") as fp:
    config = tomli.load(fp)

def element_exists(webdriver, xpath):
    try:
        elem = webdriver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return elem

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
driver.get("https://seusucesso.ahgora.com.br/")
elem = driver.find_element(By.NAME, "UserName")
elem.send_keys(config["login"]["username"])
time.sleep(2)
elem = driver.find_element(By.NAME, "Password")
elem.send_keys(config["login"]["password"])
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
if element_exists(driver, "//*[@id='page-footer']/div/div/div[2]/div/button[2]"):
    elem = driver.find_element(By.XPATH, "//*[@id='page-footer']/div/div/div[2]/div/button[2]")
    elem.click()
    time.sleep(2)
driver.get("https://seusucesso.ahgora.com.br/ChatbotEditor")
time.sleep(2)

if element_exists(driver, config["xpath"]["editbot"]):
    elem = driver.find_element(By.XPATH, config["xpath"]["editbot"])
else:
    elem = driver.find_element(By.XPATH, config["xpath"]["viewbot"])

elem.click()
time.sleep(2)
elem = driver.find_element(By.XPATH, "//*/div/div/div/div[2]/div/div[2]/button")
elem.click()
time.sleep(2)
if element_exists(driver, "/html/body/div[8]/div[3]/div/div[3]/button[2]"):
    print("chegou")
time.sleep(2)

driver.close()


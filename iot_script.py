from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
actions = ActionChains(driver)
username = ""
password = ""

driver.get("https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=9214")
original_window = driver.current_window_handle

def login():
    WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    user_field = driver.find_element(By.ID, "username")
    pass_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginbtn")

    user_field.send_keys(username)
    pass_field.send_keys(password)
    login_button.click()

def class_join():
    
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "join_button_input"))
    )
    join_button = driver.find_element(By.ID,"join_button_input")
    join_button.click()

    driver.switch_to.window(driver.window_handles[-1])
    actions.send_keys(Keys.ESCAPE)

    WebDriverWait(driver,60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "audioBtn--1H6rCK"))
    )

    audio_button = driver.find_elements(By.CLASS_NAME, "audioBtn--1H6rCK")[1]
    audio_button.click()

def send_message():

    text_area = driver.find_element(By.CLASS_NAME, "input--2wilPX")
    enter_btn = driver.find_element(By.CLASS_NAME, "sendButton--Z93EzE")
    text_area.send_keys("114 present sir")
    enter_btn.click()

login()
class_join()
time.sleep(1800)
send_message()
time.sleep(1200)
driver.quit()


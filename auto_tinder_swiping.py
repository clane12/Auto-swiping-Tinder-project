import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")
url = "https://tinder.com/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url=url)


time.sleep(2)

cookies = driver.find_element(By.XPATH, '//*[@id="o-1274314283"]/div/div[2]/div/div/div[1]/div[2]/button')
cookies.click()

log_in = driver.find_element(By.XPATH, '//*[@id="o-1274314283"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()
time.sleep(2)
facebook = driver.find_element(By.XPATH, '//*[@id="o-1052973847"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook.click()

"""after this there is a new window pop up to log in to facebook, as our main window is on tinder we can't just access
 the facebook log in window, but there is a way we can through selenium driver.window_handles[0] will be the base and [1], [2] will
  be the once that comes after.
 1. main_window = driver.window_handles[0]
 2. fb_login_window = driver.window_handles[1]
 3. driver.switch_to.window(fb_login_window)
 you can use
 4. driver.switch_to.window(main_window) to get back to the main window.
 """

main_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.title)

fb_email = driver.find_element(By.ID, "email")
fb_email.send_keys(email)

fb_pass = driver.find_element(By.ID, "pass")
fb_pass.send_keys(password)
fb_pass.send_keys(Keys.ENTER)
time.sleep(5)
# fb_continue = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div/div')
# fb_continue.click()
driver.close()

driver.switch_to.window(main_window)
time.sleep(2)

location_allow = driver.find_element(By.XPATH, '//*[@id="o-1052973847"]/div/div/div/div/div[3]/button[1]')
location_allow.click()

notify_me = driver.find_element(By.XPATH, '//*[@id="o-1052973847"]/div/div/div/div/div[3]/button[2]')
notify_me.click()

time.sleep(2)

btn = driver.find_elements(By.CSS_SELECTOR, '.button')
dislike = btn[1]
like = btn[3]

for i in range(10):
    time.sleep(2)
    try:
        dislike.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(1)
            continue



# driver.quit()
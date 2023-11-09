from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time





driver = webdriver.Chrome()  # Webdriver-manager will handle path, if not installed specify path of webdriver

driver.get('https://front-stage.cashortrade.org/');     #opens webpage

time.sleep(10) 

login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[1]/div[2]/div/div[3]/div/button[2]/div/div/p') #xpath to the 'Log in' top right of homepage
login_btn.click()

time.sleep(5)

phone_input = driver.find_element(By.ID, 'sign-up-phone-number-tel-input')  #phone number input
phone_input.send_keys("8888888888")

time.sleep(5)

phone_next = driver.find_element(By.ID, 'sign-up-phone-number-next-btn') #phone next button
phone_next.click()

time.sleep(5) 

auth2 = driver.find_element(By.ID, 'input-element')     #inputs 2auth code
auth2.send_keys('000000')

time.sleep(5)

sellbtn = driver.find_element(By.ID, 'sell-tickets-header-btn')  #sell tickets button top right
sellbtn.click()

time.sleep(5)

eventbtn = driver.find_element(By.XPATH, '//*[@id="ticket-wallet-wrapper"]/div/div[2]/div[2]/div[1]/button/h3')    #navigates to the 'U2 Cover Band', need to randomize if time permits
eventbtn.click()

time.sleep(5)

venuebtn = driver.find_element(By.XPATH, '//*[@id="ticket-wallet-wrapper"]/div/div[2]/div[2]/button/div/div/div') #selects the winery venue
venuebtn.click()

time.sleep(5)

smtbtn = driver.find_element(By.XPATH, "//div[@id='ticket-wallet-wrapper']/div/div[3]/div[2]/div/button/div[2]") #sell my tickets button
smtbtn.click()

time.sleep(5)

xferbtn = driver.find_element(By.XPATH, "xpath=//div[@id='ticket-wallet-wrapper']/div/div[3]/div[2]/div/div/button/div[2]")
xferbtn.click()

time.sleep(5)

xfer_next = driver.find_element(By.ID, "create-listing-next-btn")
xfer_next.click()


driver.quit()

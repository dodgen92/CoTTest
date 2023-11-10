from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager




print ("Choose Browser Test")
print ("1. Firefox")
print ("2. Chrome")
print ("3. Edge")
operation = input()

if operation == "1":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

if operation == "2":
    driver = webdriver.Chrome() 
    
if operation =="3":
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))




driver.get("https://www.google.com/")  

logging.info("Navigating to the website")
driver.get('https://front-stage.cashortrade.org/');     #opens webpage
logging.info("Opened the website")

driver.maximize_window()                          #maximize window


try:

    login_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/div[1]/div[2]/div/div[3]/div/button[2]/div/div/p')))
    login_btn.click()

    phone_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sign-up-phone-number-tel-input')))
    phone_input.send_keys("8888888888")

    phone_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'sign-up-phone-number-next-btn')))
    phone_next.click()

    auth2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'input-element')))
    auth2.send_keys('000000')

    sellbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'sell-tickets-header-btn')))
    sellbtn.click()

    eventbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ticket-wallet-wrapper"]/div/div[2]/div[2]/div[1]/button/h3')))
    eventbtn.click()
       
    venuebtn =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ticket-wallet-wrapper"]/div/div[2]/div[2]/button/div/div/div'))) #selects the winery venue
    venuebtn.click()
        
    smtbtn =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='ticket-wallet-wrapper']/div/div[3]/div[2]/div/button/div[2]"))) #sell my tickets button
    smtbtn.click()

    xferbtn =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/button[1]/div[2]"))) # Transfer ready selection
    xferbtn.click()
     
    xfer_next =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-next-btn")))                                   # Next button on page 2
    xfer_next.click()      

    txquantity =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/button/div[1]")))       #ticket quantity selection field
    txquantity.click()       

    quantselect =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ticket-wallet-wrapper"]/div/div[3]/div[2]/div/div/div[2]/div/div/div/button[1]')))       # selects ticket quantity from dropdown
    quantselect.click()    

    xferrdy =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[3]/div/button[1]/div")))       
    xferrdy.click()    

    ogpurchase =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[4]/div/div/button/div[1]")))
    ogpurchase.click()    

    ogpurchaseselect =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[4]/div/div/div/button[1]")))
    ogpurchaseselect.click()    

    genadmission =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[5]/div/div/button[1]/div")))
    genadmission.click()    

    tixlocation =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[5]/div/div[2]/div[2]/div/div/div/button")))
    #tixlocation.click()
    tixnextbtn = driver.find_element(By.ID, "create-listing-next-btn")                 #finds next button
    driver.execute_script("arguments[0].scrollIntoView();", tixnextbtn)               #scrolls down until next btn is in view

    tixlocation.click()
    
    tixlocationselect =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/button[1]")))
    tixlocationselect.click()
       
    #tixnextbtn = driver.find_element(By.ID, "create-listing-next-btn")
    tixnextbtn.click()      

    tixprice = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-price-per-number-input")))
    tixprice.send_keys("12")

    valueradiobtn = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div[3]/label[1]/div/div")
    valueradiobtn.click()
    
    pricenxtbtn =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-next-btn")))
    pricenxtbtn.click()

    time.sleep(2)

    fundsnxtbtn =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-next-btn")))
    fundsnxtbtn.click()

    time.sleep(2)

    textfield = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div/div[1]/textarea")))
    textfield.send_keys("TEST")
          
    fundsnxtbtn.click()

    time.sleep(2)
      
    posttixbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-post-tickets-btn")))
    driver.execute_script("arguments[0].scrollIntoView();", tixnextbtn)  
    posttixbtn.click()

    time.sleep(4)

    print("Test Case passed")


finally:
    driver.quit()

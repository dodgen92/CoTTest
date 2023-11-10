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




print ("Choose Browser Test")                                                                 #allows the tester to select which browser to run the test case in
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

    login_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/div[1]/div[2]/div/div[3]/div/button[2]/div/div/p')))      #identifies and clicks the "Log In" button in top right of home page
    login_btn.click()

    phone_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sign-up-phone-number-tel-input')))          #inputs the phone into appropriate field
    phone_input.send_keys("8888888888")

    phone_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'sign-up-phone-number-next-btn')))                #clicks next btn
    phone_next.click()

    auth2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'input-element')))                                 #inputs auth code into apporpriate field (Next button is auto generate so no need to click here)
    auth2.send_keys('000000')

    sellbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'sell-tickets-header-btn')))                         #clicks sell tickets button
    sellbtn.click()

    eventbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ticket-wallet-wrapper"]/div/div[2]/div[2]/div[1]/button/h3')))    #selects first event
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

    xferrdy =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[3]/div/button[1]/div")))       # selects the transfer ready button
    xferrdy.click()    

    ogpurchase =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[4]/div/div/button/div[1]"))) #clicks the original purchasing platform field
    ogpurchase.click()    

    ogpurchaseselect =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[4]/div/div/div/button[1]")))     #selects the original purchase site from dropdown 
    ogpurchaseselect.click()    

    genadmission =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[5]/div/div/button[1]/div")))          #clicks general admission
    genadmission.click()    

    tixlocation =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[5]/div/div[2]/div[2]/div/div/div/button")))     #selects the ticket location dropdown
    #tixlocation.click()
    tixnextbtn = driver.find_element(By.ID, "create-listing-next-btn")                 #finds next button
    driver.execute_script("arguments[0].scrollIntoView();", tixnextbtn)               #scrolls down until next btn is in view, script was failing to grab the dropdown menu until scrolling

    tixlocation.click()
    
    tixlocationselect =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/button[1]"))) #selects balcony from dropdown
    tixlocationselect.click()
       
    #tixnextbtn = driver.find_element(By.ID, "create-listing-next-btn")
    tixnextbtn.click()       #clicks next button to continue to page 3

    tixprice = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-price-per-number-input")))        #clicks the ticket price input field and inputs a value of 12 dollars
    tixprice.send_keys("12")

    valueradiobtn = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div/div[3]/label[1]/div/div")   #selects the face value radio button 
    valueradiobtn.click()
    
    pricenxtbtn =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-next-btn")))     #next button to page 4
    pricenxtbtn.click()

    time.sleep(2)           # used sleeps here because waits were confused by ID being named the same for both next buttons, causing a failure

    fundsnxtbtn =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-next-btn")))      #clicks next button
    fundsnxtbtn.click()

    time.sleep(2)          #sleep used here for the same reason

    textfield = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div/div[1]/textarea")))  #inputs "TEST" into the text field
    textfield.send_keys("TEST")
          
    fundsnxtbtn.click() #clicks next btn    

    time.sleep(2)    #sleep for the same reason
      
    posttixbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-listing-post-tickets-btn")))    #finds the "Post Tickets" Button
    driver.execute_script("arguments[0].scrollIntoView();", tixnextbtn)                                                    #scrolls down until "Post Tickets" is visible, test was failing on Firefox until implemented  
    posttixbtn.click()              #clicks post tix btn

    time.sleep(4)

    print("Test Case passed")      #Returns passed if all operations were successful


finally:
    driver.quit()


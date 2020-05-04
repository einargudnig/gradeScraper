from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome(executable_path="C:\\Users\\Einar\\Desktop\\pythonScraper\\chromedriver.exe")

driver.get('https://ugla.hi.is/vk/namskeidin_min.php?sid=40')



# Click the button to login
driver.find_element_by_id("officeLogin").click()


# find a element we can put user info into.
# wait because it is AJAx call.
try: 
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "loginfmt"))
    
)
finally:

    # send user info to seleceted user login input
    time.sleep(1)
    elementInput = driver.find_element_by_name("loginfmt")
    elementInput.send_keys("egg18@hi.is")
    
    # Press next to proceed with login
    elementBTN = driver.find_element_by_id("idSIButton9")
    time.sleep(1)
    elementBTN.click()

    #locate password input
    time.sleep(1)
    elementPw = driver.find_element_by_id("i0118")

    #Input password value
    elementPw.send_keys("FF8EVm86")

    # the button has the same ID, so it is "not loaded" to the DOM therefore we wait for two seconds for it to load.
    time.sleep(2)
    # Press finish to proceed with login, note the same button as before!?
    elementPWbttn = driver.find_element_by_id("idSIButton9")
    elementPWbttn.click()

    # again, have to wait for two seconds for the button to re-appear.
    time.sleep(2)

    # find and press the las confirm button.
    elementYBTN = driver.find_element_by_id("idSIButton9")
    elementYBTN.click()

    #(driver.page_source).encode("utf-8")

    # downloads the HTML file of the page.
    with open("C:\\Users\\Einar\\Desktop\\pythonScraper\\uglaHTML.html", "w") as f:
        f.write(driver.page_source)

    #html_source = driver.page_source
    #print(html_source)    
    time.sleep(2)
    
    driver.quit() # Calls driver.dispose method. closes all browsers windows and ends the webdriver session
###############################################################################################




#with requests.Session() as s:
#    url = "https://ugla.hi.is/"
#    r = s.get(url)
#    print(r.content)
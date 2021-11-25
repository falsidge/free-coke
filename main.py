from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#login
promo = "https://us.coca-cola.com/amoe?promotionId=8417_amc_iw_63987"
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10000)
driver.get(promo)

wait.until(lambda driver: driver.current_url == promo)
el = wait.until(lambda driver:driver.find_element (By.CLASS_NAME, "tcccLogin_capture_signin_red_link"))
link = wait.until(lambda driver:el.get_attribute("href"))

print(link)
driver.execute_script ("location.replace('"+link+"')")

#uncomment if really needed for some reason. you can manually enter your username and password
# user = ""
# password = ""
# el = wait.until(lambda driver:driver.find_element(By.ID, "signInName"))
# el.send_keys(user); 

# el = wait.until(lambda driver:driver.find_element(By.ID, "password"))
# el.send_keys(password)

# el = wait.until(lambda driver:driver.find_element(By.ID, "next"))
# wait.until(lambda driver:EC.visibility_of(el))
# el.click()
#Promo page
while True:
    wait.until(lambda driver: driver.current_url == promo)
    el = wait.until(lambda driver:driver.find_element(By.CLASS_NAME, "amoe__myentry-button"))
    wait.until(lambda driver:EC.visibility_of(el))
    el.click()

    el = wait.until(lambda driver:driver.find_element(By.CLASS_NAME, "details-screen"))
    el = wait.until(lambda driver:el.find_element(By.CLASS_NAME, "btn"))
    wait.until(lambda driver:EC.visibility_of(el))
    el.click()

    print("success")

    el = wait.until(lambda driver:driver.find_element(By.CLASS_NAME, "thankyou-screen"))
    wait.until(lambda driver:EC.visibility_of(el))
    driver.get(promo)
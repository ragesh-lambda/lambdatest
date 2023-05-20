import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

username ="ritamg@lambdatest.com"
accessToken ="e4vXxk64hYOIkG7gwld5Fsb5LpmhI8wq6J0LQ2KC9LSgJHc1N5"
passs="Shiva@12"
gridUrl = "hub.lambdatest.com/wd/hub"

url = "https://"+username+":"+accessToken+"@"+gridUrl

capability_1= {
    "browserName": "Chrome",
    "browserVersion": "110.0",
    "resolution":"1024x768",
    "platform":"Win10",
    "platformName":"Win10",
    "LT:Options": {
        "platformName": "Windows 11",
        "project": "Untitled_1",
        "resolution":"1024x768",
        "platform":"Win10",
        "platformName":"Win10",
    }
}

driver_1 = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capability_1
)
driver_1.maximize_window()
driver_1.get("http://whatismyscreenresolution.net/")
time.sleep(10)
driver_1.get("https://uat-dv.docveda.in/")
driver_1.find_element("xpath", "//button[contains(text(), 'Log In')]").click()
driver_1.find_element("id","outlined-basic").send_keys("SRP1")
driver_1.find_element("name","userName").send_keys("SRP123")
driver_1.find_element("name","password").send_keys("Admin@12345")
# driver_1.find_element("type","checkbox").click()
driver_1.find_element("xpath","/html/body/div[3]/div[3]/div/div[2]/div/div[2]/div/div/form/div[5]/button").click()
time.sleep(8)
driver_1.find_element("xpath","/html/body/div[1]/div/div[5]/div[3]/div/div[3]/div/div[2]/div/div/div[3]/div[1]/div[1]").click()

# driver_1.find_element("id","email").send_keys(username)
# driver_1.find_element("id","password").send_keys(passs)
#driver.find_element("id","login-button").click()
# elem = driver_1.find_element("id","btnHover")
# elem.send_keys("https://accounts.lambdatest.com/login")
# elem.submit()
# driver_1.find_element("id","login-button").click()
print("Printing title of current page :"+driver_1.title)
driver_1.execute_script("lambda-status=passed")
print("Requesting to mark test : pass")
driver_1.quit()


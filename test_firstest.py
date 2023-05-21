# google-search-lambdatest.py

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os


"""
    LambdaTest selenium automation sample example
    Configuration
    ----------
    username: Username can be found at automation dashboard
    accessToken:  AccessToken can be genarated from automation dashboard or profile section

    Result
    -------
    Execute Test on lambdatest Distributed Grid perform selenium automation based 
"""
# username: Username can be found at automation dashboard
username ="ritamg@lambdatest.com"
# accessToken:  AccessToken can be genarated from automation dashboard or profile section
accessToken ="e4vXxk64hYOIkG7gwld5Fsb5LpmhI8wq6J0LQ2KC9LSgJHc1N5"
# gridUrl: gridUrl can be found at automation dashboard
gridUrl = "hub.lambdatest.com/wd/hub"
passs="Shiva@12"


capabilities = {
    'browserName': 'firefox',
    'browserVersion': 'latest',
    'platformName': 'Windows 10',
    'moz:firefoxOptions': {
        'args': [],
        'prefs': {}
    },
    'LT:Options': {
        'visual': True,
        'video': True,
        'project': 'Untitled',
        'w3c': True,
        'plugin': 'python-python',
        "console":"warn",
        "smartUI.project":"Ritam Projects",
        "headless":True,
        "seCdp":True
    }
}

url = "https://"+username+":"+accessToken+"@"+gridUrl

# username: Username can be found at automation dashboard
# username = os.getenv("LT_USERNAME")
# accessToken:  AccessToken can be genarated from automation dashboard or profile section
# accessToken = os.getenv("LT_ACCESS_KEY")
# gridUrl: gridUrl can be found at automation dashboard
# gridUrl = "hub.lambdatest.com/wd/hub"
# passs="Shiva@12"

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"


# capabilities = {
#     'browserName': 'firefox',
#     'browserVersion': 'latest',
#     'platformName': 'Windows 10',
#     'moz:firefoxOptions': {
#         'args': [],
#         'prefs': {}
#     },
#     'LT:Options': {
#         'username': 'ritamg',
#         'accessKey': 'e4vXxk64hYOIkG7gwld5Fsb5LpmhI8wq6J0LQ2KC9LSgJHc1N5',
#         'visual': True,
#         'video': True,
#         'project': 'Untitled',
#         'w3c': True,
#         'plugin': 'python-python'
#     }
# }

#url = "https://"+username+":"+accessToken+"@"+gridUrl


"""
    ----------
    platformName : Supported platfrom - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
    browserName : Supported platfrom - (chrome, firefox, Internet Explorer, MicrosoftEdge)
    browserVersion :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/

    Result
    -------
"""

driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capabilities

)

"""
    ----------
    Execute test:  navigate google.com search LambdaTest
    Result
    ----------
    print title
"""

driver.get("https://accounts.lambdatest.com/login")
driver.find_element("id","email").send_keys(username)
driver.find_element("id","password").send_keys(passs)
#driver.find_element("id","login-button").click()
elem = driver.find_element("id","email")
elem.send_keys("https://accounts.lambdatest.com/login")
elem.submit()
driver.find_element("id","login-button").click()

print("Printing title of current page :"+driver.title)
driver.execute_script("lambda-status=passed")
print("Requesting to mark test : pass")

"""
    Quit selenium driver
"""
driver.quit()
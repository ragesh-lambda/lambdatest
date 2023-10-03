import os
import unittest
import sys
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
username = "rageshn"
access_key = "902OMaGaDsNUiTYVS73bU3I8X8Wld6D014LSeUog83xx6bF386"


class FirstSampleTest(unittest.TestCase):

    # Function to get a random User-Agent (you can use a library for this purpose)
    def get_random_user_agent(self):
        user_agents = [
            # Chrome on Windows
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            # Firefox on Windows
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            # Safari on macOS
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
            # Edge on Windows
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.38",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84",
            # Firefox on macOS
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
        ]
        return random.choice(user_agents)

    # setUp runs before each test case
    def setUp(self):
        lt_options = {
            "user": username,
            "accessKey": access_key,
            "build":os.getenv("LT_BUILD_NAME"),
            "name": "UnitTest-Selenium-Test",
            "platformName": "Windows 11",
            "w3c": True,
            "browserName": "Chrome",
            "browserVersion": "latest",
            "selenium_version": "4.8.0",
            "tunnel":False
        }
        
        browser_options = ChromeOptions()
        browser_options.set_capability('LT:Options', lt_options)
        
        # Add the following lines to open Chrome in incognito mode and set a random User-Agent
        browser_options.add_argument("--incognito")
        user_agent = self.get_random_user_agent()
        browser_options.add_argument(f"user-agent={user_agent}")

        # Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
        # Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
        # Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
        # Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot 
        # Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/

        self.driver = webdriver.Remote(
            command_executor="http://hub.lambdatest.com:80/wd/hub",
            options=browser_options)

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        driver = self.driver

        # Url
        driver.get("https://in.linkedin.com/?original_referer=https%3A%2F%2Fwww.google.com%2F")
        driver.refresh()
        time.sleep(10)

        # Click on check box
        email = driver.find_element(By.ID, "session_key")
        email.click()
        email_1= driver.find_element(By.ID, "session_key")
        email_1.send_keys("rageshn@lambdatest.com")
        time.sleep(10)
        password= driver.find_element(By.ID, "session_password")
        password.click()
        email_1= driver.find_element(By.ID, "session_password")
        email_1.send_keys("*****")
        time.sleep(10)
        finally_click= driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button")
        finally_click.click()

        # Click on check box
        # check_box_two = driver.find_element(By.ID, "session_password")
        # check_box_two.send_keys("Shiva@12")

        # Enter item in textfield
        # textfield = driver.find_element(By.ID, "sampletodotext")
        # textfield.send_keys("Yey, Let's add it to list")

        # Click on add button
        # add_button = driver.find_element(By.ID, "addbutton")
        # add_button.click()

        # Wait for the added item to appear
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='done-false']")))

        # # Get the added item
        # added_item = driver.find_element(By.XPATH, "//span[@class='done-false']").text
        # print(added_item)


if __name__ == "__main__":
    unittest.main()

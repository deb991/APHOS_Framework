#!/usr/bin/env python
import os
import sys
import subprocess
import time
import math
import random
import threading
from threading import *
import selenium
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#defining Chrome WebDriver
chromeDriver = 'dep_pkgs/chromedriver.exe'

class order():
    def __init__(self):
        print('Initializing constructor for the master program ')


    #def task(self, Task):
        #return self.Task


    def task_search_content(self):
        search_keyword = input('Please enter your search Keyword :: ')
        driver = chromeDriver
        driver.get('www.google.com')
        input_element = driver.find_element_by_name("q")
        input_element = driver.fin
        input_element.send_keys(search_keyword)
        input_element.submit()

        RESULTS_LOCATOR = "//div/h3/a"

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

        page1_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)

        for item in page1_results:
            print(item.text)


        #driver.quit()


if __name__ == '__main__':
    order().task_search_content()

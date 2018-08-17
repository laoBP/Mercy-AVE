# -*- coding: utf-8 -*-
"""
Created on Auh 13 10:41:43 2018

@author: Lin Ao
"""

# -*- coding: utf-8 -*-

'''
Useful methods:

driver.get(url_string)
driver.find_element_by_id(id_string)
driver.find_element_by_css_selector(css_string)

element.send_keys(string)
element.click()

time.sleep(seconds_int)

'''

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import pandas as pd


class Exportor:
    def __init__(self):
        self.base_url = r'https://ncr.energyscorecards.com/auditReport/show/'
        self.down_load_dir = r'C:\Users\lao\Documents\MercyACE'
        self.web_driver = webdriver.Chrome(r'/Users/lao/Documents/repos/chromedriver.exe')
        self.username = 'linao'
        self.password = 'AL1227680al'

    def download_by_id(self, export_id):
        # config download
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': self.down_load_dir}
        options.add_experimental_option('prefs', prefs)

        url = self.base_url + export_id
        print
        url
        self.web_driver.get(url)

        try:
            user_field = self.web_driver.find_element_by_id('username')
            pw_field = self.web_driver.find_element_by_id('password')
            login_button = self.web_driver.find_element_by_id('loginButton')

            user_field.send_keys(self.username)
            pw_field.send_keys(self.password)
            login_button.click()
        except:
            pass

        self.web_driver.find_element_by_id('exportToCSV').click()

    def quit_chrome_session(self):
        # excessive delay before quit to finish any click/save actions
        time.sleep(3)
        self.web_driver.quit()


if __name__ == '__main__':
    esc = Exportor()
    event_id_list = ['37391','37395']
    for id in event_id_list:
        esc.download_by_id(id)
    esc.quit_chrome_session()

import zipfile,fnmatch,os
rootPath = r'C:\Users\lao\Downloads'
test =  r'C:\Users\lao\Documents\MercyACE'
pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
        zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(test, os.path.splitext(filename)[0]))

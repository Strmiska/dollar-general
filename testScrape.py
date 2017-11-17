from selenium import webdriver

import requests
from bs4 import BeautifulSoup
import pandas as pd


PHANTOMJS_PATH = './phantomjs'


browser = webdriver.PhantomJS(PHANTOMJS_PATH)
browser.get('https://www.dollargeneral.com/')

soup = BeautifulSoup(browser.page_source, "html.parser")

stuff = soup.find_all('li')

print(stuff[0].prettify())

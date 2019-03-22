from django.test import TestCase
from django.test import Client
from selenium import webdriver
import time
import requests

chrome = webdriver.Chrome()
url = 'http://127.0.0.1:8000/'
chrome.get(url)
response = requests.get(url)
if response.status_code == 200:
    print('index website request successful!')
time.sleep(2)
chrome.find_element_by_xpath('//header[@class="overlay"]/a').click()
print('click investart successful!!!')

time.sleep(2)
chrome.find_element_by_xpath('//div[@align="center"]/a[1]').click()
print('Developer Login click successful!!!')
time.sleep(2)
chrome.close()

chrome = webdriver.Chrome()
chrome.get(url)
chrome.find_element_by_xpath('//div[@align="center"]/a[2]').click()
print('Investor Login click successful!!!')
time.sleep(2)

chrome.find_element_by_xpath('//footer[@class="overlay"]/a[1]').click()
print('click About Us successful！')
time.sleep(2)

chrome.find_element_by_xpath('//footer[@class="overlay"]/a[2]').click()
print('click Contact Us successful！')
time.sleep(2)
chrome.close()

url1 = 'http://127.0.0.1:8000/investart/about/'
response = requests.get(url1)
if response.status_code == 200:
    print('request about successful!')
time.sleep(2)

chrome = webdriver.Chrome()
chrome.get(url1)
chrome.find_element_by_xpath('//header[@class="overlay"]/a').click()
print('click investart successful!')
time.sleep(2)

chrome.find_element_by_xpath('//footer[@class="overlay"]/a[1]').click()
print('click About Us successful！')
time.sleep(2)

chrome.find_element_by_xpath('//footer[@class="overlay"]/a[2]').click()
print('click Contact Us successful！')
time.sleep(2)
chrome.close()

url2 = 'http://127.0.0.1:8000/investart/contact/'
response = requests.get(url2)
if response.status_code == 200:
    print('request contact successful!')
time.sleep(2)

chrome = webdriver.Chrome()
chrome.get(url2)
input = chrome.find_element_by_xpath('//input[@id="id_name"]')
input.send_keys('aaa')
time.sleep(1)

input1 = chrome.find_element_by_xpath('//input[@id="id_email"]')
input1.send_keys('123456@qq.com')
time.sleep(1)

input2 = chrome.find_element_by_xpath('//textarea[@id="id_concern"]')
input2.send_keys('dsfhidshfdoisncoidnvoidsncosdiocniodsncodsnckfndvinsdcnkdnvdfibvjncvsdncnsdifhuiesndcodsnvibdfindsocnidsvuisdoci')
time.sleep(1)

chrome.find_element_by_xpath('//input[@name="submit"]').click()
print('Test contact successful!!!')
chrome.close()
time.sleep(2)

url3 = 'http://127.0.0.1:8000/investart/?next=/investart/account/'
response = requests.get(url3)
if response.status_code == 200:
    print('request account successful!!!')
time.sleep(2)

chrome = webdriver.Chrome()
chrome.get(url3)
time.sleep(2)

chrome.find_element_by_xpath('//header[@class="overlay"]/a').click()
print('click investart successful!!!')
time.sleep(2)

chrome.find_element_by_xpath('//div[@align="center"]/a[1]').click()
print('Developer Login click successful!!!')
time.sleep(2)
chrome.close()

chrome = webdriver.Chrome()
chrome.get(url3)
chrome.find_element_by_xpath('//div[@align="center"]/a[2]').click()
print('Investor Login click successful!!!')
time.sleep(2)

chrome.find_element_by_xpath('//footer[@class="overlay"]/a[1]').click()
print('click About Us successful！')
time.sleep(2)

chrome.find_element_by_xpath('//footer[@class="overlay"]/a[2]').click()
print('click Contact Us successful！')
time.sleep(2)
chrome.close()

url4 = 'http://127.0.0.1:8000/investart/dev_login/'
response = requests.get(url4)
if response.status_code == 200:
    print('request dev_login successful!!!')
time.sleep(2)

chrome = webdriver.Chrome()
chrome.get(url4)
chrome.find_element_by_xpath('//header[@class="overlay"]/a').click()
print('click investart successful!!!')
time.sleep(2)
chrome.close()

chrome = webdriver.Chrome()
chrome.get(url4)
username = chrome.find_element_by_xpath('//input[@name="username"]')
username.send_keys('bbb')
time.sleep(1)

pwd = chrome.find_element_by_xpath('//input[@name="password"]')
pwd.send_keys('123456')
time.sleep(1)
chrome.find_element_by_xpath('//input[@type="submit"]').click()
print('Test dev_login successful!!!')

url5 = 'http://127.0.0.1:8000/investart/dev_signup/'
response = requests.get(url5)
if response.status_code == 200:
    print('request dev_signup successful!!!')
time.sleep(2)

chrome = webdriver.Chrome()
chrome.get(url5)
input = chrome.find_element_by_xpath('//input[@id="id_email"]')
input.send_keys('123456@qq.com')
time.sleep(1)

input1 = chrome.find_element_by_xpath('//input[@id="id_username"]')
input1.send_keys('bbb')
time.sleep(1)

input2 = chrome.find_element_by_xpath('//input[@id="id_password"]')
input2.send_keys('123456')
time.sleep(1)

# chrome.find_element_by_xpath('//input[@type="submit"]').click()
# time.sleep(1)
print('Test dev_signup successful!!!')
chrome.close()

url6 = 'http://127.0.0.1:8000/investart/?next=/investart/add_project/'
response = requests.get(url6)
if response.status_code == 200:
    print('request add_project successful!!!')
time.sleep(2)

url7 = 'http://127.0.0.1:8000/investart/?next=/investart/project/2/'
response = requests.get(url7)
if response.status_code == 200:
    print('request project successful!!!')
time.sleep(2)
print('Test project successful!!!')



url8 = 'http://127.0.0.1:8000/investart/password_reset/'
response = requests.get(url8)
if response.status_code == 200:
    print('request password_reset successful!!!')
time.sleep(2)

chrome = webdriver.Chrome()
chrome.get(url8)
input = chrome.find_element_by_xpath('//input[@name="email"]')
input.send_keys('123456@qq.com')
chrome.find_element_by_xpath('//input[@value="Reset my password"]').click()
print('Test password_reset successful!!!')






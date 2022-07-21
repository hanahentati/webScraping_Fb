import re
import argparse
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse
from bs4 import BeautifulSoup as bs
# chromedriver_autoinstaller.install()
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
#change the paths
path = 'C:/Users/GMI/chromedriver.exe'
# driver = webdriver.Chrome(path)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
query = 'kpop'
urlq = urllib.parse.quote_plus(query)
url= "https://www.facebook.com/search/posts?q="+urlq
print(url)
driver.get(url)

#get the text within the post
# div_text = driver.find_element(By.CSS_SELECTOR, '[data-ad-comet-preview]')
# text = div_text.get_attribute('textContent')
# print(text)

#get comment
# elements = driver.find_element(By.CSS_SELECTOR, "span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j")
# text = elements.get_attribute('textContent')
# print(text)

# txt=driver.find_elements(By.XPATH,"//div[contains(@class,'_5pbx userContent')]")
# postComments = driver.findAll("div", {"class": "_4eek"})
# print(postComments)
# for x in txt:
#     a = x.find_elements("xpath",".//a[@class='_6qw4']")
#     print ("who made the comment?  - ", a[0].get_attribute("href"))
#     print ("what's in the comment? - ", x.text)

# elements = driver.find_element(By.TAG_NAME, 'ul')
# com_elements = elements.find_element(By.TAG_NAME, 'li')
# for element in com_elements:
#     link = element.find_element(By.CSS_SELECTOR, 'div.ecm0bbzt.e5nlhep0.a8c37x1j')
# ni8dbmo4 stjgntxs l9j0dhe7
# class="l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 dati1w0a j83agx80 btwxx1t3 lzcic4wl"
elements = driver.find_element(By.TAG_NAME, 'ul')
print(elements)
com_elements = elements.find_element(By.TAG_NAME, 'li')
print(com_elements)

# link = com_elements.find_element(By.CSS_SELECTOR, 'div.ecm0bbzt.e5nlhep0.a8c37x1j')
#
#
# text = link.get_attribute('textContent')
# print(text)


# get the number of comment in a page
# elements = driver.find_elements(By.CSS_SELECTOR, "div.gtad4xkn ")
# comments = "0"
# for element in elements:
#     text = element.get_attribute("textContent")
#
#     if "commentaires" in text:
#         comments = int(re.findall("\d+", text)[0])
# print(comments)
# # get the number of partage in a page
# elements = driver.find_elements(By.CSS_SELECTOR, "div.gtad4xkn ")
# shares = "0"
# for element in elements:
#     text = element.get_attribute("textContent")
#
#     if "partages" in text:
#         shares = int(re.findall("\d+", text)[0])
# print(shares)
# # get number of reaction
# total_reactions = driver.find_element(By.CSS_SELECTOR, 'span.pcp91wgn')
# reactions = total_reactions.get_attribute("textContent")
# print(reactions)
#
# element = driver.find_element(By.CSS_SELECTOR, "a.gpro0wi8.b1v8xokw")
# posted_time = element.get_attribute('textContent')
# print(posted_time)
#
# list_of_images = []
# elements = driver.find_elements(By.CSS_SELECTOR, 'div.do00u71z.ni8dbmo4.stjgntxs.l9j0dhe7 img.i09qtzwb')
# for element in elements:
#     list_of_images.append(element.get_attribute('src'))
# print(list_of_images)
#
# div_text = driver.find_element(By.CSS_SELECTOR, "a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4 ")
# text = div_text.get_attribute('href')
# text = text[:text.rfind("/")]
# print(text)
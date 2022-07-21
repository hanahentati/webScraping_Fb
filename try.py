#imports here
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.w
import time
from urllib.request import urlopen

#disable alert
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/GMI/chromedriver.exe', chrome_options=chrome_options)
driver.maximize_window()
#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("hentati.hana.dev@gmail.com")
password.clear()
password.send_keys("bayawamaidsama1397441")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!


query = 'sql'
urlq = urllib.parse.quote_plus(query)

# wait 5 seconds to allow your new page to load
time.sleep(5)
images = []

# go to the post that have the word in them
text=driver.get("https://www.facebook.com/search/" + "posts" + "/?q="+urlq)
# time.sleep(5)
#
#     # scroll down
#     # increase the range to sroll more
#     # example: range(0,10) scrolls down 650+ images
# for j in range(0, 1):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(10)
#
# # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']"))).click()
# # load_more_comment = driver.find_elements(By.XPATH,"//div[@aria-label='Leave a comment']//button").click()
# # print("Found {}".format(str(load_more_comment)))
#
# # element = driver.find_elements(By.XPATH,"//div[@role='button']")
# # driver.execute_script("arguments[0].click();", element)
# clear_button = driver.find_element(By.XPATH, "//div[@aria-label='Leave a comment'][@role='button']")
# # print("---------",clear_button,"***********")
# # button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Leave a comment'][@role='button']"))).click()
# driver.execute_script("arguments[0].click();", clear_button)
# comments = []
# links = driver.find_element(By.CSS_SELECTOR, 'div.ecm0bbzt.e5nlhep0.a8c37x1j') or driver.find_element(By.CSS_SELECTOR, 'span.nc684nl6')
#
#
# comments.append(links.get_attribute('textContent'))
# print(comments)

# page = urlopen("https://www.facebook.com/search/" + "posts" + "/?q="+urlq)
driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)

print(html)
# print("---------",button,"***********")
# gtad4xkn
#     # target all the link elements on the page
#     anchors = driver.find_elements_by_tag_name('a')
#     anchors = [a.get_attribute('href') for a in anchors]
#     # narrow down all links to image links only
#     anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/search/posts/?q=hana")]
#
#     print('Found ' + str(len(anchors)) + ' links to images')
#
#     # extract the [1]st image element in each link
#     for a in anchors:
#         driver.get(a)  # navigate to link
#         time.sleep(5)  # wait a bit
#         img = driver.find_elements_by_tag_name("img")
#         images.append(img[1].get_attribute("src"))  # may change in future to img[?]
#
# print('I scraped ' + str(len(images)) + ' images!')
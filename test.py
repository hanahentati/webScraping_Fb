import re
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

# chromedriver_autoinstaller.install()
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
#
path = 'C:/Users/GMI/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com/jypnation")
#get the text within the post
div_text = driver.find_element(By.CSS_SELECTOR, '[data-ad-comet-preview]')
text = div_text.get_attribute('textContent')
print(text)
# get the number of comment in a page
elements = driver.find_elements(By.CSS_SELECTOR, "div.gtad4xkn ")
comments = "0"
for element in elements:
    text = element.get_attribute("textContent")

    if "commentaires" in text:
        comments = int(re.findall("\d+", text)[0])
print(comments)
# get the number of partage in a page
elements = driver.find_elements(By.CSS_SELECTOR, "div.gtad4xkn ")
shares = "0"
for element in elements:
    text = element.get_attribute("textContent")

    if "partages" in text:
        shares = int(re.findall("\d+", text)[0])
print(shares)
# get number of reaction
total_reactions = driver.find_element(By.CSS_SELECTOR, 'span.pcp91wgn')
reactions = total_reactions.get_attribute("textContent")
print(reactions)

element = driver.find_element(By.CSS_SELECTOR, "a.gpro0wi8.b1v8xokw")
posted_time = element.get_attribute('textContent')
print(posted_time)

list_of_images = []
elements = driver.find_elements(By.CSS_SELECTOR, 'div.do00u71z.ni8dbmo4.stjgntxs.l9j0dhe7 img.i09qtzwb')
for element in elements:
    list_of_images.append(element.get_attribute('src'))
print(list_of_images)

div_text = driver.find_element(By.CSS_SELECTOR, "a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4 ")
text = div_text.get_attribute('href')
text = text[:text.rfind("/")]
print(text)
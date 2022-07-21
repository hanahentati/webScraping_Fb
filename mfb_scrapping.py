from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
import urllib.parse
# code to ignore browser notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('C:/Users/GMI/chromedriver.exe', chrome_options=chrome_options)

# open the webpage
link = "https://mbasic.facebook.com/"

driver.get(link)

# target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# enter username and password
username.clear()

username.send_keys("hentati.hana.dev@gmail.com")
password.clear()
# use your username and password
password.send_keys("bayawamaidsama1397441")

# target the login button and click it
time.sleep(5)
button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))).click()


# We are logged in!
print("Logged in")

query = 'kpop'
urlq = urllib.parse.quote_plus(query)
url= "https://mbasic.facebook.com/search/posts/?q="+urlq

print(url)
driver.get(url)

anchors = driver.find_element(By.CSS_SELECTOR, "[class='dj']") or driver.find_element(By.CSS_SELECTOR, "[class='di']")
link = anchors.get_attribute('href')
print(link)
url_link = "https://mbasic.facebook.com/" + link
print(url_link)

driver.get(link)

# comments =[]
# # comments_element = drive.find_element(By.CSS_SELECTOR,"div.ed") or drive.find_element(By.CSS_SELECTOR,"div.ee") or drive.find_element(By.CSS_SELECTOR,"div.eg")or drive.find_element(By.CSS_SELECTOR,"div.ec")
# comments_element = driver.find_elements(By.CSS_SELECTOR,"[class='ed']") or driver.find_elements(By.CSS_SELECTOR,"[class='eg']") or driver.find_elements(By.CSS_SELECTOR,"[class='ec']")or driver.find_elements(By.CSS_SELECTOR,"[class='ea']")
# print("**************************")
# print(comments_element)
# for comment in comments_element:
#     print(comment)
#     comment = comment.text
#     # comment = comment.get_attribute('textContent')
#     print("--------------------------")
#     print(comment)
#     comments.append(comment)
#

list_of_images = []
elements = driver.find_elements(By.CSS_SELECTOR, 'div.bb') or driver.find_elements(By.CSS_SELECTOR, 'div.bs.bt')
for element in elements:
    print("hhhhhhhhhhhhhhhhhhh")
    print(element)
    text= element.get_attribute('src')
    print(text)
    print("ooooooooooooo")
    list_of_images.append(element.get_attribute('src'))
    print( text)

def get_comment(drive):
    comments = []
    comments_element = driver.find_elements(By.CSS_SELECTOR, "[class='ed']") or driver.find_elements(By.CSS_SELECTOR,"[class='eg']") or driver.find_elements(
        By.CSS_SELECTOR, "[class='ec']") or driver.find_elements(By.CSS_SELECTOR, "[class='ea']")
    print("**************************")
    print(comments_element)
    for comment in comments_element:
        print(comment)
        comment = comment.text
        # comment = comment.get_attribute('textContent')
        print("--------------------------")
        print(comment)
        comments.append(comment)

def get_images(drive):
    list_of_images = []
    elements = post.find_elements(By.CSS_SELECTOR, 'div.do00u71z.ni8dbmo4.stjgntxs.l9j0dhe7 img.i09qtzwb')
    for element in elements:
        list_of_images.append(element.get_attribute('src'))
    return list_of_images

# def get_comment_href():
#     anchors = driver.find_element(By.CSS_SELECTOR,"a.dj")
#     link = anchors.get_attribute('href')
#     url_link= "https://mbasic.facebook.com/"+link
#     print(url_link)

# program to parse user name who posted comment
# def Nameparse():
#     driver.get(url)
#     names = driver.find_elements(By.TAG_NAME,'h3')
#     for name in names:
#         name = name.text
#         if name == 'Narendra Modi':  # Omitting Narendra modi name from parsed list
#             continue
#         Name.append(name)
#
#
# # program to parse comments
# def Commentparse():
#     driver.get(url)
#     comments = driver.find_elements(By.CSS_SELECTOR,"[class='ed']") or driver.find_elements(By.CSS_SELECTOR,
#         "[class='ee']") or driver.find_elements(By.CSS_SELECTOR,"[class='eg']")
#     for comment in comments:
#         comment = comment.text
#         Comment.append(comment)
#
#
# # Program to scrap comments from each page
# Name = []
# Comment = []
# cnt = 0
# # program to parse comments from 5 pages, if you want comments from all pages then use while loop
# for i in range(6):
#     # while True:
#     url = ("https://mbasic.facebook.com/story.php?story_fbid=pfbid0bKLYKqyRvH4moDo6Ythjyvm146eVqEsaQ7cHBDWw1yz68m2qonLUbvqXY45NdvkFl&id=166105103436041&refid=8&_ft_=qid.-5945334933790118761%3Amf_story_key.-4125898141492481991%3Atop_level_post_id.5553409891372175%3Acontent_owner_id_new.166105103436041%3Apage_id.166105103436041%3Astory_location.5%3Astory_attachment_style.share%3Aview_time.1658314454%3Afilter.h_nor%3Aott.AX-bFqCjDJQHuLQG%3Aweight.4245.8857421875%3Asty.263%3Amf_objid.5553409891372175%3Aent_attachement_type.ExternalShareAttachment%3Aapp_id.966242223397117%3Aviewstate_id.-4125898141492481991%3Apos.1%3Apage_insights.%7B%22166105103436041%22%3A%7B%22page_id%22%3A166105103436041%2C%22page_id_type%22%3A%22page%22%2C%22actor_id%22%3A166105103436041%2C%22dm%22%3A%7B%22isShare%22%3A1%2C%22originalPostOwnerID%22%3A0%7D%2C%22psn%22%3A%22EntStatusCreationStory%22%2C%22post_context%22%3A%7B%22object_fbtype%22%3A266%2C%22publish_time%22%3A1658313703%2C%22story_name%22%3A%22EntStatusCreationStory%22%2C%22story_fbid%22%3A%5B5553409891372175%5D%7D%2C%22role%22%3A1%2C%22sl%22%3A5%2C%22targets%22%3A%5B%7B%22actor_id%22%3A166105103436041%2C%22page_id%22%3A166105103436041%2C%22post_id%22%3A5553409891372175%2C%22role%22%3A1%2C%22share_id%22%3A0%7D%5D%7D%7D%3Aactrs.166105103436041%3Atds_flgs.3%3Aftmd_400706.111111l&__tn__=%2AW-R")
#     url = url + str(cnt)
#     Nameparse()
#     print(Name)
#     Commentparse()
#     print("mmmmmmmm",Comment)
#     print(url)
#     cnt = cnt + 10
#
# # create a dataframe
# data = pd.DataFrame({'Name': Name, 'Comment': Comment})
# data.to_csv('Facebbok_comments.csv')
# print('data saved')
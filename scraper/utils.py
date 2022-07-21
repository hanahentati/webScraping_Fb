
import re
import requests
import time

from tqdm import tqdm
import numpy as np
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def initialize_driver():
    """ Initialize the driver for windows, and returns the driver
    """

    # disable alert
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # specify the path to chromedriver.exe (download and save on your computer)
    driver = webdriver.Chrome('C:/Users/GMI/chromedriver.exe', chrome_options=chrome_options)
    driver.maximize_window()
    # open the webpage
    driver.get("http://www.facebook.com")

    # target username
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

    # enter username and password
    username.clear()
    username.send_keys("hentati.hana.dev@gmail.com")
    password.clear()
    password.send_keys("bayawamaidsama1397441")

    # target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    # We are logged in!



    return driver
def get_full_path(name: str) -> str:
    """ Get the full URL of a facebook page, and returns the full URL of a facebook page corresponding
    to the name.
    """

    return "https://www.facebook.com/search/" + "posts" + "/?q="+name




def scroll(driver):
        """routine to scroll through the Facebook page
        Input:
        range(5): number of times to scroll you can change the number
        """
        try:
            for i in tqdm(range(5), desc="Scrolling"):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(np.random.randint(5, 15))
        except Exception as e:
            print(f"Scrolling stopped! {e}")

def see_more_comment(driver):

    clear_button = driver.find_element(By.XPATH, "//div[@aria-label='Leave a comment'][@role='button']")
    driver.execute_script("arguments[0].click();", clear_button)
    time.sleep(100)
    more_comments = driver.find_element(By.CSS_SELECTOR,"div.j83agx80.buofh1pr.jklb3kyz.l9j0dhe7")
    for coment in more_comments:
        text = coment.get_attribute('textContent')
        if "more comments" in text:
            clear_button = driver.find_element(By.XPATH, "//div[@role='button']")
            driver.execute_script("arguments[0].click();", clear_button)
            time.sleep(100)




def get_text(post):
    """ Scrap the text of the current post,
     and returns an str if the post contain a text description.
                None if the post contain Only images/video/pdf
    """
    try:
        div_text = post.find_element(By.CSS_SELECTOR, '[data-ad-comet-preview]')
        text = div_text.get_attribute('textContent')
    except:
        text = None
    return text

def get_fullcomments(post):

    comments = []
    try:

        link = post.find_element(By.CSS_SELECTOR, 'div.ecm0bbzt.e5nlhep0.a8c37x1j')
        text = link.get_attribute('textContent')

        comments.append(text)

    except:
        text = None
    return comments


def get_comments(post):
    """ Scrap the number of comments in the current post, and returns the number of comments.
    """

    elements = post.find_elements(By.CSS_SELECTOR, "div.gtad4xkn ")
    comments = "0"
    for element in elements:
        text = element.get_attribute("textContent")

        if "comments" in text:
            comments = int(re.findall("\d+", text)[0])

    return comments

def get_shares(post):
    """ Scrap the shares  of the current post, and returns the number of shares.

    """

    elements = post.find_elements(By.CSS_SELECTOR, "div.gtad4xkn ")
    shares = "0"

    for element in elements:
        text = element.get_attribute("textContent")
        if "shares" in text:
            shares = int(re.findall("\d+", text)[0])

    return shares

def get_images(post):
    """ Scrap all the images of the current post,
     and returns the links of all images of the current post.
    """

    list_of_images = []
    elements = post.find_elements(By.CSS_SELECTOR, 'div.do00u71z.ni8dbmo4.stjgntxs.l9j0dhe7 img.i09qtzwb')
    for element in elements:
        list_of_images.append(element.get_attribute('src'))
    return list_of_images


def get_link_video(post):
    """ Scrap the video of the current post,
     and returns the link of the video if the post contain a video.
                None if not.
    """
    try:
        div_text = post.find_element(By.CSS_SELECTOR, "a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4 ")
        text = div_text.get_attribute('href')
        text = text[:text.rfind("/")]
    except:
        text = None
    return text



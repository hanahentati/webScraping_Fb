
import re
import requests
import time
import chromedriver_autoinstaller
from tqdm import tqdm
import numpy as np

from selenium import webdriver

from selenium.webdriver.common.by import By



def initialize_driver():
    """ Initialize the driver for windows, and returns the driver
    """
    path = 'C:/Users/GMI/chromedriver.exe'
    driver = webdriver.Chrome(path)
    """ 
        if you want to download the chromedriver automatically
        uncomment the code bellow
    """
    # chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
    # # and if it doesn't exist, download it automatically,
    # # then add chromedriver to path
    #
    # driver = webdriver.Chrome()
    # driver.get("http://www.python.org")
    # assert "Python" in driver.title
    return driver
def get_full_path(name: str) -> str:
    """ Get the full URL of a facebook page, and returns the full URL of a facebook page corresponding
    to the name.
    """
    return "https://facebook.com/{}".format(name)




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


def get_comments(post):
    """ Scrap the number of comments in the current post, and returns the number of comments.
    """

    elements = post.find_elements(By.CSS_SELECTOR, "div.gtad4xkn ")
    comments = "0"
    for element in elements:
        text = element.get_attribute("textContent")

        if "commentaires" in text:
            comments = int(re.findall("\d+", text)[0])

    return comments

def get_shares(post):
    """ Scrap the shares  of the current post, and returns the number of shares.

    """

    elements = post.find_elements(By.CSS_SELECTOR, "div.gtad4xkn ")
    shares = "0"

    for element in elements:
        text = element.get_attribute("textContent")
        if "partages" in text:
            shares = int(re.findall("\d+", text)[0])

    return shares

def get_reactions(post):
    """ Scrap the reactions of the current post, and returns the number of reactions.
    """
    reactions = 0
    try:
        total_reactions = post.find_element(By.CSS_SELECTOR, 'span.pcp91wgn')
        reactions = total_reactions.get_attribute("textContent")
    except Exception as e:
        print(e)
    return reactions


def get_time(post):
    """ get the posted time of the current post, and returns it
    """

    element = post.find_element(By.CSS_SELECTOR, "a.gpro0wi8.b1v8xokw")
    posted_time = element.get_attribute('textContent')
    return posted_time


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


def check_page_exists(name: str) -> bool:
    """ Check if a facebook page exists or not using the facebook graph.
    """

    url = "https://graph.facebook.com/" + name
    response = requests.get(url)

    if response.text.find("Unsupported get request") == -1:
        return True
    else:
        return False
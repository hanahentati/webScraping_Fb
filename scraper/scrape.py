from scraper.utils import *
from selenium.webdriver.common.by import By


class FacebookScrapping:
    """A class used to represent a pages scraper."""

    def __init__(self, page_name: str):
        """
        Instantiate a FacebookScraper object.
        """

        self.driver = None
        self.page_name = page_name
        self.URL = get_full_path(page_name)

    def init_driver(self):
        """ Initialize the driver """

        self.driver = initialize_driver()
        self.driver.get(self.URL)
        scroll(self.driver)
        see_more_comment(self.driver)

    def scrape_data(self):
        """ Function to scrap all the posts of the current facebook page opened by the driver.
        Returns:
            data (dict): A dictionary containing all the scraped posts from the page.
        """
        data = {}

        all_posts = self.driver.find_elements(By.CSS_SELECTOR, '[aria-posinset]')
        for index, post in enumerate(all_posts):
            id = index
            text = get_text(post)
            video = get_link_video(post)
            comments = get_comments(post)
            shares = get_shares(post)
            full_comment = get_fullcomments(post)
            images = get_images(post)

            data[id] = {
                "page_name": self.page_name,
                "shares_count": shares,
                "comments_count": comments,
                "content": text,
                "full_comment": full_comment,
                "video_link": video,
                "image": images,
            }
        return data
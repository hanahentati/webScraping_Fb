from scraper.utils import *
from selenium.webdriver.common.by import By


class FacebookScrapping:
    """A class used to represent a single page scraper."""

    def __init__(self, page_name: str, timeout: int):
        """
        Instantiate a FacebookScraper object.
        Args:
            page_name (str): the name of the page
            timeout (int): the maximum time for scraping
        """

        self.driver = None
        self.page_name = page_name
        self.URL = get_full_path(page_name)
        self.timeout = timeout

    def init_driver(self):
        """ Initialize the driver """

        self.driver = initialize_driver()
        self.driver.get(self.URL)
        scroll(self.driver)

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
            total_reactions = get_reactions(post)
            posted_time_of_cp = get_time(post)
            images = get_images(post)

            data[id] = {
                "page_name": self.page_name,
                "shares_count": shares,
                "comments_count": comments,
                "reaction_count": total_reactions,
                "content": text,
                "posted_on": posted_time_of_cp,
                "video_link": video,
                "image": images,
            }
        return data
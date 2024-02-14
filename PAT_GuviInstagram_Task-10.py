from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class GuviInstagram:
    def __init__(self, profile_url):
        """Constructor method to initialize GuviInstagram instance."""
        self.profile_url = profile_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """Method to navigate to the profile URL, maximize window, and wait."""
        self.driver.get(self.profile_url)
        self.driver.maximize_window()
        sleep(5)

    def get_followers(self):
        """Method to retrieve follower count using XPATH - Absolute xpath."""
        followers_element = self.driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button')
        if followers_element:
            return followers_element[0].text
        else:
            return "0"

    def get_following(self):
        """Method to retrieve following count using XPATH - Absolute xpath."""
        following_element = self.driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button')
        if following_element:
            return following_element[0].text
        else:
            return "0"

    def quit(self):
        """Method to quit the WebDriver instance."""
        self.driver.quit()

# Usage
profile_url = "https://www.instagram.com/guviofficial/"
obj = GuviInstagram(profile_url)
obj.boot()
followers_count = obj.get_followers()
following_count = obj.get_following()
print("Followers:", followers_count)
print("Following:", following_count)
obj.quit()

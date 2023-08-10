from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


class Profile:
    """
    Class - `Profile`
    Example:
    ```
    profile = Profile()
    ```\n
    Methods :\n
    1. ``.getinfo() | Response - Title, description, avatar and banner image, user name, 
                                 industry, location, join date and following, follower, 
                                 subscriber and tweet count of a Profile.
        Note: For the arguments in calling getInfo() function:-
              login_username: apply your twitter account username not email only username,
              login_password: apply your twitter account password,
              profile_username: apply the twitter username for the account you want to scrape the data
    """

    def __init__(self, login_username, login_password, profile_username):
        self.login_username = login_username
        self.login_password = login_password
        self.profile_username = profile_username

    def getInfo(self):
        """
        Class - `Profile`
        Example:
        ```
        elon = Profile(login_username, login_password, profile_username)
        elon.getInfo()
        ```
        Returns:
        {
            "name": Name of the Profile
            "avatar_url": Avatar image link of the Profile
            "banner_url": Banner image link of the Profile
            "description": Description of the Profile
            "user_name": User name of the Profile
            "industry": Industry of the Profile
            "location": Location of the Profile
            "join_date": Join date of the Profile
            "following_count": No. of accounts following by the Profile
            "follower_count": No. of follwers of the Profile
            "subscriber_count": No. of subscribers of the Profile
            "tweet_count": No. of tweets of the Profile
        }
        """
        driver = Chrome(ChromeDriverManager().install())
        try:
            driver.get('https://twitter.com/login')
            sleep(3)
            profile_data = {"profile_data": []}
            username = driver.find_element("xpath", '//input[@autocomplete="username"]')
            username.send_keys(self.login_username)
            username.send_keys(Keys.RETURN)
            sleep(1)
            password = driver.find_element("xpath", '//input[@name="password"]')
            sleep(1)
            password.send_keys(self.login_password)
            password.send_keys(Keys.RETURN)
            sleep(2)
            driver.get('https://twitter.com/' + self.profile_username)
            sleep(5)

            name = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/span/span[1]').text
            avatar = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/a').get_attribute('href')
            banner = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/a/div/div[2]/div/img').get_attribute('src')
            try:
                desc = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div/span').text
            except:
                desc = ""
            try:
                industry = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span').text
            except:
                industry = ""
            try:
                location = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[2]/span/span').text
            except:
                location = ""
            try:
                subscriber_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[3]/a/span[1]/span').text
            except:
                subscriber_count = ""
            try:
                try:
                    join_date = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[2]/span').text
                except:
                    join_date = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/span[2]/span').text
            except:
                join_date = ""
            try:
                try:
                    following_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
                except:
                    following_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div[1]/a/span[1]/span').text
            except:
                following_count = ""
            try:
                try:
                    follower_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text
                except:
                    follower_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div[2]/a/span[1]/span').text
            except:
                follower_count = ""
            user_name = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/span').text
            tweet_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div').text
            

            profile_data["profile_data"].append(
                {
                    "name": name,
                    "avatar_url": avatar,
                    "banner_url": banner,
                    "description": desc,
                    "user_name": user_name,
                    "industry": industry,
                    "location": location,
                    "join_date": join_date,
                    "following_count": following_count,
                    "follower_count": follower_count,
                    "subscriber_count": subscriber_count,
                    "tweet_count": tweet_count
                }
            )
            return profile_data["profile_data"]
        except:
            return None

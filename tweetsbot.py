from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep



class Tweetsbot:
	def __init__(self, user):
		self.tweets_collected = []
		self.user = user
		self.url = "https://twitter.com/"+self.user
		self.path = "/XXXXXXXXXXXXXXXXXXXXXXX/geckodriver"
		
		self.__start(self.path, self.url)


	def __start(self, path, url):
		print("Bot is Started")
		driver = webdriver.Firefox(options=self.__options(), executable_path=path)
		driver.get(url)
		sleep(5)
		self.__scroll(driver)


	def __tweets(self, driver):
		tweets = driver.find_elements_by_tag_name("article")
		for tweet in tweets:
			__spans = tweet.find_elements_by_tag_name("span")
			for __s in __spans:
				if len(str(__s.text)) > 50:
					if str(__s.text) not in self.tweets_collected:
						self.tweets_collected.append(str(__s.text))
						print(str(__s.text))
		print("{} Tweets Collected".format(len(self.tweets_collected)))
		return


	def __scroll(self, driver):
		print("Bot is Scrolling")
		SCROLL_PAUSE_TIME = 2
		# Get scroll height
		last_height = driver.execute_script("return document.body.scrollHeight")
		while True:
		    # Scroll down to bottom
		    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		    # Wait to load page
		    sleep(SCROLL_PAUSE_TIME)
		    self.__tweets(driver)
		    # Calculate new scroll height and compare with last scroll height
		    new_height = driver.execute_script("return document.body.scrollHeight")
		    if new_height == last_height:
		        break
		    last_height = new_height
		return


	def __options(self):
		"""
		Configuring options of the Bot
		"""
		options = Options()
		options.add_argument("Cache-Control=no-cache")
		options.add_argument("--no-sandbox")
		options.add_argument("--dns-prefetch-disable")
		options.add_argument("--disable-dev-shm-usage")
		options.add_argument("--disable-web-security")
		options.add_argument("--ignore-certificate-errors")
		options.page_load_strategy = 'none'
		options.add_argument("--ignore-certificate-errors-spki-list")
		options.add_argument("--ignore-ssl-errors")
		return options


tw = Tweetsbot("username_in_url")

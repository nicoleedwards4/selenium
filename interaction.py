from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# wikipedia example
# wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
#
# driver.get(wiki_url)
#
# english_articles = driver.find_element("xpath", '//*[@id="articlecount"]/a[1]')
# article_count = english_articles.text
# # english_articles.click()
#
# search = driver.find_element("name", "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# form sign up example
form_url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(form_url)

first = driver.find_element("name", "fName")
first.send_keys("myfirst")

last = driver.find_element("name", "lName")
last.send_keys("mylast")

email = driver.find_element("name", "email")
email.send_keys("myemail@email.com")

submit = driver.find_element("css selector", "form button")
submit.click()

# driver.close()



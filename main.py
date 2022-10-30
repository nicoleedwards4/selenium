from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Amazon price example
# amazon_html = "https://www.amazon.com/dp/1801813051/ref=sspa_dk_detail_0?ie=UTF8&psc=1&pd_rd_i=&pd_rd_i" \
#               "=1801813051p13NParams&s=books&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM "
# driver.get(amazon_html)
# price = driver.find_element("id", "price")
# print(price.text)

python_url = "https://www.python.org/"

driver.get(python_url)

events = {}

for i in range(0, 5):
    upcoming_event_time = driver.find_element("xpath",
                                              f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i + 1}]/time')
    upcoming_event_name = driver.find_element("xpath",
                                              f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i + 1}]/a')
    events[i] = {
        "time": upcoming_event_time.text,
        "name": upcoming_event_name.text,
    }

print(events)
driver.close()

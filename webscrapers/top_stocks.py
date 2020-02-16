from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 


def scrape():
    # sets options for driver 
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    # initialize driver
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    driver.get('https://finance.yahoo.com/most-active?offset=0&count=100')

    # get rows
    rows = driver.find_elements_by_class_name('simpTblRow')
    stock_keys = [r.text.split()[0] for r in rows]
    return stock_keys



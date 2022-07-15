import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

web = 'https://www.youtube.com/'
service = Service('/Users/UltraBook/PycharmProjects/pythonProject1/venv/Lib/site-packages/selenium/webdriver/chromium'
                  '/chromedriver')

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(web)

# try to reject cookies only in case it is required
try:
    reject_cookies = driver.find_element(by=By.XPATH, value='.//tp-yt-paper-button [contains(@class, "style-scope '
                                                            'ytd-button-renderer style-primary size-default")]')
    reject_cookies.click()
except selenium.common.exceptions.NoSuchElementException:
    pass

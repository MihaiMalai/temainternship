import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from internet_connection import check_internet

chrome_options = webdriver.ChromeOptions()

web = 'https://www.youtube.com/'
# provide your file's path to chromedriver
service = Service('/Users/UltraBook/PycharmProjects/pythonProject1/venv/Lib/site-packages/selenium/webdriver/chromium'
                  '/chromedriver')

check_internet()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(web)

check_internet()

# reject cookies in case it is required
try:
    reject_cookies = driver.find_element(by=By.XPATH, value='.//tp-yt-paper-button [contains(@class, "style-scope '
                                                            'ytd-button-renderer style-primary size-default")]')
    reject_cookies.click()
except selenium.common.exceptions.NoSuchElementException:
    pass

check_internet()

# access the first video in the list using the link from 'href' by full XPath
first_video = driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two'
                                                     '-column-browse-results-renderer/div['
                                                     '1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row['
                                                     '1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div['
                                                     '1]/ytd-thumbnail/a')
first_video.get_attribute('href')
first_video.click()

# waiting to load the video
time.sleep(3)
fullscreen = driver.find_element(by=By.XPATH, value='.//button [contains(@class, "ytp-fullscreen-button ytp-button")]')
fullscreen.click()

# waiting 4 secs to be able to skip the add
time.sleep(4)

check_internet()

try:
    skip_add = driver.find_element(by=By.XPATH, value='.//button [contains(@class, "ytp-ad-skip-button ytp-button")]')
    skip_add.click()
except selenium.common.exceptions.NoSuchElementException:
    time.sleep(7)  # exception in case the add is longer
    try:
        skip_add = driver.find_element(by=By.XPATH, value='.//button [contains(@class, "ytp-ad-skip-button '
                                                          'ytp-button")]')
        skip_add.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass  # in case you can't skip the add

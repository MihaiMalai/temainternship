import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from internet_connection import check_internet
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %('
                                                                                 'message)s')

chrome_options = webdriver.ChromeOptions()

logging.info('Assigning youtube.com link to a variable')
web = 'https://www.youtube.com/'
logging.info('Assigning chromedriver path service to a variable')
# provide your file's path to chromedriver
service = Service('/Users/UltraBook/PycharmProjects/pythonProject1/venv/Lib/site-packages/selenium/webdriver/chromium'
                  '/chromedriver')

check_internet()

logging.info('Opening google chrome browser')
driver = webdriver.Chrome(service=service, options=chrome_options)
logging.info('Accessing youtube.com')
driver.get(web)

check_internet()

# waiting to load youtube.com
time.sleep(3)

logging.info('Managing cookies')
# reject cookies in case it is required
try:
    reject_cookies = driver.find_element(by=By.XPATH, value='.//tp-yt-paper-button [contains(@class, "style-scope '
                                                            'ytd-button-renderer style-primary size-default")]')
    reject_cookies.click()
    logging.info('Cookies successfully rejected')
except selenium.common.exceptions.NoSuchElementException as ne:
    logging.exception('Exception occurred, no cookies pop-up displayed')

check_internet()

logging.info('Accessing the first displayed video')
# access the first video in the list using the link from 'href' by full XPath
first_video = driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two'
                                                     '-column-browse-results-renderer/div['
                                                     '1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row['
                                                     '1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div['
                                                     '1]/ytd-thumbnail/a')
first_video.get_attribute('href')
first_video.click()

logging.info('Loading video')
# waiting to load the video
time.sleep(3)

logging.info('Making video full screen')
fullscreen = driver.find_element(by=By.XPATH, value='.//button [contains(@class, "ytp-fullscreen-button ytp-button")]')
fullscreen.click()

# waiting 4 secs to be able to skip the add
time.sleep(4)

check_internet()

try:
    logging.info('Skipping the add')
    skip_add = driver.find_element(by=By.XPATH, value='.//button [contains(@class, "ytp-ad-skip-button ytp-button")]')
    skip_add.click()
except selenium.common.exceptions.NoSuchElementException:
    logging.exception('Exception occurred, waiting 6 more seconds to skip the add')
    time.sleep(6)  # exception in case the add is longer
    try:
        skip_add = driver.find_element(by=By.XPATH, value='.//button [contains(@class, "ytp-ad-skip-button '
                                                          'ytp-button")]')
        skip_add.click()
    except selenium.common.exceptions.NoSuchElementException:
        logging.exception('Exception occurred, unable to skip the add')


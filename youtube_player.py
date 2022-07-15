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

# access the first video in the list using the link from 'href' by full XPath
first_video = driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two'
                                                     '-column-browse-results-renderer/div['
                                                     '1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row['
                                                     '1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div['
                                                     '1]/ytd-thumbnail/a')
first_video.get_attribute('href')
first_video.click()

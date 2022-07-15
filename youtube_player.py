from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

web = 'https://www.youtube.com/'
path = '/Users/UltraBook/PycharmProjects/pythonProject1/venv/Lib/site-packages/selenium/webdriver/chromium/chromedriver'

driver = webdriver.Chrome(path, options=chrome_options)
driver.get(web)

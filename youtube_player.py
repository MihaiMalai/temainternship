from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

web = 'https://www.youtube.com/'
driver.get(web)

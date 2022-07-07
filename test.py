from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('https://fabrykatestow.pl')
driver.close()

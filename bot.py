from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:/chromedriver')
driver.get('https://www.nike.com.br/Snkrs/Produto/Kybrid-S2/153-169-211-252378');
time.sleep(5) 
driver.find_element_by_id('anchor-acessar').click()



time.sleep(0)
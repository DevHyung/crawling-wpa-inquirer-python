from selenium import webdriver
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://www.fangraphs.com/tools/wpa-inquirer')

for i in range(1,9):
    driver.find_element_by_xpath('//*[@id="rcbRun_Input"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="rcbRun_DropDown"]/div/ul/li[{}]'.format(i)).click()
    time.sleep(2)
    bs4 = BeautifulSoup(driver.page_source,'lxml')
    runEnv = bs4.find('input',id='rcbRun_Input')['value']
    print(runEnv)


driver.quit()

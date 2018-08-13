from selenium import webdriver
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://www.fangraphs.com/tools/wpa-inquirer')

for i in range(1,9): # 8개
    # 첫번째
    driver.find_element_by_xpath('//*[@id="rcbRun_Input"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="rcbRun_DropDown"]/div/ul/li[{}]'.format(i)).click() # 첫번쨰
    time.sleep(2)

    input("넘어가려면클릭")
    # 두번쨰
    for twoIdx in range(1,9): #8개
        driver.find_element_by_xpath('//*[@id="rcbBase_Input"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="rcbBase_DropDown"]/div/ul/li[{}]'.format(twoIdx)).click()
        time.sleep(2)
        input("넘어가려면클릭")
        bs4 = BeautifulSoup(driver.page_source, 'lxml')
        runEnv = bs4.find('input', id='rcbRun_Input')['value']
        baseSitu = bs4.find('input',id='rcbBase_Input')['value']
        print(runEnv,baseSitu)


driver.quit()

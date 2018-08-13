from selenium import webdriver
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://www.fangraphs.com/tools/wpa-inquirer')
DELAY = 5

for i in range(1,9): # 8개
    # 첫번째
    driver.find_element_by_xpath('//*[@id="rcbRun_Input"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="rcbRun_DropDown"]/div/ul/li[{}]'.format(i)).click() # 첫번쨰

    time.sleep(DELAY)

    # 두번쨰
    for twoIdx in range(1,9): #8개
        driver.find_element_by_xpath('//*[@id="rcbBase_Input"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="rcbBase_DropDown"]/div/ul/li[{}]'.format(twoIdx)).click()
        time.sleep(DELAY)

        # 세번째
        for threeIdx in range(1, 19):  # 8개
            driver.find_element_by_xpath('//*[@id="rcbInning_Input"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="rcbInning_DropDown"]/div/ul/li[{}]'.format(threeIdx)).click()
            time.sleep(DELAY)

            # 네번째 rcbOuts_Input
            for fourIdx in range(1, 4):  # 3개
                driver.find_element_by_xpath('//*[@id="rcbOuts_Input"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="rcbOuts_DropDown"]/div/ul/li[{}]'.format(fourIdx)).click()
                time.sleep(DELAY)

                # 다섯번째 rcbScore_Input
                for fiveIdx in range(1, 22):  # 21개
                    driver.find_element_by_xpath('//*[@id="rcbScore_Input"]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        '//*[@id="rcbScore_DropDown"]/div/ul/li[{}]'.format(fiveIdx)).click()
                    time.sleep(DELAY)
                    #=== TEST PRINT
                    bs4 = BeautifulSoup(driver.page_source, 'lxml')
                    runEnv = bs4.find('input', id='rcbRun_Input')['value']
                    baseSitu = bs4.find('input',id='rcbBase_Input')['value']
                    inning = bs4.find('input', id='rcbInning_Input')['value']
                    outs = bs4.find('input', id='rcbOuts_Input')['value']
                    runDifferential = bs4.find('input', id='rcbScore_Input')['value']
                    print(runEnv,baseSitu,inning,outs,runDifferential)
                    print(driver.find_element_by_xpath('//*[@id="radAjax"]/table/tbody/tr[6]/td[2]').text)
                    print(driver.find_element_by_xpath('//*[@id="radAjax"]/table/tbody/tr[8]/td[2]').text)


driver.quit()

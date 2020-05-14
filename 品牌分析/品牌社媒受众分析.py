from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
#打开品牌列表
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[3]/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[3]/ul/li/ul/li/span").click()
sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[13]/td[2]/div/a").click()
sleep(2)

#打开社媒受众分析
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/a[5]").click()
sleep(5)
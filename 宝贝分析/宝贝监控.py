from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
#宝贝监控
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/div").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/ul/li/ul/li[3]/span").click()
sleep(2)

#查看详情
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[8]/td[10]/div/p/button/span").click()
sleep(3)

#按日
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/h4/div/label[2]/span").click()





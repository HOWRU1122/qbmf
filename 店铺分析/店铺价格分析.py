from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
#关注列表
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[4]/div").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[4]/ul/li/ul/li/span").click()
sleep(5)
driver.find_element_by_xpath("//a[@title='perfectdiary旗舰店']").click()
sleep(2)
#价格分析
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/a[2]").click()
#选择日期
driver.find_element_by_xpath("//input[@placeholder='选择日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(1)


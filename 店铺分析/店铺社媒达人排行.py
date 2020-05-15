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

#社媒达人分析
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/a[6]").click()
sleep(2)
#总销量排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[2]").click()
sleep(1)
#时间选择
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(1)
#按月
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/div[3]/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table[3]/tbody/tr/td[3]/div/a").click()
sleep(1)

#切换抖音短视频
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/a[2]").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
sleep(1)
#月时间选择
driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table[3]/tbody/tr/td[3]/div/a").click()
#按周
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/div[3]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[1]").click()
sleep(1)
#周时间选择
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(1)

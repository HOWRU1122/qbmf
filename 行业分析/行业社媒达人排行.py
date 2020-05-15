from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li/ul/li/ul/li[5]").click()
sleep(1)
#关键词排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/a[5]").click()
sleep(1)
#总销量排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[2]").click()
sleep(1)
#流量排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[1]").click()
sleep(1)
#周时间选择
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[3]/td[2]/div/span").click()
sleep(1)
#按月
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2]/div[3]/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
sleep(1)
#月时间选择
driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table[3]/tbody/tr[2]/td/div/a").click()
sleep(1)
#切换抖音短视频
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div/div/a[2]").click()
sleep(2)
#日销排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
sleep(2)
#流量排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[1]").click()
sleep(1)
#月时间选择
driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table[3]/tbody/tr/td[4]/div/a").click()
sleep(2)
#按周
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2]/div[3]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[1]").click()
sleep(1)
#周时间选择
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[3]/td/div").click()
sleep(2)


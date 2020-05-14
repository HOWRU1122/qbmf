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
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/a[4]").click()
sleep(1)

#飙升排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[2]").click()
sleep(1)
#热销排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[1]").click()
sleep(1)

#日时间选择
driver.find_element_by_xpath("//input[@placeholder='选择日期']").click()

driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[4]/td/div/span").click()

#按周
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[3]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
sleep(1)
#选择周
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[3]/td[3]/div").click()
sleep(1)

#词云图
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[5]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[3]/li[2]").click()
sleep(1)
#切换销售量
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/label[2]/span").click()
sleep(2)
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
#宝贝排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/a[3]").click()
sleep(1)

#飙升排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[2]").click()
sleep(1)
#新品热销
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[3]").click()
sleep(1)
#热销排行
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[1]").click()
sleep(1)

#周时间选择
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[3]/td[4]/div").click()
sleep(1)
#按月
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[3]/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
sleep(1)
#月时间选择
driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table[3]/tbody/tr[2]/td/div/a").click()
sleep(1)
#数据来源
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[5]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
sleep(1)

#切换柱状图
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[7]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[4]/li[2]").click()
sleep(2)
#切换饼图
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[7]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[4]/li[3]").click()
sleep(2)


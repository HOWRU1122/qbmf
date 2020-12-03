from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
#抖音短视频
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li/ul/li/ul/li[4]/ul/li/ul/li/span").click()
sleep(3)
#选择时间
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[4]/div/span").click()
sleep(3)
#平均值
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/label/span[1]/span").click()
sleep(3)
#选择时间
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/input").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/table/tbody/tr[2]/td[4]/div").click()
sleep(2)
#平均值
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/label[3]/span[1]/span").click()
sleep(3)

#切换受众分析
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/a[2]").click()
sleep(5)

#切换流量分析
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/a[3]").click()
sleep(5)

#选择时间
driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[4]/div/span").click()
sleep(2)

#查看明细
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/table/tbody/tr/td[6]/div/a").click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[5]/div/div[1]/button/i").click()
sleep(1)

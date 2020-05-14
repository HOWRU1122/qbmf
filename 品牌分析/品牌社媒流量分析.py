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

#打开社媒流量分析
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/a[4]").click()
sleep(5)

#选择时间
driver.find_element_by_xpath("//input[@placeholder='选择日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(3)
#近30天
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div/h3/div/div/label[2]/span").click()
sleep(6)
#近90天
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div/h3/div/div/label[3]/span").click()
sleep(6)
#总量
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/h4/div/div/label/span/span").click()
sleep(3)

#抖音短视频
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/a[2]").click()
sleep(5)
#选择时间
driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(5)
#查看商品明细
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/a[@class='text-link']").click()
sleep(5)


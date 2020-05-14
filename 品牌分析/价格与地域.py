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

#打开价格与地域
#价格分析
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/a[2]").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[2]").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li").click()
sleep(1)
#选择时间
driver.find_element_by_xpath("//input[@placeholder='选择日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(2)
#选择数据来源
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[5]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
sleep(3)
#选择饼图
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[7]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[3]/li[2]").click()
sleep(1)

#地域分析
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[4]/li[2]").click()
sleep(1)
#选择时间
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/table/tbody/tr[2]/td[5]/div").click()
sleep(1)
#按月
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[4]/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[5]/li[2]").click()
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/table/tbody/tr/td[3]/div/a").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/table/tbody/tr/td[4]/div/a").click()
sleep(1)
#查看数据来源
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[6]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[6]/li/div/div[1]/label[4]/span[1]/span[@class='el-checkbox__inner']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[6]/li/div/div[2]/a[@class='btn']").click()
sleep(1)

#切换饼图

driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[8]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[7]/li[2]").click()
sleep(1)
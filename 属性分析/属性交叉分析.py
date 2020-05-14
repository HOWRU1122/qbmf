from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
#打开属性交叉分析
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[2]/div").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[2]/ul/li/ul/li[3]/span").click()
sleep(1)
#选择类目
driver.find_element_by_xpath("//a[@style='width: 232.021px;']").click()
sleep(1)
driver.find_element_by_xpath("//a[@title='彩妆/香水/美妆工具']").click()
sleep(3)
driver.find_element_by_xpath("//a[@title='唇膏/口红']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/h4").click()

#选择属性
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/a").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div[2]/div/a").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/button").click()
sleep(3)
#选择时间
driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(3)
#选择数据来源
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
sleep(3)
#选择折线图
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[5]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
sleep(1)
#选择宝贝列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/label[2]/span").click()
sleep(5)
#选择时间
driver.find_element_by_xpath("//input[@placeholder='选择日期']").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
sleep(3)

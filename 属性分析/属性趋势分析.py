from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
#打开属性规模分析
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[2]/div").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[2]/ul/li/ul/li[2]/span").click()
sleep(1)
#选择属性
driver.find_element_by_xpath("//a[@style='width: 232.021px;']").click()
sleep(1)
driver.find_element_by_xpath("//a[@title='彩妆/香水/美妆工具']").click()
sleep(2)
driver.find_element_by_xpath("//a[@title='唇膏/口红']").click()
sleep(2)
driver.find_element_by_xpath("//a[@title='价格']").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div").click()
#选择日期
driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
sleep(1)

driver.find_element_by_xpath("/html/body/div[3]/div/div/div/table/tbody/tr/td[3]/div/a").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div/table/tbody/tr/td[4]/div/a").click()
sleep(2)
#选择数据来源
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[3]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
sleep(2)
#选择饼图
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[5]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
sleep(1)

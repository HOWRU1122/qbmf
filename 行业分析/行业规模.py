from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
driver.find_element_by_xpath("//a[@title='彩妆/香水/美妆工具>唇膏/口红']").click()
sleep(1)
driver.find_element_by_xpath("//a[@title='彩妆/香水/美妆工具']").click()
sleep(2)
driver.find_element_by_xpath("//a[@title='唇膏/口红']").click()
sleep(1)
#选择周
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[3]/td[3]/div").click()
sleep(1)
#按月
driver.find_element_by_xpath("//span[@class='el-dropdown-link el-dropdown-selfdefine']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li[2]").click()
sleep(1)
#选择月份
driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table[3]/tbody/tr[2]/td/div/a").click()
sleep(1)

#数据涞源
driver.find_element_by_xpath("//span[@class='el-dropdown-link el-dropdown-selfdefine']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
sleep(1)

driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[5]/span").click()
sleep(1)

driver.find_element_by_xpath("/html/body/ul[3]/li[2]").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[7]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[3]/li[3]").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[7]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ul[3]/li[1]").click()
sleep(1)



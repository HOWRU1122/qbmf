from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
#打开宝贝列表
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/ul/li/ul/li/span").click()
sleep(5)

#宝贝追踪
driver.find_element_by_xpath("//a[@title='完美日记动物眼影盘锦鲤小狗小猫猫咪老虎斑虎小猪熊猫小鹿盘女']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/a[2]").click()
sleep(1)

#日期选择
driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(1)
#调价追踪
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/a[2]").click()
sleep(1)
#日期选择
driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(1)
#改名追踪
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/a[3]").click()
sleep(1)
#选择时间
driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
sleep(1)



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)



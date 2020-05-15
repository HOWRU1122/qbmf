from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[4]/div").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[4]/ul/li/ul/li[2]/span").click()
sleep(1)
#店铺对比
#选择店铺
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[2]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[7]/div/span[2]").click()
sleep(2)
#选择店铺
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[3]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li[2]/div/span[2]").click()
sleep(2)
#选择店铺
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[4]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[5]/div/div/ul/li[5]/div/span[2]").click()
sleep(2)
#按周
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/button[2]").click()
sleep(2)
#按月
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/button[3]").click()
sleep(2)
#清空店铺
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th/button/span").click()
sleep(1)

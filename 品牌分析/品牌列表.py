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
#日热销列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/button[2]/span").click()
sleep(3)
#日飙升列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/button[3]/span").click()
sleep(3)
#关注列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/button/span").click()
sleep(4)
#打开近7天、30天销售额销售量
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label/span/span").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[2]/span/span").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[3]/span/span").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[4]/span/span").click()


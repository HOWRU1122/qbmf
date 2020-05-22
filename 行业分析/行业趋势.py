import unittest

from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
class Assert_test(unittest.TestCase):
    #获取规模里的表格数据
    # 按月
    driver.find_element_by_xpath("//span[@class='el-dropdown-link el-dropdown-selfdefine']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[2]").click()
    sleep(1)
    # 月时间选择
    driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table[3]/tbody/tr/td[4]/div/a").click()
    sleep(1)
    # 获取表格销售额
    money = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/span").get_attribute(
        "textContent")
    print(money)
    # 获取表格销售量
    amount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[4]/div").get_attribute(
        "textContent")
    print(amount)
#跳到属性趋势
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li/ul/li/ul/li[2]").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div/div/div[2]/span").click()
    sleep(1)
#时间区间
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div/table/tbody/tr/td[4]/div/a").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div/table/tbody/tr/td[4]/div/a").click()
    sleep(1)
#获取趋势里的表格数据
    trendmoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/span").get_attribute(
        "textContent")
    print(trendmoney)
# 获取表格销售量
    trendamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[3]/table/tbody/tr[2]/td[5]/div").get_attribute(
        "textContent")
    print(trendamount)

#数据来源
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[3]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
    sleep(1)
#切换折线图
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[5]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
    sleep(1)

    def test_case1(self, a=money, b=trendmoney):
        try:
            self.assertEqual(a, b, msg="行业趋势销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=amount, d=trendamount):
        try:
            self.assertEqual(c, d, msg="行业趋势销售量对不上"),
        except AssertionError as msg2:
            print(msg2)


if __name__ == "__main__":
    unittest.main()

import unittest

from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options = webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)


class Assert_test(unittest.TestCase):
    # 选择类目
    driver.find_element_by_xpath("//a[@title='彩妆/香水/美妆工具>唇膏/口红']").click()
    sleep(1)
    driver.find_element_by_xpath("//a[@title='彩妆/香水/美妆工具']").click()
    sleep(2)
    driver.find_element_by_xpath("//a[@title='唇膏/口红']").click()
    sleep(1)

    # 获取头部销售额
    toolmoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/p[1]/span").get_attribute("textContent")
    print(toolmoney)
    # 获取头部销售量
    toolamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/p[1]").get_attribute("textContent")
    print(toolamount)
    # 周时间选择
    driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[3]/td[3]/div").click()
    sleep(1)
    # 按月
    driver.find_element_by_xpath("//span[@class='el-dropdown-link el-dropdown-selfdefine']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[2]").click()
    sleep(1)
    # 月时间选择
    driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table[3]/tbody/tr[2]/td/div/a").click()
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
    # 数据涞源
    driver.find_element_by_xpath("//span[@class='el-dropdown-link el-dropdown-selfdefine']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
    sleep(2)
    # 切换柱状图
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[5]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[3]/li[2]").click()
    sleep(2)
    # 切换饼图
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[7]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[3]/li[3]").click()
    sleep(2)

    def test_case1(self, a=toolmoney, b=money):
        try:
            self.assertEqual(a, b, msg="行业规模销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=toolamount, d=amount):
        try:
            self.assertEqual(c, d, msg="行业规模销售量对不上"),
        except AssertionError as msg2:
            print(msg2)


if __name__ == "__main__":
    unittest.main()

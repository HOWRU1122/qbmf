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
# 打开宝贝列表
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/ul/li/ul/li/span").click()
sleep(5)


class Assert_test(unittest.TestCase):
    # 获取宝贝列表数据
    listdaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[6]/td[3]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(listdaymoney)

    listdayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[6]/td[5]/div").get_attribute(
        "textContent")
    print(listdayamount)
    # 价格走势
    driver.find_element_by_xpath("//a[@title='完美日记十二色动物眼影盘小狗小猫猫咪老虎斑虎小猪小鹿小熊猫盘']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/a[3]").click()
    sleep(1)
    # 获取头部数据
    tooldaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/p[2]/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(listdaymoney)

    tooldayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/p[2]").get_attribute(
        "textContent")
    print(listdayamount)

    # 获取表格数据
    tabledaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[5]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(tabledaymoney)

    tabledayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[3]/div").get_attribute(
        "textContent")
    print(tabledayamount)
    # 时间选择
    driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
    sleep(2)

    def test_case1(self, a=listdaymoney, b=tooldaymoney):
        try:
            self.assertEqual(a, b, msg="宝贝价格走势日销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=listdayamount, d=tooldayamount):
        try:
            self.assertEqual(c, d, msg="宝贝价格走势日销售量对不上"),
        except AssertionError as msg2:
            print(msg2)

    def test_case3(self, e=tooldaymoney, f=tabledaymoney):
        try:
            self.assertEqual(e, f, msg="宝贝价格走势日销售额对不上"),
        except AssertionError as msg3:
            print(msg3)

    def test_case4(self, g=tooldayamount, h=tabledayamount):
        try:
            self.assertEqual(g, h, msg="宝贝价格走势日销售量对不上"),
        except AssertionError as msg4:
            print(msg4)

    def test_case5(self, i=tabledaymoney, j=listdaymoney):
        try:
            self.assertEqual(i, j, msg="宝贝价格走势30日销售额对不上"),
        except AssertionError as msg5:
            print(msg5)

    def test_case6(self, k=tabledayamount, l=listdayamount):
        try:
            self.assertEqual(k, l, msg="宝贝价格走势30日销售量对不上"),
        except AssertionError as msg6:
            print(msg6)


if __name__ == "__main__":
    unittest.main()

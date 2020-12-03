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
# 打开品牌列表
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[3]/div/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[3]/ul/li/ul/li/span").click()
sleep(4)
# 打开近7天、30天销售额销售量
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label/span/span").click()
driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[2]/span/span").click()
driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[3]/span/span").click()
driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[4]/span/span").click()


class Assert_test(unittest.TestCase):
    # 获取当日、近7天、30天销售额销售量
    listdaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[6]/td[3]/div/span").get_attribute(
        "textContent").strip().replace('w','')
    print(listdaymoney)
    listsevendaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[6]/td[7]/div/span").get_attribute(
        "textContent").strip().replace('w','')
    print(listsevendaymoney)
    listthittydaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[6]/td[9]/div/span").get_attribute(
        "textContent").strip().replace('w','')
    print(listthittydaymoney)

    listdayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[6]/td[5]/div").get_attribute(
        "textContent")
    print(listdayamount)
    listsevendayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[6]/td[8]/div").get_attribute(
        "textContent")
    print(listsevendayamount)
    listthittydayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[6]/td[10]/div").get_attribute(
        "textContent")
    print(listthittydayamount)
    # 打开趋势分析
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[6]/td[2]/div/a").click()
    sleep(3)
    # 获取当日、近7天、30天销售额销售量
    tooldaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/p[2]/span").get_attribute("textContent").strip().replace('w','')
    print(tooldaymoney)
    toolsevendaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/p[2]/span").get_attribute("textContent").strip().replace('w','')
    print(toolsevendaymoney)
    toolthittydaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/p[2]/span").get_attribute("textContent").strip().replace('w','')
    print(toolthittydaymoney)
    tooldayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/p[2]").get_attribute("textContent").strip().replace(' ','')
    print(tooldayamount)
    toolsevendayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/p[2]").get_attribute("textContent").strip().replace(' ','')
    print(toolsevendayamount)
    toolthittydayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/p[2]").get_attribute("textContent").strip().replace(' ','')
    print(toolthittydayamount)
    # 切换销售额销售量
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[2]").click()
    sleep(2)
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li").click()
    sleep(2)
    # 获取表格中销售额销售量
    tabledaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div/span").get_attribute(
        "textContent")
    print(tabledaymoney)

    tabledayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[4]/div").get_attribute(
        "textContent")
    print(tabledayamount)

    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
    sleep(1)

    # 选择时间
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div[3]/div[2]/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr/td/div/a").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr/td[4]/div/a").click()
    sleep(3)
    # 数据来源
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
    sleep(3)

    # 切换抖音直播
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/a[2]").click()
    sleep(3)

    def test_case1(self, a=listdaymoney, b=tooldaymoney):
        try:
            self.assertEqual(a, b, msg="品牌趋势当日销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=listdayamount, d=tooldayamount):
        try:
            self.assertEqual(c, d, msg="品牌趋势当日销售量对不上"),
        except AssertionError as msg2:
            print(msg2)

    def test_case3(self, e=listsevendaymoney, f=toolsevendaymoney):
        try:
            self.assertEqual(e, f, msg="品牌趋势近7天销售额对不上"),
        except AssertionError as msg3:
            print(msg3)

    def test_case4(self, g=listsevendayamount, h=toolsevendayamount):
        try:
            self.assertEqual(g, h, msg="品牌趋势近7天销售量对不上"),
        except AssertionError as msg4:
            print(msg4)

    def test_case5(self, i=listthittydaymoney, j=toolthittydaymoney):
        try:
            self.assertEqual(i, j, msg="品牌趋势近30天销售额对不上"),
        except AssertionError as msg5:
            print(msg5)

    def test_case6(self, k=listthittydayamount, l=toolthittydayamount):
        try:
            self.assertEqual(k, l, msg="品牌趋势近30天销售量对不上"),
        except AssertionError as msg6:
            print(msg6)

    def test_case7(self, m=tabledaymoney, n=listdaymoney):
        try:
            self.assertEqual(m, n, msg="品牌趋势当日销售量对不上"),
        except AssertionError as msg7:
            print(msg7)

    def test_case8(self, o=tabledayamount, p=listdayamount):
        try:
            self.assertEqual(o, p, msg="品牌趋势当日销售量对不上"),
        except AssertionError as msg8:
            print(msg8)


if __name__ == "__main__":
    unittest.main()

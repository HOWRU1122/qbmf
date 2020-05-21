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
# 关注列表
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[4]/div").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[4]/ul/li/ul/li/span").click()
sleep(5)

# 打开近7天近30天销售额销量
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label/span/span").click()
driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[2]/span/span").click()
driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[3]/span/span").click()
driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/label[4]/span/span").click()
sleep(1)

class Assert_test(unittest.TestCase):
    # 获取店铺列表数据
    listdaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[3]/td[3]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(listdaymoney)

    listsevenmoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[3]/td[7]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(listsevenmoney)

    listthirtymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[3]/td[9]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(listthirtymoney)

    listdayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[3]/td[5]/div").get_attribute(
        "textContent")
    print(listdayamount)

    listsevenamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[3]/td[8]/div").get_attribute(
        "textContent")
    print(listsevenamount)

    listthirtyamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[3]/td[10]/div").get_attribute(
        "textContent")
    print(listthirtyamount)
    # 打开店铺详情
    driver.find_element_by_xpath("//a[@title='perfectdiary旗舰店']").click()
    sleep(2)
    # 获取头部店铺数据
    tooldaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/p[2]/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(tooldaymoney)

    toolsevenmoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[1]/p[2]/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(toolsevenmoney)

    toolthirtymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/p[2]/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(toolthirtymoney)

    tooldayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/p[2]").get_attribute(
        "textContent").strip().replace(' ', '')
    print(tooldayamount)

    toolsevenamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/p[2]").get_attribute(
        "textContent").strip().replace(' ', '')
    print(toolsevenamount)

    toolthirtyamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]/p[2]").get_attribute(
        "textContent").strip().replace(' ', '')
    print(toolthirtyamount)

    # 获取表格日数据

    tabledaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(tooldaymoney)

    tabledayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[4]/div").get_attribute(
        "textContent").strip().replace(' ', '')
    print(tooldayamount)
    # 销售额销售量切换
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[2]").click()
    sleep(1)
    # 选择时间
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div[3]/div[2]/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td/div/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
    sleep(1)
    # 按月
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[2]/li[2]").click()
    sleep(1)
    # 月时间选择
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div[3]/div[2]/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr/td[2]/div/a").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr/td[4]/div/a").click()
    sleep(1)
    # 切换抖音短视频
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/a[2]").click()
    sleep(1)

    def test_case1(self, a=listdaymoney, b=tooldaymoney):
        try:
            self.assertEqual(a, b, msg="日销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=listdayamount, d=tooldayamount):
        try:
            self.assertEqual(c, d, msg="日销售量对不上"),
        except AssertionError as msg2:
            print(msg2)

    def test_case3(self, e=listsevenmoney, f=toolsevenmoney):
        try:
            self.assertEqual(e, f, msg="7日销售额对不上"),
        except AssertionError as msg3:
            print(msg3)

    def test_case4(self, g=listsevenamount, h=toolsevenamount):
        try:
            self.assertEqual(g, h, msg="7日销售量对不上"),
        except AssertionError as msg4:
            print(msg4)

    def test_case5(self, i=listthirtymoney, j=toolthirtymoney):
        try:
            self.assertEqual(i, j, msg="30日销售额对不上"),
        except AssertionError as msg5:
            print(msg5)

    def test_case6(self, k=listthirtyamount, l=toolthirtyamount):
        try:
            self.assertEqual(k, l, msg="30日销售量对不上"),
        except AssertionError as msg6:
            print(msg6)

    def test_case7(self, m=tabledaymoney, n=tooldaymoney):
        try:
            self.assertEqual(m, n, msg="30日销售额对不上"),
        except AssertionError as msg7:
            print(msg7)

    def test_case8(self, o=tabledayamount, p=tooldayamount):
        try:
            self.assertEqual(o, p, msg="30日销售量对不上"),
        except AssertionError as msg8:
            print(msg8)

    def test_case9(self, q=tabledaymoney, r=listdaymoney):
        try:
            self.assertEqual(q, r, msg="30日销售额对不上"),
        except AssertionError as msg9:
            print(msg9)

    def test_case10(self, s=tabledayamount, t=listdayamount):
        try:
            self.assertEqual(s, t, msg="30日销售量对不上"),
        except AssertionError as msg10:
            print(msg10)


if __name__ == "__main__":
    unittest.main()

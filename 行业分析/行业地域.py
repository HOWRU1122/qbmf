import unittest

from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options = webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li/ul/li/ul/li[3]").click()
sleep(1)


class Assert_test(unittest.TestCase):
    # 获取规模里的表格数据
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
        "textContent").strip().replace('w','')
    print(money)
    # 获取表格销售量
    amount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[4]/div").get_attribute(
        "textContent")
    print(amount)
    # 获取地域销表格数据
    # 按月
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[1]/div/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[2]").click()
    sleep(1)
    # 月时间选择
    driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table[3]/tbody/tr[1]/td[4]/div/a").click()
    sleep(1)
    aprilregionmoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/span").get_attribute(
        "textContent").strip().replace('w','')
    print(aprilregionmoney)
    # 获取表格销售量
    aprilregionamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[4]/div").get_attribute(
        "textContent")
    print(aprilregionamount)
    # 月时间选择
    driver.find_element_by_xpath("//input[@placeholder='选择月份']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table[3]/tbody/tr[2]/td[1]/div/a").click()
    sleep(1)
    mayregionmoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/span").get_attribute(
        "textContent").strip().replace('w','')
    print(mayregionmoney)
    # 获取表格销售量
    mayregionamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[4]/div").get_attribute(
        "textContent")
    print(mayregionamount)
    maytoolmoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/p[1]/span").get_attribute(
        "textContent").strip().replace('w','')
    print(maytoolmoney)
    # 获取表格销售量
    maytoolamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/p[1]").get_attribute(
        "textContent")
    print(maytoolamount)
    # 选择省份
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/a").click()
    sleep(1)
    driver.find_element_by_xpath("//a[@title='浙江']").click()
    sleep(1)
    # 按周
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[1]/div/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[1]").click()
    sleep(1)
    # 周时间选择
    driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[3]/td[2]/div/span").click()

    # 数据来源
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[3]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
    sleep(1)
    # 切换柱状图
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[5]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[3]/li[2]").click()
    sleep(1)
    # 切换饼图
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[7]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[3]/li[3]").click()
    sleep(1)

    # 切换地图
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[7]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[3]/li[4]").click()
    sleep(1)

    def test_case1(self, a=money, b=aprilregionmoney):
        try:
            self.assertEqual(a, b, msg="行业地域销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=amount, d=aprilregionamount):
        try:
            self.assertEqual(c, d, msg="行业地域销售量对不上"),
        except AssertionError as msg2:
            print(msg2)

    def test_case3(self, e=mayregionmoney, f=maytoolmoney):
        try:
            self.assertEqual(e, f, msg="行业地域销售额对不上"),
        except AssertionError as msg3:
            print(msg3)

    def test_case4(self, g=mayregionamount, h=maytoolamount):
        try:
            self.assertEqual(g, h, msg="行业地域销售量对不上"),
        except AssertionError as msg4:
            print(msg4)


if __name__ == "__main__":
    unittest.main()

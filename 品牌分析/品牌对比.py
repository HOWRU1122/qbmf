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
    # 打开品牌列表
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[3]/div/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[3]/ul/li/ul/li/span").click()
    sleep(5)
    # 打开趋势分析
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[6]/td[2]/div/a").click()
    sleep(3)
    # 按月
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[2]").click()
    sleep(1)
    # 选择月时间
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div[3]/div[2]/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr/td/div/a").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr/td[4]/div/a").click()
    sleep(3)
    # 获取表格数据
    tablemoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(tablemoney)
    tableamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr/td[5]/div").get_attribute(
        "textContent")
    print(tableamount)

    # 打开品牌对比
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[3]/ul/li/ul/li[2]/span").click()
    sleep(1)
    # 选择月
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/button[3]").click()
    sleep(2)
    # 选择品牌
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[2]/div/div/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[6]/span").click()
    sleep(2)
    # 获取对比数据
    tablemonthmoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[3]/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(tablemoney)
    tablemonthamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr[3]/td[2]/span").get_attribute(
        "textContent")
    print(tableamount)

    # 选择品牌
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[3]/div/div/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li[3]/span").click()
    sleep(2)
    # 选择品牌
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[4]/div/div/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[5]/div/div/ul/li[4]").click()
    sleep(2)

    # 选择周
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/button[2]").click()
    sleep(2)
    # 选择日
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/button[1]").click()
    sleep(2)
    # 清空品牌
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th/button").click()
    sleep(1)

    def test_case1(self, a=tablemoney, b=tablemonthmoney):
        try:
            self.assertEqual(a, b, msg="月销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=tableamount, d=tablemonthamount):
        try:
            self.assertEqual(c, d, msg="月销售量对不上"),
        except AssertionError as msg2:
            print(msg2)


if __name__ == "__main__":
    unittest.main()

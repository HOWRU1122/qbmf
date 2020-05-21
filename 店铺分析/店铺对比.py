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


class Assert_test(unittest.TestCase):
    # 打开店铺详情
    driver.find_element_by_xpath("//a[@title='perfectdiary旗舰店']").click()
    # 按月
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[2]").click()
    sleep(1)
    # 月时间选择
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div[3]/div[2]/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr/td[4]/div/a").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr/td[4]/div/a").click()
    sleep(1)
    # 获取表格数据
    tablemonthmoney = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(tablemonthmoney)

    tablemonthamount = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr/td[5]/div").get_attribute(
        "textContent").strip().replace(' ', '')
    print(tablemonthamount)
    # 店铺对比
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[4]/ul/li/ul/li[2]/span").click()
    sleep(1)
    # 按月
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/button[3]").click()
    sleep(2)
    # 选择店铺
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[2]/div/div/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[6]/div/span[2]").click()
    sleep(2)
    # 获取销售额销售量
    monthmoney = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr[4]/td[3]/span").get_attribute("textContent").strip().replace('w', '')
    print(monthmoney)

    monthamount = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr[5]/td[2]/span").get_attribute("textContent").strip().replace(' ', '')
    print(monthamount)
    # 选择店铺
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[3]/div/div/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li[3]/div/span[2]").click()
    sleep(2)
    # 选择店铺
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th[4]/div/div/input").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[5]/div/div/ul/li[4]/div/span[2]").click()
    sleep(2)
    # 按周
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/button[2]").click()
    sleep(2)
    # 按日
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/button[1]").click()
    sleep(2)
    # 清空店铺
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/table/thead/tr/th/button/span").click()
    sleep(1)

    def test_case1(self, a=tablemonthmoney, b=monthmoney):
        try:
            self.assertEqual(a, b, msg="月销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=tablemonthamount, d=monthamount):
        try:
            self.assertEqual(c, d, msg="月销售量对不上"),
        except AssertionError as msg2:
            print(msg2)


if __name__ == "__main__":
    unittest.main()






import unittest
from selenium.webdriver import ActionChains

from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options = webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
# 宝贝监控
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/div").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/ul/li/ul/li[3]/span").click()
sleep(3)


# 获取宝贝销量
class Assert_test(unittest.TestCase):
    # 获取表格数据
    tablemoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[8]/td[5]/div/span")
    action = ActionChains(driver)
    ActionChains(driver).move_to_element(tablemoney).perform()
    sleep(1)
    tabledaymoney = driver.find_element_by_xpath("/html/body/div[3]/div[2]").get_attribute("textContent")
    print(tabledaymoney)

    tabledayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[8]/td[6]/div").get_attribute(
        "textContent").strip().replace(' ', '')
    print(tabledayamount)
    # 查看详情
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[8]/td[10]/div/p/button/span").click()
    sleep(3)
    # 获取表格数据
    tooldaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[2]/span[2]").get_attribute(
        "textContent").strip().replace('w', '')
    print(tooldaymoney)

    tooldayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[1]/span[2]").get_attribute(
        "textContent").strip().replace(' ', '')
    print(tooldayamount)
    # 按日
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[3]/h4/div/label[2]/span").click()

    def test_case1(self, a=tabledaymoney, b=tooldaymoney):
        try:
            self.assertEqual(a, b, msg="销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=tabledayamount, d=tooldayamount):
        try:
            self.assertEqual(c, d, msg="销售量对不上"),
        except AssertionError as msg2:
            print(msg2)


if __name__ == "__main__":
    unittest.main()






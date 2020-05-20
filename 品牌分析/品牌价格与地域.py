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
sleep(5)


class Assert_test(unittest.TestCase):
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

    # 价格分析
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/a[2]").click()
    sleep(2)
    # 选择时间
    driver.find_element_by_xpath("//input[@placeholder='选择日期']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/div/span").click()
    sleep(2)
    # 销售额销售量切换
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[2]").click()
    sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li").click()
    sleep(1)
    # 选择数据来源
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[5]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/label[4]/span/span[@class='el-checkbox__inner']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li/div/div/a[@class='btn']").click()
    sleep(3)
    # 选择饼图
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[7]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[3]/li[2]").click()
    sleep(1)
    # 地域分析
    # 切换销售量
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[4]/li[2]").click()
    sleep(1)
    # 选择时间
    driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/table/tbody/tr[2]/td[5]/div").click()
    sleep(1)
    # 按月
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[4]/div/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[5]/li[2]").click()
    sleep(1)
    # 月时间选择
    driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/table/tbody/tr/td[4]/div/a").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/table/tbody/tr/td[4]/div/a").click()
    sleep(1)
    # 获取表格数据
    tabledaymoney = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/span").get_attribute(
        "textContent").strip().replace('w', '')
    print(tablemoney)
    tabledayamount = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[3]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div").get_attribute(
        "textContent")
    print(tableamount)

    # 切换数据来源
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[6]/span").click()
    sleep(1)
    driver.find_element_by_xpath(
        "/html/body/ul[6]/li/div/div[1]/label[4]/span[1]/span[@class='el-checkbox__inner']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[6]/li/div/div[2]/a[@class='btn']").click()
    sleep(1)
    # 切换饼图
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[8]/span").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/ul[7]/li[2]").click()
    sleep(1)

    def test_case1(self, a=tablemoney, b=tabledaymoney):
        try:
            self.assertEqual(a, b, msg="月销售额对不上"),
        except AssertionError as msg1:
            print(msg1)

    def test_case2(self, c=tableamount, d=tabledayamount):
        try:
            self.assertEqual(c, d, msg="月销售量对不上"),
        except AssertionError as msg2:
            print(msg2)


if __name__ == "__main__":
    unittest.main()


# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os


curpath = os.path.dirname(os.path.realpath("__file__"))
apath = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/宝贝分析/宝贝列表.py")
print(apath)

for i in range(1):
    os.system("python3 %s" % apath)

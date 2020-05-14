# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os


curpath = os.path.dirname(os.path.realpath("__file__"))
apath1 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/情报魔方循环/行业分析/行业分析循环脚本.py")
apath2 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/情报魔方循环/属性分析/属性分析循环脚本.py")
apath3 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/情报魔方循环/品牌分析/品牌分析循环脚本.py")
apath4 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/情报魔方循环/店铺分析/店铺分析循环脚本.py")
apath5 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/情报魔方循环/宝贝分析/宝贝分析循环脚本.py")

print(apath1,apath2,apath3,apath4,apath5)

l = [apath1,apath2,apath3,apath4,apath5]

for path in l:
    for i in range(1):
        os.system("python3 %s" % path)

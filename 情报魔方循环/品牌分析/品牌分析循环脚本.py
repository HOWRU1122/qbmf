# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os


curpath = os.path.dirname(os.path.realpath("__file__"))
apath1 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/品牌分析/品牌列表.py")
apath2 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/品牌分析/品牌趋势分析.py")
apath3 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/品牌分析/品牌价格与地域.py")
apath4 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/品牌分析/品牌关联分析.py")
apath5 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/品牌分析/品牌社媒流量分析.py")
apath6 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/品牌分析/品牌社媒受众分析.py")
apath7 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/品牌分析/品牌社媒达人排行.py")
apath8 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/品牌分析/品牌对比.py")

print(apath1,apath2,apath3,apath4,apath5,apath6,apath7,apath8)

l = [apath1,apath2,apath3,apath4,apath5,apath6,apath7,apath8]

for path in l:
    for i in range(1):
        os.system("python3 %s" % path)

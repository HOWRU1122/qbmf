# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os


curpath = os.path.dirname(os.path.realpath("__file__"))
apath1 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业规模.py")
apath2 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业趋势.py")
apath3 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业地域.py")
apath4 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业内容营销抖音短视频.py")
apath5 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业内容营销淘宝直播.py")
apath6 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业品牌排行.py")
apath7 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业店铺排行.py")
apath8 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业宝贝排行.py")
apath9 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业关键词排行.py")
apath10 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/行业分析/行业社媒达人排行.py")

print(apath1,apath2,apath3,apath4,apath5,apath6,apath7,apath8,apath9,apath10)

l = [apath1,apath2,apath3,apath4,apath5,apath6,apath7,apath8,apath9,apath10]

for path in l:
    for i in range(1):
        os.system("python3 %s" % path)

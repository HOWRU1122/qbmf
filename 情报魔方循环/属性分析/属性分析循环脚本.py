# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os


curpath = os.path.dirname(os.path.realpath("__file__"))
apath1 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/属性分析/属性规模分析.py")
apath2 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/属性分析/属性趋势分析.py")
apath3 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/qingbaomofang/属性分析/属性交叉分析.py")

print(apath1,apath2,apath3)

l = [apath1,apath2,apath3]

for path in l:
    for i in range(1):
        os.system("python3 %s" % path)

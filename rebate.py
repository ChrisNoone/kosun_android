# coding: utf-8

bol = int(raw_input("是否低频彩（福彩3D、排列三）：（1 - 是，0 - 否）"))
rebat = float(raw_input("输入返点："))

while 1:
    print u"\n***************分割线***************\n"
    print u"返点为：%s" % (rebat)

    a = float(raw_input("输入最低赔率："))
    b = float(raw_input("输入最高赔率："))

    if a == 0 or b == 0:
        continue;
    if bol == 1:
        bouns = (b - a) / 10 * rebat + a
    elif bol == 0:
        bouns = (b - a) / 13 * rebat + a

    print "显示赔率：%s" % bouns
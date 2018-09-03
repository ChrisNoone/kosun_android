# coding:utf-8

from appium import webdriver
from time import sleep

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "79BHADRNMSBP2",
    "appPackage": "com.prometheus.cprelease",
    "appActivity": "com.prometheus.MainActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# app启动较慢，需要等待比较久的时间
sleep(15)
# 通过元素的text文本进行定位，//* 匹配页面中总所有元素
driver.find_element_by_xpath("//*[@text='我的']").click()

from selenium import webdriver
import time
d = webdriver.Chrome()
time.sleep(2)
url = "www.baidu.com"
d.get(url)
# 这是一个测试 你猜猜 this is a test
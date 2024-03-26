from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe %s")
driver.get("http://www.ynet.co.il")
title = driver.title
driver.refresh()
if title==driver.title:
    print("equal")
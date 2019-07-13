import random
import urllib.request
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

whatToDo = input("navigate(n)")


def navigate():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.reseguiden.se/reseguider/sol-bad?page=0")
    x = 1
    while x < 21:
        driver.execute_script("window.scrollBy(0, 200);")
        x += 1
        # sleep(3)
        sleep(3)
        try:
            driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[" + str(x) + "]/a/div/div[1]").click()
            print("hittade " + str(x))
        except NoSuchElementException:
            print("hittade inte " + str(x))
        # driver.find_element_by_xpath("""//*[@id="l-i""" + str(x) + """"]""").click()
        # //*[@id="l-i2"]
        # sleep(3)
        # driver.back()
        # sleep(3)
        # driver.find_element_by_xpath("""//*[@id="articleTileList"]/div[""" + str(x) + """]/a/div[2]/div[2]""").click()
        driver.execute_script("window.scrollBy(0, 2000);")
        sleep(3)
        try:
            name = random.randrange(1, 100000)
            full_name = str(name) + ".txt"
            fh = open(full_name, 'w')
            elements = driver.find_elements_by_class_name("bb-subheader")
            for element in elements:
                print(element.text)
                fh.write(element.text)
            p = driver.find_elements_by_css_selector("p")
            for ps in p:
                print(ps.text)
                fh.write(ps.text)
            driver.back()
        except NoSuchElementException:
            sleep(3)
            # sleep(2)
            driver.back()
        # sleep(3)
    else:
        sleep(3)
        driver.find_element_by_class_name("ess_page_nav_item ess_page_nav_next").click()
        exit()


def downloadArticle(x):
    pass


if whatToDo == "n":
    navigate()

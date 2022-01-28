#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## Simple MMO
## File description:
## Main file
##

import json
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

def save_cookies():
    file = open("log.json", "w")
    json.dump(driver.get_cookies(), file)
    file.close

file = open("log.json", "r")
cookie = json.load(file)
file.close
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("https://web.simple-mmo.com/")
for i in cookie:
    driver.add_cookie(i)
driver.get("https://web.simple-mmo.com/travel")
elem = driver.find_element(By.ID, "primaryStepButton")
sleep(1)
while 1:
    elem.click()
    sleep(random.randint(1, 10))
save_cookies()

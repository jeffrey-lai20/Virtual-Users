import requests
import time
import getpass
import selenium
import time
import sys
import csv
import getpass

from selenium import webdriver

default_target = "https://0.0.0.0:8080/invalid?reason=Password%20are%20not%20matching."

def scrape(target):

    driver = webdriver.Firefox()

    print("Going to home page")
    driver.get("https://0.0.0.0:8080/")

    time.sleep(1)

    print("Going to register page")
    driver.get("https://0.0.0.0:8080/register")

    username = "test2"
    password = "test2"
    misMatchPassword = "notTheSame"

    print("Registering!")

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    # Enter confirm password
    password_field = driver.find_element_by_name("confirm_password")
    password_field.clear()
    password_field.send_keys(misMatchPassword)
    time.sleep(1)

    # Hit the button
    register_button = driver.find_element_by_name("registerButton")
    register_button.click()
    print("Registered!")

    time.sleep(1)
    driver.get(target)
    print("Arrived at target")

    time.sleep(1)
    print("Finished, closing web driver.")
    driver.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        target_url = default_target
    else:
        target_url = sys.argv[1]

    scrape(target_url)
print("Finished!")

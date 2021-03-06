import requests
import time
import getpass
import selenium
import time
import sys
import csv
import getpass

from selenium import webdriver

default_target = "https://0.0.0.0:8080/login?redirect_msg=Registered%20successfully!%20Please%20Login."

def scrape(target):

    driver = webdriver.Firefox()

    print("Going to home page")
    driver.get("https://0.0.0.0:8080/")

    time.sleep(1)

    print("Going to register page")
    driver.get("https://0.0.0.0:8080/register")

    username = "user"
    password = "user"
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
    password_field.send_keys(password)
    time.sleep(1)

    # Hit the button
    register_button = driver.find_element_by_name("registerButton")
    register_button.click()
    print("Registered!")


    username = "user"
    password = "user"
    print("Logging in")

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)

    # Hit the button
    login_button = driver.find_element_by_name("loginButton")
    login_button.click()
    print("Logged in!")

    time.sleep(1)


    driver.get("https://0.0.0.0:8080/logout")
    time.sleep(1)

    print("Going to login page")
    driver.get("https://0.0.0.0:8080/login")

    username = "staff"
    password = "staff"
    print("Logging in")

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)
    # Hit the button
    login_button = driver.find_element_by_name("loginButton")
    login_button.click()
    print("Logged in!")

    time.sleep(1)

    profile = driver.find_element_by_link_text("Profile")
    profile.click()
    time.sleep(1)

    link1 = driver.find_element_by_link_text("Manage Users")
    link1.click()
    time.sleep(1)

    driver.get("https://0.0.0.0:8080/delete/user")
    time.sleep(1)

    driver.get("https://0.0.0.0:8080/logout")
    time.sleep(1)

    driver.get("https://0.0.0.0:8080/login")
    time.sleep(1)

    username = "user"
    password = "user"
    print("Logging in")

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(1)

    # Hit the button
    login_button = driver.find_element_by_name("loginButton")
    login_button.click()
    time.sleep(1)
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

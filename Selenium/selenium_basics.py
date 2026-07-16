"""Selenium basics examples converted from a text file to a Python module.

Each function demonstrates a small Selenium task. Ensure you have:
- Selenium installed: pip install selenium
- A compatible WebDriver (e.g. chromedriver) available in PATH, or configure a Service.

Run the file directly: python Selenium/selenium_basics.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def open_example_com():
    """Open example.com and print the page title."""
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")
        print(driver.title)
    finally:
        driver.quit()


def open_python_org_print_title_and_url():
    """Open python.org and print the title and current URL."""
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.python.org")
        print(driver.title)
        print(driver.current_url)
    finally:
        driver.quit()


def print_python_introduction():
    """Open python.org and print the element with class 'introduction'."""
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.python.org")
        heading = driver.find_element(By.CLASS_NAME, "introduction")
        print(heading.text)
    finally:
        driver.quit()


def print_first_h1():
    """Open python.org and print the first h1 text."""
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.python.org")
        heading = driver.find_element(By.TAG_NAME, "h1")
        print(heading.text)
    finally:
        driver.quit()


def fill_web_form():
    """Fill example Selenium web form and print the returned message."""
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        text_box = driver.find_element(By.NAME, "my-text")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button")

        text_box.send_keys("Andriud mokosi Selenium")
        submit_button.click()

        # small pause to allow the page to update
        time.sleep(0.5)

        message = driver.find_element(By.ID, "message")
        print(message.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    # Run all examples in sequence
    open_example_com()
    open_python_org_print_title_and_url()
    print_python_introduction()
    print_first_h1()
    fill_web_form()

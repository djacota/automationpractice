from datetime import datetime
import json
import psutil
import os


from src.pages.o__general_purpose import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.ui import Select


class Browser:
    def __init__(self):
        self.my_chrome_options = webdriver.ChromeOptions()
        self.my_chrome_options.add_argument("--headless")
        self.my_chrome_options.add_argument("--window-size=1920,1080")
        self.my_chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        config_file_path = str(os.path.dirname(os.path.realpath(__package__))) + "/src/config.json"
        __json = None
        try:
            with open(config_file_path) as json_file:
                __json = json.load(json_file)
            self.my_executable_path = __json["path"]["ChromeDriver"]
            self.my_driver = webdriver.Chrome(options=self.my_chrome_options, executable_path=self.my_executable_path)
        except:
            assert False, "Browser initialising: FAILED"

    def take_screenshot(self):
        current_time = datetime.now()
        filename = '' + \
                   str(current_time.year) + \
                   str(current_time.month) + \
                   str(current_time.day) + \
                   str(current_time.hour) + \
                   str(current_time.minute) + \
                   str(current_time.second) + \
                   str(current_time.microsecond)
        self.my_driver.get_screenshot_as_file(
            str(os.path.dirname(os.path.realpath(__package__))) +
            '/output/screenshots/' +
            filename +
            '.PNG'
        )

    def click(self, xpath: str):
        locator = xpath
        driver = self.my_driver
        try:
            elem = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator))).click()
        except Exception as e:
            print(str(e))
            self.take_screenshot()

    def send_keys(self, xpath: str, keys: str, concat: str):
        driver = self.my_driver
        locator = xpath
        try:
            if concat == "-":
                elem = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator))).clear()
                elem = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator))).send_keys(keys)
            if concat == "+":
                elem = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator))).send_keys(keys)
        except Exception as e:
            print(str(e))
            self.take_screenshot()

    def click_by_webelement(self, webelement: WebElement, xpath: str):
        locator = xpath
        try:
            elem = WebDriverWait(webelement, 10).until(ec.visibility_of_element_located((By.XPATH, "." + locator))).click()
        except Exception as e:
            print(str(e))
            self.take_screenshot()

    def send_keys_by_webelement(self, webelement: WebElement, xpath: str, keys: str, concat: str):
        locator = xpath
        try:
            if concat == "-":
                elem = WebDriverWait(webelement, 10).until(ec.visibility_of_element_located((By.XPATH, "." + locator))).clear()
                elem = WebDriverWait(webelement, 10).until(ec.visibility_of_element_located((By.XPATH, "." + locator))).send_keys(keys)
            if concat == "+":
                elem = WebDriverWait(webelement, 10).until(ec.visibility_of_element_located((By.XPATH, "." + locator))).send_keys(keys)
        except Exception as e:
            print(str(e))
            self.take_screenshot()

    def find_locator_by_xpath(self, xpath: str):
        locator = xpath
        driver = self.my_driver
        try:
            elem = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator)))
            return True
        except Exception as e:
            print(str(e))
            self.take_screenshot()
            return False

    def scroll_to_element_by_xpath(self, xpath: str, wait: int):
        try:
            if self.find_locator_by_xpath(xpath):
                driver = self.my_driver
                locator = xpath
                element = driver.find_element_by_xpath(locator)
                driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center"});', element)
                import time
                time.sleep(wait)
        except:
            self.take_screenshot()

    def is_element_in_viewport(self, xpath: str):
        try:
            driver = self.my_driver
            locator = xpath
            if self.find_locator_by_xpath(locator):
                # js = """
                #     var f = (function (){
                #
                #         var isInViewport = function (elem) {
                #             var bounding = elem.getBoundingClientRect();
                #             return (
                #                 bounding.top >= 0 &&
                #                 bounding.left >= 0 &&
                #                 bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                #                 bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
                #             );
                #         };
                #
                #         var getElementByXpath = function (path) {
                #             return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                #         };
                #
                #         var obj__Article = getElementByXpath(\"""" + locator + """\");
                #
                #         return isInViewport(obj__Article);
                #     }());"""
                js = """
                    var isInViewport = function (elem) {
                        var bounding = elem.getBoundingClientRect();
                        return (
                            bounding.top >= 0 &&
                            bounding.left >= 0 &&
                            bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                            bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
                        );
                    };
        
                    var getElementByXpath = function (path) {
                        return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    };
        
                    var obj__Article = getElementByXpath(\"""" + locator + """\");
        
                    return isInViewport(obj__Article);
                """
                driver.execute_script(js)
        except:
            self.take_screenshot()

    def mouseover_element_by_xpath(self, xpath: str):
        try:
            if self.find_locator_by_xpath(xpath):
                driver = self.my_driver
                locator = xpath
                web_element = driver.find_element_by_xpath(locator)
                action = ActionChains(driver)
                action.move_to_element(web_element).perform()
        except:
            self.take_screenshot()

    def get_attribute_from(self, html_dom_element: str, xpath: str):
        try:
            if self.find_locator_by_xpath(xpath):
                elem = self.my_driver.find_element_by_xpath(xpath)
                return str(elem.get_attribute(html_dom_element)).strip().replace("""&nbsp;""", "")
            else:
                return ''
        except:
            self.take_screenshot()

    def close_driver(self):
        self.my_driver.close()
        self.my_driver.quit()

    def get_pid(self):
        p = psutil.Process(self.my_driver.service.process.pid)
        return p.pid


class Table:
    @staticmethod
    def get_table_by_xpath(driver: Browser, xpath: str):
        tbl = {}
        tbl_head = {}
        tbl_row = {}
        driver = driver.my_driver
        locator = xpath
        tbl["xpath"] = locator
        # get table head
        col_counter = 0
        elem = driver.find_elements_by_xpath(locator + '/thead/tr/th')
        for column in elem:
            tbl_head["col_" + str(col_counter)] = str(column.get_attribute(HtmlDomElement.innerHTML)).strip().replace('&nbsp;', "")
            col_counter = col_counter + 1
        tbl["head"] = tbl_head
        # get table rows
        col_num = col_counter
        row_counter = 0
        col_counter = 0
        elem = driver.find_elements_by_xpath(locator + '/tbody/tr/td')  # ../tbody/tr[3]/td[4]
        for column in elem:
            try:
                expression = locator + '/tbody/tr[' + str(row_counter + 1) + ']/td[' + str(col_counter + 1) + ']/a'
                if column.find_element_by_xpath(expression):
                    column = driver.find_element_by_xpath(expression)
                    data_ = str(column.get_attribute(HtmlDomElement.innerHTML)).strip().replace('&nbsp;', '')
                    xpath_ = locator + '/tbody/tr[' + str(row_counter + 1) + ']/td[' + str(col_counter + 1) + ']/a'
                    row_ = ("row_" + str(row_counter), "col_" + str(col_counter % col_num))
                    tbl_row[row_] = {"data": data_, "xpath": xpath_}
            except:
                data_ = str(column.get_attribute(HtmlDomElement.innerHTML)).strip().replace('&nbsp;', '')
                xpath_ = locator + '/tbody/tr[' + str(row_counter + 1) + ']/td[' + str(col_counter + 1) + ']'
                row_ = ("row_" + str(row_counter), "col_" + str(col_counter % col_num))
                tbl_row[row_] = {"data": data_, "xpath": xpath_}
            col_counter = col_counter + 1
            if col_counter == col_num:
                col_counter = 0
                row_counter = row_counter + 1
        tbl["row"] = tbl_row
        return tbl

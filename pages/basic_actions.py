import inspect

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.exception_handling import ElementNotClicked
from utilities.pytest_logger import SingletonLogger


class Basic_Actions:
    basic_wait_time = 40

    def __init__(self, driver=None):
        self.logger = SingletonLogger()
        self.logger.logger.info("basic action class is initiated with browser driver value")
        self.driver = driver
        self.wait_for_45_seconds = 45

    def type_words(self, locator, text):
        self.log_my_keyword_name_and_argument()
        element = self.driver.find_element(locator[0],locator[1])
        element.clear()
        element.send_keys()

    def click_me(self,locator,timeout = None):
        element = self.driver.find_element(locator[0], locator[1])
        if timeout is None:
            timeout = self.basic_wait_time
        clicked = False
        try:
            element.click()
            clicked = True
            self.logger.logger.info("element clicked using selenium")
        except Exception as e:
            self.logger.logger.error(f"click using webdriver is failed : {e}")

        if not clicked:
            try:

                action = ActionChains(self.driver)
                action.move_to_element(element)
                clicked = True
                self.logger.logger.info("element is clicked using mouse over actions")
            except Exception as e:
                self.logger.logger.info(f"element click using action chains is failed : {e}")
        if not clicked:
            message = f"element is not able to click ==>{str(locator)} "
            self.logger.logger.info(message)
            raise ElementNotClicked(message)

    def wait_for_objects(self,locator,timeout=None):
        self.log_my_keyword_name_and_argument()
        if timeout is None:
            timeout = self.basic_wait_time
        wait = WebDriverWait(self.driver,timeout)
        wait.until(EC.presence_of_element_located(locator))
        return True

    def wait_for_objects_ignore_error(self,locator,timeout=None):
        try:
            self.log_my_keyword_name_and_argument()
            if timeout is None:
                timeout = self.basic_wait_time
            wait = WebDriverWait(self.driver,timeout)
            wait.until(EC.presence_of_element_located(locator))
        except:
            self.logger.logger.debug(f"wait for objects ignore error ")
            pass
    def log_my_keyword_name_and_argument(self):
        """This function is used to collect the variable name and arguments to log in logging"""
        """To get the function name"""
        current_frame = inspect.currentframe()
        calling_frame = current_frame.f_back
        function_name = calling_frame.f_code.co_name
        """To get variable name in dictionary format"""
        frame = inspect.currentframe().f_back
        format_args = ""
        for key, value in frame.f_locals.items():
            if key != "self":
                format_args += str(key) + "=" + str(value) + ""
        format_args = "No arguments " if format_args == "" else format_args
        self.logger.logger.info(f"{function_name} called arguments=======>: {format_args}")

    def wait_for_object_disappear(self,locator,timeout):
        self.log_my_keyword_name_and_argument()
        WebDriverWait(self.driver,timeout).until_not(EC.presence_of_element_located(locator))

    def element_displayed(self,locator,timeout=None):
        self.log_my_keyword_name_and_argument()
        if timeout is None:
            timeout = self.basic_wait_time
        try:
            self.wait_for_objects(locator,timeout)
            return self.driver.find_element(locator[0],locator[1]).is_displayed()
        except Exception as err:
            try:
                self.scroll_into_view(locator)
                return self.driver.find_element(locator[0],locator[1]).is_displayed()
            except Exception as err:
                self.logger.logger(str(err))
                print(err)
                self.logger.debug(f"element_displayed \n called {locator} is not available in the webpage")
                return False

    def scroll_into_view(self, locator):
        pass

    def get_web_element(self, locator):
        self.log_my_keyword_name_and_argument()
        element = self.driver.find_element(locator[0],locator[1])
        return element

    def get_web_elements(self,locator):
        self.log_my_keyword_name_and_argument()
        elements = self.driver.find_elements(locator[0],locator[1])
        return elements

    def get_attribute(self, locator, attribute):
        self.log_my_keyword_name_and_argument()
        self.wait_for_objects(locator)
        if attribute == 'text':
            return self.driver.find_element(locator[0], locator[1]).text
        return self.driver.find_element(locator[0], locator[1]).value_of_css_property(attribute)

    def append_key(self,locator,text):
        self.log_my_keyword_name_and_argument()
        self.driver.find_element(locator[0], locator[1]).send_keys(Keys.END)
        self.driver.find_element(locator[0],locator[1]).send_keys(text)

    def capturescreenshot(self):
        pass

    def check_the_text_of_objects(self,locator,text_to_compare):
        self.log_my_keyword_name_and_argument()
        received_text = self.get_attribute(locator,'text')
        if received_text == "" or received_text is None:
            received_text = self.get_attribute(locator,'value')
        return text_to_compare == received_text

    def clear_field(self,locator):
        self.log_my_keyword_name_and_argument()
        element = self.driver.find_element(locator[0],locator[1])
        element.clear()

    def click_me_with_index(self,locator,pos):
        self.log_my_keyword_name_and_argument()
        elements = self.driver.find_elements(locator[0],locator[1])
        if len(elements) >= pos:
            elements[pos-1].click()
        else:
            self.logger.logger.info("position of input is greater than length")
            print("Xpath position is greater than available elements")

    def click_using_text(self,text):
        self.log_my_keyword_name_and_argument()
        if self.element_displayed((By.XPATH, "//*[text()='{}']".format(text))):
            self.logger.logger.info("element clicked by text value present in the object")
            locator = (By.XPATH,"//*[text()='{}']".format(text))
        else:
            self.logger.logger.info("element clicked by value present in the object")
            locator = (By.XPATH, "//*[@value = '{}']".format(text))
        self.click_me(locator)

    def click_using_text_by_index(self,text,pos):
        pass

    def close_current_tab(self):
        self.log_my_keyword_name_and_argument()
        self.driver.close()

    def close_browser(self):
        self.log_my_keyword_name_and_argument()
        self.driver.quit()
    """locator can't be sent to the action method directly, it has to be assigned to element"""

    def double_click(self,locator):
        self.log_my_keyword_name_and_argument()
        element = self.get_web_element(locator)
        action = ActionChains(self.driver)
        action.double_click(element).click().perform()

    def execute_script(self,script_data):
        self.log_my_keyword_name_and_argument()
        self.driver.execute_script(script_data)

    def get_css_property(self,locator, property_name):
        self.log_my_keyword_name_and_argument()
        self.wait_for_objects(locator)
        self.driver.find_element(locator[0],locator[1]).value_of_css_property(property_name)

    def get_current_url(self):
        self.log_my_keyword_name_and_argument()
        return self.driver.current_url

    def get_value_from_cookie(self):
        self.log_my_keyword_name_and_argument()
        data = self.driver.get_cookies()
        return data

    def go_to_url(self):
        pass

    def is_clickable_object(self,locator):
        self.log_my_keyword_name_and_argument()
        try:
            WebDriverWait(self.driver,self.basic_wait_time).until(EC.element_to_be_clickable(locator))
            return True
        except:
            self.logger.logger.error(f"unclickable_object")
            return False

    def is_current_url(self,url):
        self.log_my_keyword_name_and_argument()
        if self.get_current_url() == url:
            self.logger.logger.info(f"current url is same as {url} ")
            return True
        self.logger.logger.error("current url is not same as url")
        return False

    def press_home_page(self,input_field=None):
        self.log_my_keyword_name_and_argument()
        if input_field is not None:
            self.wait_for_objects(input_field)
            self.driver.find_element(input_field[0],input_field[1]).send_keys(Keys.HOME)
            self.logger.logger.info("cursor is moved to home object")
            return True
        else:
            self.logger.logger.debug("home page is key is not clicked")
            return False

    def press_page_down_key(self):
        self.log_my_keyword_name_and_argument()
        locator = (By.TAG_NAME,'body')
        self.driver.find_element(locator[0],locator[1]).send_keys(Keys.PAGE_DOWN)

    def press_page_up_key(self):
        self.log_my_keyword_name_and_argument()
        locator = (By.TAG_NAME,'body')
        self.driver.find_element(locator[0],locator[1]).send_keys(Keys.PAGE_UP)

    def page_refresh(self):
        self.log_my_keyword_name_and_argument()
        self.driver.refresh()

    def scroll_element_to_view(self,locator):
        self.log_my_keyword_name_and_argument()
        self.driver.execute_script("arguments[0].scrollIntoView(true);",self.get_web_element(locator))

    def select_default_frame(self):
        self.log_my_keyword_name_and_argument()
        self.driver.switch_to.default_content()

    def select_frame(self,locator):
        self.log_my_keyword_name_and_argument()
        element = self.driver.find_element(locator[0],locator[1])
        self.driver.switch_to.frame(element)

    def back_to_body_from_frame(self):
        self.log_my_keyword_name_and_argument()
        self.driver.switch_to.default_content()

    def select_tab_by_index(self,position):
        self.log_my_keyword_name_and_argument()
        self.driver.switch_to.window(self.driver.window_handles[position-1])

    def set_default_timeout(self,timeout):
        self.log_my_keyword_name_and_argument()
        self.basic_wait_time = timeout

    def submit_element(self,locator):
        self.log_my_keyword_name_and_argument()
        self.driver.find_element(locator[0],locator[1]).submit()

    def is_alert_appear(self):
        self.log_my_keyword_name_and_argument()
        try:
            WebDriverWait(self.driver,10).until(EC.alert_is_present())
            self.logger.logger.info("alert is appear")
            return True
        except:
            self.logger.logger.error("alert is not displayed")
            return False

    def get_alert_text(self):
        self.log_my_keyword_name_and_argument()
        if self.is_alert_appear():
            alert = self.driver.switch_to.alert
            self.logger.logger.info(f'alert text is {alert.text}')
            return alert.text
        else:
            self.logger.logger.error("alert is not displayed")
        raise AssertionError

    def accept_the_alert(self):
        self.log_my_keyword_name_and_argument()
        if self.is_alert_appear():
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            self.logger.logger.info(f"alert is accepted {alert_text}")
        else:
            self.logger.logger.info("alert is not accepted")
            raise AssertionError

    def dismiss_the_alert(self):
        self.log_my_keyword_name_and_argument()
        if self.is_alert_appear():
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.dismiss()
            self.logger.logger.info("alert is dismissed")
        else:
            self.logger.logger.error("alert is not dismissed")
            raise AssertionError

    def compare_alert_text(self, comparison_text):
        self.log_my_keyword_name_and_argument()
        if self.is_alert_appear():
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            self.logger.logger.info(f"compared output {alert_text == comparison_text}")
            return alert_text == comparison_text

    """correct the below method later"""
    def set_check_box_value(self,locator,value = True):
        self.log_my_keyword_name_and_argument()
        element = self.get_web_element(locator)
        # element.set_checked(value)
        if value != element.is_selected():
            element.click()
            self.logger.logger.info("element is selected")
        else:
            self.logger.logger.error("element is not displayed")


    def get_check_box_value(self,locator):
        self.log_my_keyword_name_and_argument()
        element = self.get_web_element(locator)
        self.logger.logger.info(f"checkbox selected status {element.is_selected}")
        return element.is_selected

    def set_radio_button(self,locator):
        self.log_my_keyword_name_and_argument()
        element = self.get_web_element(locator)
        element.click()

    def set_radio_button_value(self,locator,value = True):
        self.log_my_keyword_name_and_argument()
        element = self.get_web_element(locator)
        if value != element.is_selected:
            element.click()
            self.logger.logger.info("element is selected")
        else:
            self.logger.logger.error("element is not displayed")

    def close_tab_by_index(self,index_number):
        self.log_my_keyword_name_and_argument()
        self.select_tab_by_index(index_number)
        self.driver.close()
        self.driver.switch_to.window(self.driver.find_element[0])














































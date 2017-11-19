'''
Created on Nov 16, 2017

@author: xbolanos
@version: version 1.0 beta
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestSystem2(unittest.TestCase):
    def setUp(self):
        """
        @summary: initialize variables for the test system.
        Return
        ------
        @return: null
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_system2(self):
        """
        @summary: call with selenium some actions in the system.

        Return
        ------
        @return: null.
        """
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("ReconoceME").click()
        driver.find_element_by_id("recognizeFiles").clear()
        driver.find_element_by_id("recognizeFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/9.pgm")
        driver.find_element_by_id("recognizeFiles").submit()
        driver.find_element_by_css_selector(
            "button.swal-button.swal-button--confirm").click()

    def is_element_present(self, how, what):
        """
        @summary: validate if an element in the system is present
        Return
        ------
        @return: boolean
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        """
        @summary: validate if appears an alert
        Return
        ------
        @return: boolean
        """
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        """
        @summary: print why the system fail.

        Return
        ------
        @return: null
        """
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        """
        @summary: finish the test system

        Return
        ------
        @return: null
        """
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

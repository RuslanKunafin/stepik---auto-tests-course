from selenium import webdriver
import time
import unittest
class Testlink(unittest.TestCase):
    def test_link_1(self):
        
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.first_class > input')
        input1.send_keys('A')
        input2 = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input')
        input2.send_keys('B')    
        input3 = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.third_class > input')
        input3.send_keys('C')       
     
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
        time.sleep(1)

    
        welcome_text_elt = browser.find_element_by_tag_name("h1")
   
        welcome_text = welcome_text_elt.text

   
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
     
    def test_link_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.first_class > input')
        input1.send_keys('A')
        input2 = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input')
        input2.send_keys('B')    
        input3 = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.third_class > input')
        input3.send_keys('C')       
     
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
        time.sleep(1)

    
        welcome_text_elt = browser.find_element_by_tag_name("h1")
   
        welcome_text = welcome_text_elt.text

   
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)        
if __name__ == "__main__":
    unittest.main()
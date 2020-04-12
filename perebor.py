from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
def calc(a, b):
    return str(a+b)
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
      
    
    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text
    a=int(a)
    b=int(b)
    c=calc(a, b)
    
    print(calc(a, b))
    c=str(c)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(c).click()
    browser.find_element_by_css_selector('body>div>form>button').click()
    time.sleep(5)

finally:
     
    time.sleep(10)
     
    browser.quit()        
from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)    

    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()    
    option2 = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", option2)   
    option2.click()    
    option3 = browser.find_element_by_class_name('btn')
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", option3)  
    option3.click()
   
    

    
    time.sleep(5)

    
    

finally:
    
    time.sleep(10)
    
    browser.quit()
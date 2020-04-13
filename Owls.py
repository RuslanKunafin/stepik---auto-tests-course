import time
import pytest
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.mark.parametrize('links', ['stepik.org/lesson/236895/step/1', 'stepik.org/lesson/236897/step/1', 'stepik.org/lesson/236897/step/1', 'stepik.org/lesson/236898/step/1', 'stepik.org/lesson/236899/step/1', 'stepik.org/lesson/236903/step/1', 'stepik.org/lesson/236904/step/1', 'stepik.org/lesson/236905/step/1'])
def test_count(browser, links):
    link = f'https://{links}'
    answer = math.log(int(time.time()))
    answer=str(answer)
    
    browser.get(link)
    browser.implicitly_wait(15)
    
    input1 = browser.find_element_by_tag_name('textarea')
    input1.send_keys(answer)
    time.sleep(5)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(5)
    
    text_page = browser.find_element_by_class_name(".smart-hints__hint")
        
    assert 'Correct!' == text_page.text, "!!!TEST IS WRONG!!!"
    

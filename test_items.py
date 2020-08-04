
import time

def test_find_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(button) == 1,  "OMG! Button was stolen!"

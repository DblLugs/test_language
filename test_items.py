
from selenium.webdriver.support.ui import Select

def test_find_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(7)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("es")
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button == True,  "Караул, кнопку украли!"

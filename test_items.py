def test_alien(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(7)
    answer = math.log(int(time.time()))
    y = str(answer)
    input1 = browser.find_element_by_css_selector('[placeholder="Напишите ваш ответ здесь..."]')
    input1.send_keys(y)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    correct_name = browser.find_element_by_class_name("smart-hints__hint")
    correct = correct_name.text
    assert "Correct!" == correct, f'Не совпадает фидбек!, Выводит: {correct}.'
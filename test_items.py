import time

def test_add_to_bascet(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(3)
    browser.find_element_by_id('add_to_basket_form')
    assert len(browser.find_elements_by_id('add_to_basket_form')) == 1, "selector is not unique"
    time.sleep(30)

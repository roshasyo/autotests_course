import time
import pytest

@pytest.mark.parametrize('language', ['es', 'fr'])
def test_add_to_cart_button_exists(browser, language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Ждем 30 секунд для визуальной проверки
    time.sleep(30)

    # Проверяем наличие кнопки добавления в корзину
    button = browser.find_element("css selector", ".btn-add-to-basket")
    
    assert button is not None, "Кнопка добавления в корзину не найдена"

import pytest  # Импортируем pytest
from playwright.sync_api import Playwright, Page  # Импортируем класс страницы, будем использовать его для аннотации типов


@pytest.fixture                                                                          # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def initialize_browser_state(playwright: Playwright):
    # Открываем браузер и создаем новую страницу
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

    # Переходим на страницу входа
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

    # Заполняем поле username
        email_input = page.get_by_test_id('registration-form-username-input').locator('input')
        email_input.fill("username")

    # Заполняем поле пароль
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

    # Нажимаем на кнопку Registration
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path="browser-state.json")
        browser.close()
@pytest.fixture                                                                          # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Ниже идет инициализация и открытие новой страницы
        browser = playwright.chromium.launch(headless=False)                             # Запускаем браузер
        context = browser.new_context(storage_state="browser-state.json")                # Используем сохраненное состояние из файла json
        yield browser.new_page()                                                         # Передаем страницу для использования в тесте
        browser.close()                                                                  # Закрываем браузер после выполнения тестов


# фикстура initialize_browser_state
#
# тут код

# Эта фикстура должна регистрировать нового пользователя и сохранять состояние браузера для последующего использования.
# Код сохранения состояния браузера был ранее реализован в тесте test_empty_courses_list, но теперь его нужно вынести в фикстуру.
# Фикстура должна выполняться один раз за всю сессию тестирования.
# После выполнения фикстуры должен появиться файл browser-state.json.
# Фикстура не должна использовать autouse.
# Фикстура не должна возвращать никаких значений.

# chromium_page_with_state
#
# тут код

# вариант1
#
# @pytest.fixture(scope="function")
## scope="session": выполняется один раз за всю сессию тестирования. Используется для данных, которые нужны для всей тестовой сессии, например настройки автотестов
# def chromium_page_with_state():
# def chromium():
#     browser = new_chromium() # Открываем новое окно браузера
#     yield browser
#     browser.close()  # Закрываем окно браузера (teardown)

# # Фикстура для открытия браузера, выполняющаяся для каждого теста
# # @pytest.fixture(scope='function')
# # def browser():
# #     print("[FUNCTION] Открываем браузер на каждый автотест")



# Задание:
# Эта фикстура должна открывать новую страницу браузера, используя сохраненное состояние из файла browser-state.json.
# Фикстура должна запускаться на каждый автотест.
# Она будет использоваться для загрузки браузера с сохраненными данными (например, для авторизации).
# Данная фикстура должна использовать ранее созданную фикстуру initialize_browser_state.




from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # 2. Проверяем, что    кнопка    "Registration"    находится    в    состоянии    disabled.
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # 3. Заполнит    форму    регистрации.
    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    email_input = page.get_by_test_id('registration-form-username-input').locator('input')
    email_input.fill("username")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # 4. Убедится, что кнопка "Registration" стала доступной для взаимодействия (enabled).
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()
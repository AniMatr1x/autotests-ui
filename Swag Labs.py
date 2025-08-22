from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://www.saucedemo.com/")


    page.wait_for_timeout(5000)

    # Заполняем поле email
    email_input = page.get_by_test_id('user-name').locator('input')
    email_input.fill("standard_user")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('password').locator('input')
    password_input.fill("secret_sauce")

    # Нажимаем на кнопку Login
    login_button = page.get_by_test_id('login-button')
    login_button.click()

    # # Проверяем, что появилось сообщение об ошибке
    # wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # expect(wrong_email_or_password_alert).to_be_visible()
    # expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)
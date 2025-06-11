import pytest


@pytest.mark.parametrize('number', [1, 2, 3, -1])  # мы здесь задаем с какими параметрами должен пробежаться тест
def test_numbers(number: int):  # здесь указываем параметр
    print(f'Nubmer: {number}')
    assert number > 0


# В данном тесте мы задаем 2 параметра
@pytest.mark.parametrize('number, expected',
                         [(1, 1), (2, 4), (3, 9)])  # мы здесь задаем с какими параметрами должен пробежаться тест
def test_several_numbers(number: int, expected: int):  # здесь указываем параметр
    assert number ** 2 == expected


# В данном тесте мы списком перебираем значения
@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


# from auth_module import login
# Здесь pytest выполнит тест test_login три раза с разными значениями username и password.
@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("admin", "admin123")
])
def test_login(username, password):
    assert login(username, password) == "Success"  # login  не определен


# Иногда удобнее передавать значения в виде словарей, особенно если параметры могут изменяться:

@pytest.mark.parametrize("data", [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "admin", "password": "admin123"},
])
def test_login(data):
    assert login(data["username"], data["password"]) == "Success"  # login  не определен

    # Пишем в тесте расшифровку данных. Подписываем наши тестовые значения


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")


# Тест 5
# Здесь мы указали тестовые данные и расшифровку к ним
users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    pass

# Page Class. Этот класс должен содержать все элементы и методы, необходимые для взаимодействия с этой страницей.
# Этот класс служит обёрткой для взаимодействия с конкретной страницей.

# При использовании Page Object Model (POM)  важно правильно организовать код, чтобы он был чистым, поддерживаемым и легко расширяемым.
# Один из ключевых аспектов этого подхода — это правильная инициализация объектов страниц.
# Создадим класс для страницы логина и его конструктор. Конструктор принимает объект page, который будет использоваться для взаимодействия с элементами страницы.

from playwright.sync_api import Page


# page: Page — это аннотация типа, указывающая,
# что параметр page должен быть объектом типа Page из Playwright.
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login")
        self.error_message = page.locator("#errorAlert")

        #  Эти методы будут использовать сохраненные локаторы для выполнения действий, таких как ввод текста и нажатие кнопок.

    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto('https://zimaev.github.io/pom/')

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()

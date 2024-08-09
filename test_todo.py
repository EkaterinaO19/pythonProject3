import re
from playwright.sync_api import Playwright, sync_playwright, expect

# playwright codegen demo.playwright.dev/todomvc/#/

# Локаторы пишут на двух языках:
# XPath  //tag_name[@attribute_name ='Value of attribute']
# CSS-селекторы tagname[attribute='attribute value']
# Для того чтобы использовать селекторы  CSS и XPath в Рlaywright, реализован метод - page.locator(selector, **kwargs)

# id css: page.locator("#new-todo").click()
# id xpath: page.locator("//*[@id='new-todo']").click()

# class css: page.locator(".new-todo").click()
# xpath: page.locator("//*[@class='new-todo']").click()

#  atributes css: page.locator("[placeholder='Your email address']").click()
# x-path: page.locator("//*[@placeholder='Your email address']").click()

# Комбинация селекторов тега, класса или ID и атрибута может оказаться лучшей стратегией, чем использование только одного из данных типов селектора.
# Для достижения уникальности элемента это может стать лучшим решением.
# page/locator("input[placeholder='Your email address']").click()
# page.locator("//input[@placeholder='Your email address']").click()

# Вы также можете использовать несколько классов для поиска элемента, объединив их следующим образом:
    # page.locator("css=.first-class.another-class").click()
    # page.locator("xpath=//div[contains(@class, 'first-class') and contains(@class, 'another-class')]").click()


# Атрибут <data-testid> используется для идентификации веб-элемента специально для облегчения процесса тестирования.
# page.get_by_testid('todo-title').click()


# Поиск изображение на основе атрибута alt - page.get_by_alt_text(text, **kwargs)
# page.get_by_alt_text('logo').click()

# Поиск по его атрибуту title - page.get_by_title(text, **kwargs)
# page.get_by_title(name).fill("Anton")


# Поиск по роли ARIA(атрибутам доступности) - это новый подход к стратегии составления локаторов и поиска веб-элементов.
# Локатор page.get_by_role(role, ** kwargs) отражает то, как вспомогательные технологии(Скринридер (screen reader)) для людей с ограниченными возможностями, воспринимают страницу.
# Например, является ли какой-либо элемент кнопкой(button) или заголовком(теги h1-h6).


#     Но если вы передадите параметр exact=True, то Playwright будет искать точное совпадение. И в таком случае код приведенный ниже не сможет найти нужный элемент и вызовет ошибку.
#     page.get_by_text("switch checkbox",exact=True).click()

# Метод get_by_text()  позволяет выбирать элемент через его текстовое содержимое.  По умолчанию данный метод ищет вхождение текста, а не точное его совпадение.


# Комбинатор - это то, что определяет отношения между селекторами.
# Комбинатор потомков - представлен символом пробела (" "). Он объединяет два селектора таким образом, что элементы, соответствующие второму селектору, выбираются, если у них есть предки (родитель, родитель родителя, родитель родителя родителя и т.д.), соответствующие первому селектору.
# page.locator(".container p").click() -- все p контейнера

# Чтобы указать, что один селектор является прямым дочерним элементом другого используйте символ ( > )
# page.locator(".container > p).click() -- первый по вложенности p

# Псевдоклас в CSS — это ключевое слово, добавленное к селектору, которое определяет его особое состояние.
# Рlaywright дополняет работу с CSS  селекторами с помощью различных псевдоклассов.


# Элементы, отвечающие одному из условий
# page.locator('button:has-text("Log in"), button:has-text("Sign in")').click()
# Пример выше нажимает на элемент с тегом <button>, которая содержит текст "Log in" или "Sign in".

# Вы можете сузить запрос до n-го совпадения, используя локатор nth=
# Первый элемент page.locator("button").locator("nth=0").click()
# Последний элемент page.locator("button").locator("nth=-1").click()
# locator("td:right-of(td p:text('Software engineer'), 100)").nth(0)

# Встроенные локаторы get_by_*:   Для обеспечения стабильности своих тестов,
# get_by_text()
# page.get_by_label(text, **kwargs)
# page.get_by_placeholder(text, **kwargs)
# page.get_by_test_id('todo-title').click()
# page.get_by_alt_text('logo').click()
# page.get_by_title("username").fill("Anton")


# locator.or_
# Создает локатор, который соответствует любому из двух локаторов.
# Локатор locator.or_ используется для поиска элемента, который соответствует хотя бы одному из заданных селекторов
from playwright.sync_api import Playwright, sync_playwright
# def test_or(page):
#     selector = page.locator("input").or_(page.locator("text"))
#     selector.fill("Hello Stepik")


# locator.and_
# Локатор locator.and_ используется для поиска элемента, который соответствует всем заданным селекторам.
# page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))


# Цепочка локаторов
# Локаторы могут быть объединены в последовательность(цепь)  с помощью символа  >>
# css=article >> .baz >> css=span[attr=value]



# Фильтрация
# Для того чтобы помочь локализовать поиск,  реализован метод filter().
# Сузить поиск можно передав аргументом фильтр по тексту, по локатору или можно использовать оба способа фильтрации.
# Функция filter()  принимает несколько аргументов:
# has
# has_not
# has_text
# has_not_text
# page.locator("li").filter(has_text='Company').click()

# Явное ожидание элемента
# Если выполнение теста требует появление определенного элемента на странице,
# то вы можете указать playwright явно дождаться  элемента с помощью
# page.wait_for_selector()


# Выпадающий список
# Метод select_option() проверяет, что целевой элемент является тегом  <select>
# index - опции для выбора по индексу.В python, как и в любом языке программирования, индексы начинаются с ноля. По этому чтобы выбрать опцию - Предложил новую функцию, нужно указать индекс 1
# value - для выбора по значению атрибута value.
# label - выбор по текстовому значению

# Drag and Drop
# page.drag_and_drop(source, target, **kwargs)


# Диалоговые окна
# confirmation: page.on("dialog", lambda dialog: dialog.accept())
# Прежде чем обрабатывать какое-либо событие, необходимо подписаться на прослушивание события которе вас интересует с помощью таких методов  как - on или once (добавляет прослушиватель, который будет выполняться только один раз).
# Для отписки от событий используйте метод removeListener

# dialog.accept() - закрыть диалоговое окно нажав кнопку «OK»
# dialog.default_value - возвращает значение подсказки по умолчанию, в случае если тип диалога prompt
# dialog.dismiss() - закрыть диалоговое окно нажав кнопку «Отмена/Cancel»
# dialog.message - возвращает сообщение отображаемое в диалоговом окне.
# dialog.type - возвращает тип диалогового окна


# Загрузка файла
# Чтобы загрузить файлы хранящиеся локально на вашем ПК с помощью Playwright,
# вы должны сначала найти элемент ввода для загрузки файла и использовать метод set_input_files(), чтобы указать путь к необходимому файлу.


# Работа с несколькими вкладками(Tabs)

# Web-first assertions -  список проверок и система повтора действий вплоть до получения желаемого результата.
#expect(locator).not_to_be_checked()
#

from playwright.sync_api import Page
from playwright.sync_api import expect



def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/", wait_until='domcontentloaded')
    page.locator(".new-todo").click()
    # x-path:
    # page.locator("*//[@class='new-todo']").click()
    page.get_by_placeholder("What needs to be done?").fill("wash dishes")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_label("Toggle Todo").check()
    page.get_by_label("Delete").click()


def test_input_form(page):
    page.goto("https://zimaev.github.io/text_input/")
    page.locator("input[placeholder='email']").fill("lalal@gmail.com")
    page.get_by_title("username").fill("Ivan")
    page.get_by_placeholder("password").fill("123")
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()


def test_to_similar_buttons(page):
    page.goto("https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()


def test_locators_chain(page):
    page.goto("https://zimaev.github.io/navbar/#")
    nav_bar = page.locator("#navbarNavDropdown >> li:has-text('Company')")
    nav_bar.click()


def test_filter_method(page):
    page.goto("https://zimaev.github.io/navbar/#")
    page.locator("li").filter(has_text='Company').click()
#   page.locator('li').filter(has=page.locator('.dropdown-toggle')).click()


# отжать вс ЧБ
def test_for_cycle(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    checkbox = page.locator("input")
    for i in range(checkbox.count()):
        checkbox.nth(i).click()


# Начиная с версии playwright 1.29 появился специализированный метод locator.all() для перебора всех совпадающих элементов. Если локатор находит несколько  элементов,
# метод locator.all() возвращает массив локаторов указывающих на соответствующие элементы.
def test_locator_all(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    checkboxes = page.locator("input")
    a = []
    for checkbox in checkboxes.all():
        checkbox.check()
        a.append(checkbox)
    print(a)


def test_select(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option("#floatingSelect", value="3")
    # По умолчанию используется поиск по value. Вы можете использовать синтаксис, без явного указания стратегии поиска
    # page.select_option('#floatingSelect', "3")
    page.select_option("#floatingSelect", index=1)
    page.select_option("#floatingSelect", label="Нашел и завел bug")


def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")


def test_drag_drop(page):
    page.goto("https://www.globalsqa.com/demo-site/draganddrop/", wait_until='domcontentloaded')
    source = page.locator("img[alt='The chalet at the Green mountain lake']")
    page.drag_and_drop(source, "#trash")


def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    # page.on -  прослушивает события которые, происходит в приложении.
    # 'dialog'  -  указывает на тип события которое нужно обработать
    # lambda dialog: dialog.accept() - анонимная функция обрабатывающая событие.
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()


def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")











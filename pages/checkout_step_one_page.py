from playwright.sync_api import Page, expect


class CheckoutStepOnePage:
    def __init__(self, page: Page):
        self.page = page
        self.name = page.locator("[data-test=\"firstName\"]")
        self.lastname = page.locator("[data-test=\"firstName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("#continue")

    def fill_name(self, name):
        self.name.wait_for(state="visible")
        self.name.fill(name)

    def fill_lastname(self, lastname):
        self.lastname.fill(lastname)

    def fill_postal_code(self, postal_code):
        self.postal_code.fill(postal_code)

    def click_continue_button(self):
        self.continue_button.click()

    def get_url(self):
        return self.page.url
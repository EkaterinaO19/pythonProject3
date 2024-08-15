from playwright.sync_api import Page, expect


class StoreInventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.locator(".app_logo")
        self.logout_btn = page.locator(".logout_sidebar_link")
        self.product_name = page.locator(".inventory_item_name ")
        self.add_to_cart_btn = page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove_from_cart_btn = page.locator("#remove-sauce-labs-backpack")
        self.product_price = page.locator('.inventory_item_price')
        self.product_quantity = page.locator('.shopping_cart_badge')
        self.go_to_cart_btn = page.locator(".shopping_cart_link")
        self.burger_btn = page.locator("#react-burger-menu-btn")

    def assert_logo(self, logo_txt):
        expect(self.logo).to_have_text(logo_txt)

    def add_to_cart(self):
        self.add_to_cart_btn.wait_for(state='visible')
        self.add_to_cart_btn.click()

    def navigate_to_cart(self):
        self.go_to_cart_btn.click()

    def remove_from_cart(self):
        self.remove_from_cart_btn.click()

    def get_product_name(self):
        return self.product_name.inner_text()

    def get_product_price(self):
        return self.product_price.inner_text()

    def get_product_quantity(self):
        return self.product_quantity.inner_text()

    def get_cart_badge(self):
        return self.product_quantity.inner_text()

    def click_burger_menu(self):
        self.burger_btn.click()

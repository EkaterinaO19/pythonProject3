from playwright.sync_api import Page, expect


class StoreProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_name = page.locator(".inventory_details_name large_size")
        self.back_to_products_btn = page.locator("#back-to-products")
        self.add_to_cart_btn = page.locator("#add-to-cart")
        self.remove_btn = page.locator("#remove")

    def add_to_cart(self):
        self.add_to_cart_btn.click()

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/inventory-item.html?id=4")

    def assert_remove_btn(self):
        expect(self.remove_btn).to_be_visible()

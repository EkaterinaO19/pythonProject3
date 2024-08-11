from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_name = page.locator(".inventory_item_name")
        self.product_price = page.locator('.inventory_item_price')
        self.product_quantity = page.locator('.shopping_cart_badge')

    def get_product_name(self):
        print(self.product_name.inner_text())
        return self.product_name.inner_text()

    def get_product_price(self):
        return self.product_price.inner_text()

    def get_product_quantity(self):
        return self.product_quantity.inner_text()
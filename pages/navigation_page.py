from playwright.sync_api import Page, expect


class NavigationPage:
    def __init__(self, page: Page):
        self.page = page
        self.links = {
            "all_items": ("#inventory_sidebar_link", "https://www.saucedemo.com/inventory.html"),
            "about": ("#about_sidebar_link", "https://saucelabs.com/"),
            "logout": ("#logout_sidebar_link", "https://www.saucedemo.com/"),
            "reset": ("#reset_sidebar_link", "https://www.saucedemo.com/inventory.html/")
        }

    def navigate_and_check_url(self, link_name: str):
        locator, expected_url = self.links[link_name]
        self.page.locator(locator).click()
        expect(self.page).to_have_url(expected_url)
        if link_name != "about":
            self.page.go_back()

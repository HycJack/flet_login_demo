import flet as ft

class ThemeButton(ft.IconButton):
    def __init__(self, page, text="Dark", icon=ft.Icons.DARK_MODE_OUTLINED):
        self.page = page
        super().__init__(icon)
        self.on_click = lambda e: self.theme_change_click()

    def theme_change_click(self):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            # self.text = "Light"
            self.icon = ft.Icons.WB_SUNNY_OUTLINED
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            # self.text = "Dark"
            self.icon = ft.Icons.DARK_MODE_OUTLINED
        self.page.update()
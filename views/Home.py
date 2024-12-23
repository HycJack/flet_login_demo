import flet as ft

from components.theme_btn import ThemeButton

class HomeView(ft.View):
    def __init__(self , page: ft.Page) -> None:
        super().__init__(
            route="/home",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.title = "Home"

    def build(self):
        self.controls.clear()
        self.create_app_header()
        self.container = ft.Container(expand=True, content=ft.Column(controls=[]))
        self.container.content = ft.Column(controls=[ft.Text("Text2Text!", size=34, weight=ft.FontWeight.BOLD)])
        
        self.rail = self.create_sider()
        
        self.controls.append(
            ft.Row(
                [
                    self.rail,
                    ft.VerticalDivider(width=1),
                    self.container
                ],
                expand=True,
            )
        )

    def change_main(self, index):
        if index == 0:
            self.container.content = ft.Column(controls=[ft.Text("Text2Text!", size=34, weight=ft.FontWeight.BOLD)])
        elif index == 1:
            self.container.content = ft.Column(controls=[ft.Text("Text2Image!", size=34, weight=ft.FontWeight.BOLD)])
        elif index == 2:
            self.container.content = ft.Column(controls=[ft.Text("Settings", size=34, weight=ft.FontWeight.BOLD)])
        else:
            self.container.content = ft.Column(controls=[ft.Text("Hello, 11111!")])
        
        self.update()

    def create_app_header(self):
        theme_change_button = ThemeButton(self.page)
        btn_logout = ft.IconButton(icon=ft.Icons.LOGOUT_OUTLINED, tooltip="Logout", on_click=lambda e: self.page.go("/"))
        print("Login user name: ")
        print(self.page.session.get("user_name"))
        if self.page.session.get("user_name"):
            text_user = ft.Text(f'欢迎 {self.page.session.get("user_name")}！', size=15, weight=ft.FontWeight.W_600, text_align=ft.TextAlign.CENTER)
        else:
            text_user = ft.Text('请登录以访问系统！', size=15, weight=ft.FontWeight.W_600)

        bar = ft.AppBar(
            elevation=10,
            leading_width=180,
            bgcolor=ft.Colors.PRIMARY_CONTAINER,
            actions=[
                ft.Container(
                    padding=18,
                    content=ft.Column(
                        # alignment=ft.VerticalAlignment.CENTER,
                        # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            text_user
                        ],
                    ),
                ),
                theme_change_button,
                btn_logout,
            ],
        )
        self.navigation_bar = bar

    def create_sider(self):
        rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icons.CHAT_OUTLINED,
                    selected_icon=ft.Icons.CHAT,
                    label="Text2Text"
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icon(ft.Icons.IMAGE_OUTLINED),
                    selected_icon=ft.Icon(ft.Icons.IMAGE),
                    label="Text2Image",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),
            ],
            on_change=lambda e: self.change_main(e.control.selected_index),
        )
        return rail
    

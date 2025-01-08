import flet as ft

from components.theme_btn import ThemeButton


class AnimatedBox(ft.Container):
    def __init__(self, border_color, bg_color, rotate_angle):
        super().__init__(
            width=48,
            height=48,
            border=ft.border.all(2.5, border_color),
            bgcolor=bg_color,
            border_radius=2,
            rotate=ft.transform.Rotate(rotate_angle, ft.alignment.center),
            animate_rotation=ft.animation.Animation(700, "easeInOut"),
        )
        
class LoginView(ft.View):
    def __init__(self , page: ft.Page) -> None:
        super().__init__(
            route="/",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page=page
        self.page.on_keyboard_event = self.on_key_down

    def build(self):
        self.title = "Login Page"
        # Username input field
        self.username = ft.TextField(icon=ft.Icons.PERSON_ROUNDED, label="Username", width=300)

        # Password input field
        self.password = ft.TextField(icon=ft.Icons.LOCK, label="Password", 
                                     password=True, can_reveal_password=True, width=300)
        
        # Password input field
        self.repeat_password = ft.TextField(icon=ft.Icons.LOCK, label="Repeat Your Password", 
                                     password=True, can_reveal_password=True, width=300)

        # Login button
        self.login_button = ft.ElevatedButton(
                content=ft.Text(
                    'Sign In',
                    size=13,
                    color="white",
                    weight="bold",
                ),
                style=ft.ButtonStyle(
                    shape={
                        "": ft.RoundedRectangleBorder(radius=8),
                    },
                    
                    bgcolor={"": "black"},
                ),
                height=42,
                width=320,
                on_click=self.on_login_click,
            )
        
        self.register_button = ft.ElevatedButton(
                content=ft.Text(
                    'Sign Up',
                    size=13,
                    color="white",
                    weight="bold",
                ),
                style=ft.ButtonStyle(
                    shape={
                        "": ft.RoundedRectangleBorder(radius=8),
                    },
                    
                    bgcolor={"": "black"},
                ),
                height=42,
                width=320,
                on_click=self.on_login_click,
            )
        self.login_card = ft.Card(
            width=408,
            # height=612,
            elevation=15,
            content=ft.Container(
                border_radius=6,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[ThemeButton(self.page)]
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                ft.Text("Sign In", size=22, weight="bold"),
                                
                            ],
                        ),
                        ft.Divider(height=30, color="transparent"),
                        self.username,
                        ft.Divider(height=1, color="transparent"),
                        self.password,
                        # ft.Divider(height=1, color="transparent"),
                        # ft.Row(
                        #     width=320,
                        #     alignment=ft.MainAxisAlignment.END,
                        #     controls=[
                        #         ft.Container(
                        #             content=ft.Text("Forgot Passowrd?", size=14),
                        #         )
                        #     ],
                        # ),
                        ft.Divider(height=45, color="transparent"),
                        self.login_button,
                        ft.TextButton("Don't have an account? Register", on_click=self.show),
                        ft.Divider(height=35, color="transparent"),
                    ],
                ),
            ),
        )
        self.register_card = ft.Card(
            width=408,
            # height=612,
            elevation=15,
            content=ft.Container(
                border_radius=6,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[ThemeButton(self.page)]
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                ft.Text("Sign Up", size=22, weight="bold"),
                                
                            ],
                        ),
                        ft.Divider(height=30, color="transparent"),
                        self.username,
                        ft.Divider(height=1, color="transparent"),
                        self.password,
                        ft.Divider(height=1, color="transparent"),
                        self.repeat_password,
                        ft.Divider(height=45, color="transparent"),
                        self.register_button,
                        ft.TextButton("Already have an account, Login", on_click=self.show),
                        ft.Divider(height=35, color="transparent"),
                    ],
                ),
            ),
        )
        self.controls.clear()
        self.controls.append(
            self.login_card
        )
        def handle_close(e):
            self.page.close(self.dlg_modal)
            self.page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Please input user name and password!"),
            actions=[
                ft.TextButton("Yes", on_click=handle_close),
                ft.TextButton("No", on_click=handle_close),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: self.page.add(
                ft.Text("Modal dialog dismissed"),
            ),
        )
        

    def on_key_down(self, e: ft.KeyboardEvent):
        # print(e.ctrl)
        # if e.ctrl:
            if e.key == "Enter":
                self.login_button.on_click(None)

    def on_login_click(self, e):
        # Handle login logic here
        if self.username.value == "" or  self.username.value  is None or self.password.value == "" or  self.password.value  is None :
            self.page.open(self.dlg_modal)
        if self.username.value == "admin" and self.password.value == "password":
            self.page.session.set("user_name", self.username.value)
            print(self.page.session.get("user_name"))
            self.page.go("/home")
        else:
            snack_bar = ft.SnackBar(ft.Text("Invalid username or password"), open=True)
            self.page.overlay.append(snack_bar)
        self.page.update()

    def show(self, e):
        """
        Navigates to the registration.
        """
        print(self.controls[0])
        if self.controls[0] == self.login_card:
            self.controls.clear()
            self.controls.append(
                self.register_card
            )
        else:
            self.controls.clear()
            self.controls.append(
                self.login_card
            )
        self.page.update()
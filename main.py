import math
import flet as ft
from views.Home import HomeView
from views.Login import LoginView


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = ft.padding.only(right=50)
    page.title = "AI Chat UI"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    routes = {
        "/": LoginView(page),
        "/home": HomeView(page),
    }
    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()
        page.views.append(
            routes[
                page.route
                if page.route in list(routes.keys()) 
                else "/"
            ]
        )
        page.update()
    
    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views.pop()
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)    

ft.app(target=main, assets_dir="assets")
import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"
    navigation_bar=ft.NavigationBar(
                                    destinations=[
                                        ft.NavigationDestination(icon_content=ft.Icon(name=ft.icons.APPS, color="white"),selected_icon_content=None),
                                        ft.NavigationDestination(icon_content=ft.Icon(name=ft.icons.HOME, color="white")),
                                        ft.NavigationDestination(icon_content=ft.Icon(name=ft.icons.CHAT, color="white"))
                                    ],
                                    bgcolor="#c55b36",
                                )
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    navigation_bar,
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),

                ],
                
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
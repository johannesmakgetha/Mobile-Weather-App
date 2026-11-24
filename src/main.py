import flet as ft
from pages.home import home_page
from pages.search import search_page
from pages.about import about_page
import uuid



async def main(page: ft.Page):
    page.bgcolor = ft.Colors.LIGHT_BLUE_600
    page.padding = 0
    page.spacing = 0
    page.theme = ft.Theme(
    system_overlay_style=ft.SystemOverlayStyle(

        system_navigation_bar_color=ft.Colors.LIGHT_BLUE_600,
        system_navigation_bar_divider_color=ft.Colors.LIGHT_BLUE_600,

        status_bar_icon_brightness=ft.Brightness.LIGHT,
        system_navigation_bar_icon_brightness=ft.Brightness.LIGHT,
        
        enforce_system_navigation_bar_contrast=False,
        enforce_system_status_bar_contrast=False,
        )
    )

    prefs = ft.SharedPreferences()
    page.services.append(prefs)

    user_id = await prefs.get("anonymous_user_id")

    if not user_id:
        user_id = str(uuid.uuid4())
        await prefs.set("anonymous_user_id", user_id)

    def route_change():
        page.views.clear()

        if page.route == "/":
            page.views.append(home_page(page,prefs,user_id))
        elif page.route == "/home":
            page.views.append(home_page(page,prefs,user_id))
        elif page.route == "/search":
            page.views.append(search_page(page,prefs,user_id))
        elif page.route == "/about":
            page.views.append(about_page(page))

        page.update()

    page.on_route_change = route_change
    route_change()
    # page.add(home_page(page))


if __name__ == "__main__":
    ft.run(main)

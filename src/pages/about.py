import flet as ft


def about_page(page: ft.Page) -> ft.View:

    async def go_to_home(e):
        await page.push_route('/home')
    
    app_bar = ft.AppBar(
    
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=go_to_home
                
            ),
            bgcolor=ft.Colors.BLACK,
            title="About",
            center_title=True,
            elevation= 4,
            shadow_color=ft.Colors.WHITE,
            title_text_style=ft.TextStyle(
                size = 20,
                color=ft.Colors.WHITE,
                weight=ft.FontWeight.BOLD
            ),
            
            )
    

    def open_info_dialog(page, title, message):
        dialog = ft.AlertDialog(
            
            title=ft.Text(
                title,
                color="#ffffff",
                weight=ft.FontWeight.BOLD,
            ),
            content=ft.Container(
                width=350,
                content=ft.Text(
                    message,
                    color="#cccccc",
                    selectable=True,
                ),
            ),
            bgcolor="#111820",
            shape=ft.RoundedRectangleBorder(radius=16),
            actions=[
                ft.TextButton(
                    "Close",
                    on_click=lambda e: page.pop_dialog(),
                ),
            ],
            )
        page.show_dialog(dialog)
    

    loading_info_container = ft.Container(
            padding=16,
            border=ft.Border.all(1, "#35414a"),
            border_radius=16,
            bgcolor="#111820",
            on_click=lambda e: open_info_dialog(
                page,
                "App Loading Information",
                "Please Note: The Backend May Take a Moment to Wake Up\n\n"
                "The app's backend is hosted online. When it is inactive "
                "for a while, the hosting service may put it to sleep. "
                "The first request after this may take longer than usual "
                "or fail.\n\n"
                "If the app does not load, please try the following:\n\n"
                "1. Home Screen (Weather Display)\n"
                "- Pull down to refresh the weather.\n"
                "- Please try refreshing at least 4 times, waiting for "
                "each loading attempt to finish before trying again.\n\n"
                "2. Search Page\n"
                "- Enter the city name and press Search.\n"
                "- If the search does not work, wait for the loading "
                "attempt to finish and press Search again.\n"
                "- Please try at least 3 times.\n\n"
                "Thank you for your patience and understanding!"
            ),
            content=ft.Row(
                controls=[
                    ft.Icon(
                        ft.Icons.REFRESH_ROUNDED,
                        color="#8DD8E8",
                        size=26,
                    ),
                    ft.Column(
                        expand=True,
                        spacing=5,
                        controls=[
                            ft.Text(
                                "App Loading Information",
                                color="#ffffff",
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                "Troubleshooting loading and search issues",
                                color="#aaaaaa",
                                size=12,
                            ),
                        ],
                    ),
                    ft.Icon(
                        ft.Icons.CHEVRON_RIGHT,
                        color="#aaaaaa",
                    ),
                ],
            ),
        )





    disclaimer_container = ft.Container(
        padding=16,
        border=ft.Border.all(1, "#35414a"),
        border_radius=16,
        bgcolor="#111820",
        on_click=lambda e: open_info_dialog(
        page,
        "Weather Disclaimer",
        "Weather forecasts are estimates based on available weather data.\n\n"
        "Actual weather conditions may differ.\n\n"
        "Do not rely solely on this application for emergency alerts or "
        "safety-critical decisions."
        ),
        content=ft.Row(
            controls=[
                ft.Icon(
                    ft.Icons.HELP_OUTLINE,
                    color="#8DD8E8",
                    size=26,
                ),
                ft.Column(
                    expand=True,
                    spacing=5,
                    controls=[
                        ft.Text(
                            "Weather Disclaimer",
                            color="#ffffff",
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Forecasts are estimates and may change",
                            color="#aaaaaa",
                            size=12,
                        ),
                    ],
                ),
                ft.Icon(
                    ft.Icons.CHEVRON_RIGHT,
                    color="#aaaaaa",
                ),
            ],
        ),
    )

    support_container = ft.Container(
    padding=16,
    border=ft.Border.all(1, "#35414a"),
    border_radius=16,
    bgcolor="#111820",
    on_click=lambda e: open_info_dialog(
        page,
        "Contanct & Support",
        "Have a question, suggestion or encountered a problem?\n\n"
        "We'd love to hear from you.\n\n"
        "makgethamj@gmail.com ",
    ),
    content=ft.Row(
        controls=[
            ft.Icon(
                ft.Icons.DESCRIPTION_OUTLINED,
                color="#8DD8E8",
                size=26,
            ),
            ft.Column(
                expand=True,
                spacing=5,
                controls=[
                    ft.Text(
                        "Contact & Support",
                        color="#ffffff",
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Encountered a problem?",
                        color="#aaaaaa",
                        size=12,
                    ),
                ],
            ),
            ft.Icon(
                ft.Icons.CHEVRON_RIGHT,
                color="#aaaaaa",
            ),
        ],
    ),
)


    privacy_container = ft.Container(
    padding=16,
    border=ft.Border.all(1, "#35414a"),
    border_radius=16,
    bgcolor="#111820",
    on_click=lambda e: open_info_dialog(
    page,
    "Privacy & Data",
    "Your privacy matters.\n\n"
    "Your saved locations are stored locally on your device. "
    "They are used to remember your preferred locations "
    "and provide weather information.\n\n"
    "Your location preferences are not shared with other users. ",
),
    content=ft.Row(
        controls=[
            ft.Icon(
                ft.Icons.SHIELD_OUTLINED,
                color="#8DD8E8",
                size=26,
            ),
            ft.Column(
                expand=True,
                spacing=5,
                controls=[
                    ft.Text(
                        "Privacy & Data",
                        color="#ffffff",
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Learn how your data is handled",
                        color="#aaaaaa",
                        size=12,
                    ),
                ],
            ),
            ft.Icon(
                ft.Icons.CHEVRON_RIGHT,
                color="#aaaaaa",
            ),
        ],
    ),
)
    version_details = ft.Container(
    alignment=ft.Alignment.CENTER,
    padding=ft.Padding(10, 20, 10, 10),
    content=ft.Text(
        "Ski-cast • Version 1.0.0",
        size=12,
        color="#8A949E",
        text_align=ft.TextAlign.CENTER,
    ),
)


    return ft.View(
        appbar=app_bar,
        route="/about",
        bgcolor="#090e12",
        controls=[
            ft.Container(
                padding=ft.Padding(0,15,0,0),

                expand=True,
                content=ft.SafeArea(
                    avoid_intrusions_left=False,
                    avoid_intrusions_right=False,
                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            loading_info_container,
                            disclaimer_container,
                            privacy_container,
                            support_container,
                            version_details
                        ],
                        expand=True,
                        spacing=10,
                    ),
                    expand=True,
                ),
            )
        ],
      
        padding=5,
    )
    

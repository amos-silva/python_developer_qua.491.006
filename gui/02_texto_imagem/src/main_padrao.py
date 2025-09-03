import flet as ft

def main(page: ft.Page):

    page.add(
        ft.SafeArea(
            ft.Container(),
            expand=True,
        )
    )

ft.app(main)

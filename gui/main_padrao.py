import flet as ft

def main(page: ft.Page):

    # propriedades da pagina
    page.title = "Teste"                  # titulo da janela do programa
    page.scroll = "adaptive"                # coloca a janela em tamanho adaptavel
    page.theme_mode = ft.ThemeMode.LIGHT    # colocar o tema CLARO


    page.add(
        ft.SafeArea(
            ft.Container(

                alignment=ft.alignment.center

            ),            
            expand=True
        )
    )

ft.app(main)
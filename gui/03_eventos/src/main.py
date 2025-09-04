import flet as ft

def main(page: ft.Page):

    def exibir_texto(e):
        result.value = texto.value
        page.update()

    # propriedades da pagina
    page.title = "Eventos"                  # titulo da janela do programa
    page.scroll = "adaptive"                # coloca a janela em tamanho adaptavel
    page.theme_mode = ft.ThemeMode.LIGHT    # colocar o tema CLARO

    #Variaveis
    texto = ft.TextField(label="Digite o seu Texto aqui")   # Caixa de texto
    result = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(    
                ft.Text("App Eventos", size=30, weight="bold"),
                alignment=ft.alignment.center,

            ),
            expand=True,
        ),
        texto,
        ft.ElevatedButton("Enviar", on_click=exibir_texto),
        result
    )

ft.app(main)

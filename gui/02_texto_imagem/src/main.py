import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro App em Janela - Flet"    ## Titulo da janela
    page.scroll = "adaptive"        ## adaptar a imagem à janela

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column([
                    ft.Text("Olá mundo - Flat Python , aqui é o texto principal", size=40),
                    ft.Text("🐍🤣🤣🤣🐍", size=30)
                ]

                )
                
            ),
            expand=True,
        ),
        ft.Text("🎆🎆Aqui é uma estrutura fora do SafeArea, para as demais estruturas da janela🎆🎆", size=20),
        ft.Image(
            src="imagem.jpg",
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("Erro ao carregar a imagem"),
            width=600       ## tamanho da imagem
        )
        
    )

ft.app(main)

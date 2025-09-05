import flet as ft

def main(page: ft.Page):

    # Função do evento
    def calcular_imc (e):
        if not peso.value:
            peso.error_text = "Digite um Peso"
            page.update()
        else:
            peso.error = ""
            page.update()

        if not altura.value:
            altura.error_text = "Digite uma Altura"
            page.update()
        else:
            altura.error = ""

            # Recebe os inputs
            peso.value = float(peso.value.replace(",","."))
            altura.value = float(altura.value.replace(",","."))

            #Calcula IMC
            imc = peso.value / (altura.value**2)

            # Exibe o valor d IMC
            caixa_modal.title.value = f"Seu IMC é:  {imc:.2f}"      # Caixa que exibe o resultados

            # Diagnostico do IMC
            if imc < 18.5:
                caixa_modal.content.value = "Você está abaixo do peso"
            elif imc < 25:
                caixa_modal.content.value = "Você está no peso ideal",
            elif imc < 30:
                caixa_modal.content.value = "Você está acima do peso"
            elif imc < 35:
                caixa_modal.content.value = "Você está obeso"
            elif imc < 40:
                caixa_modal.content.value = "Você está com obesidade nível 2"
            else:
                caixa_modal.content.value = "Você está com obesidade Mórbita"

            # abre o modal
            page.open(caixa_modal)

            #limpa os campos par aproxima execução
            peso.value = ""
            altura.value = ""


            page.update()


    # propriedades da pagina
    page.title = "IMC - Indice de Massa Corporal"   # titulo da janela do programa
    page.scroll = "adaptive"                        # coloca a janela em tamanho adaptavel
    page.theme_mode = ft.ThemeMode.LIGHT            # colocar o tema CLARO

    # Variaveis
    peso = ft.TextField(label="Peso", suffix_text=" kg")
    altura = ft.TextField(label="Altura", suffix_text=" metros", on_submit=calcular_imc)    # on submit para ativar o ENTER na função

    # Caixa de Dialogo
    caixa_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(caixa_modal))],     # comando para dar um OK e fechar a janela
        actions_alignment=ft.MainAxisAlignment.END      # Alinhamento da Caixa
    )

    # Conteudo da Pagina / Janela
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Indice de massa Corporal",size=30, weight="bold"),

                alignment=ft.alignment.center

            ),            
            expand=True
        ),
        ft.ResponsiveRow(
            [
                ft.Container(peso, col={"sm":6, "md":4, "xl":2}),   # Tamanhos de tela
                ft.Container(altura, col={"sm":6, "md":4, "xl":2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Calcular ICM", on_click=calcular_imc),
                    padding=30  # Espaçamento do botão
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    )

ft.app(main)
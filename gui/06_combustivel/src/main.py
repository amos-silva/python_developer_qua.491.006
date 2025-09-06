import flet as ft

def main(page: ft.Page):

    # Função chamada ao clicar no botão
    def calcular_combustivel(e):
        try:
            gasolina = float(gasolina_input.value.replace(",", "."))
            etanol = float(etanol_input.value.replace(",", "."))
            calculo = (etanol / gasolina) * 100
            melhor = "Gasolina" if calculo > 70 else "Etanol"
            resultado_texto.value = f"Melhor abastecer com: {melhor} ({calculo:.2f}%)"
        except:
            resultado_texto.value = "Erro: insira valores válidos para os combustíveis."

        page.update()


    # Propriedades da página
    page.title = "Abastecer"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de entrada
    gasolina_input = ft.TextField(label="Valor da gasolina (R$)", width=200)
    etanol_input = ft.TextField(label="Valor do etanol (R$)", width=200, on_submit=calcular_combustivel)
    resultado_texto = ft.Text(size=20)

    
    # Adicionando os elementos à página
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Melhor Combustível para Abastecer", size=30),
                alignment=ft.alignment.center,
                padding=20
            ),
            expand=True
        ),
        ft.ResponsiveRow(
            [
                gasolina_input,
                etanol_input
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.ElevatedButton("Calcular", on_click=calcular_combustivel)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                resultado_texto
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)

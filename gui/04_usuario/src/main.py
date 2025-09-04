import flet as ft
from dataclasses import dataclass


# classe Pessoa
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    salario: float
    email: str

def main(page: ft.Page):

    # função do evento
    def mostrar_dados(e):
        saida_titulo.value = "Dados do Usuário\n"
        nome.value = f"Nome: {usuario.nome.value}"
        idade.value = f"Idade: {usuario.idade.value}"
        peso.value = f"Peso: {usuario.peso.value} Kg"
        salario.value = f"Salario: R$ {usuario.salario.value}"
        email.value = f"Email: {usuario.email.value}"

        page.update()


    # Instancia do usuario
    usuario = Pessoa(nome="", idade=0, peso=0.0, salario=0.0, email="")

    # propriedades da pagina
    page.title = "Dados do Usuário"         # titulo da janela do programa
    page.scroll = "adaptive"                # coloca a janela em tamanho adaptavel
    page.theme_mode = ft.ThemeMode.LIGHT    # colocar o tema CLARO


    # Setar os valor do usuario
    usuario.nome = ft.TextField(label="Nome")
    usuario.idade = ft.TextField(label="Idade", suffix_text=" anos")
    usuario.peso = ft.TextField(label="Peso", suffix_text="Kg ")
    usuario.salario = ft.TextField(label="Salario", prefix_text="R$ ")
    usuario.email = ft.TextField(label="Email", on_submit=mostrar_dados)    # on_submit = dar ENTER para salvar

    # Variaveis de saida
    saida_titulo = ft.Text(weight="bold")
    nome = ft.Text()
    idade = ft.Text()
    peso = ft.Text()
    salario = ft.Text()
    email = ft.Text()


    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Dados do Usuario", size=30, weight="bold"),
                alignment=ft.alignment.center,

            ),            
            expand=True,
        ),
        usuario.nome,
        usuario.idade,
        usuario.peso,
        usuario.salario,
        usuario.email,
        ft.ElevatedButton("Enviar",on_click=mostrar_dados),
        saida_titulo,
        nome,
        idade,
        peso,
        salario,
        email

    )

ft.app(main)

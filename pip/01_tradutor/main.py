from deep_translator import GoogleTranslator
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    tradutor = GoogleTranslator(source="auto", target="pt")
    limpar()

    while True:
        try:
            print("Tradutor")
            print("1 - Traduzir")
            print("2 - SAIR")
            opcao = input("Informe a opção desejada: ").strip()

            match opcao:
                case "1":
                    texto_original = input("Digite o texto para Traduzir: \n")
                    texto_traduzido = tradutor.translate(texto_original)

                    print(f"\nTexto Traduzido:\n{texto_traduzido}\n")

                case "2":
                    print("Programa encerrado.")
                    break
                case _:
                    print("Opção inválida!")
                    continue

        except Exception as e:
            print(f"Não foi possivel traduzir. {e}")
            continue
        

if __name__ == "__main__":
    main()
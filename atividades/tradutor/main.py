from deep_translator import GoogleTranslator
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    tradutor = GoogleTranslator(source="auto", target="pt")
    limpar()

    while True:
        try:
            print("Tradutor")
            print("1 - Digitar um texto Traduzir")
            print("2 - Importar um Arquivo para Traduzir")
            print("3 - SAIR")
            opcao = input("Informe a opção desejada: ").strip()

            match opcao:
                case "1":
                    texto_original = input("Digite o texto para Traduzir: \n")
                    texto_traduzido = tradutor.translate(texto_original)

                    print(f"\nTexto Traduzido:\n{texto_traduzido}\n")

                case "2":
                  
                    caminho = input("Digite o nome do Arquivo para Traduzir: \n").strip().lower()
            
                    # Abre o arquivo em modo leitura
                    with open(caminho, 'r', encoding='utf-8') as arquivo:
                        conteudo = arquivo.read()
                        print("Conteúdo do arquivo:")
                        print(conteudo)                        
                case "3":
                    print("SAIR.")
                    continue
                case _:
                    print("Opção inválida!")
                    continue

        except Exception as e:
            print(f"Não foi possivel traduzir. {e}")
            continue
        

if __name__ == "__main__":
    main()
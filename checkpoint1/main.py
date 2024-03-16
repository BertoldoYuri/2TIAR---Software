import subprocess
from checkpoint1 import CriandoAlgoritmo

def main():
    # Solicitar ao usuário para inserir o comando da aplicação
    comando = input("Digite uma frase ou um texto: ")

    # Executar o comando usando subprocess
    try:
        CriandoAlgoritmo().analisando_texto(comando)
    except Exception as e:
        print(f"Ocorreu um erro ao executar a aplicação: {e}")

if __name__ == "__main__":
    main()
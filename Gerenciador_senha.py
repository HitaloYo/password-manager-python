import random

# Definindo os tipos de caracteres
min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'

# Função para gerar senha aleatória
def gerar_senha(completa, tamanho):
    return ''.join(random.choice(completa) for _ in range(tamanho))

# Função para validar entrada
def validar_entrada():
    while True:
        try:
            qnt = int(input('Digite o tamanho da senha: '))
            if qnt <= 0:
                print("O tamanho da senha deve ser maior que 0.")
            else:
                return qnt
        except ValueError:
            print("Por favor, insira um número válido.")

# Menu de opções
def menu():
    print("Escolha o tipo de senha a ser gerada:")
    print("1 - Senha completa (minúsculas, maiúsculas, números e símbolos)")
    print("2 - Senha com maiúsculas e números")
    print("3 - Senha com minúsculas e maiúsculas")
    print("4 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    return opcao

# Gerar senhas com base na opção escolhida
def gerar_senhas(opcao, tamanho):
    if opcao == '1':
        senha = gerar_senha(min + max + num + sybs, tamanho)
        print("Senha completa: ", senha)
    elif opcao == '2':
        senha = gerar_senha(max + num, tamanho)
        print("Senha maiúsculas e números: ", senha)
    elif opcao == '3':
        senha = gerar_senha(min + max, tamanho)
        print("Senha minúsculas e maiúsculas: ", senha)
    else:
        print("Opção inválida. Tente novamente.")

# Execução principal
def main():
    tamanho = validar_entrada()
    
    while True:
        opcao = menu()
        if opcao == '4':
            print("Saindo...")
            break
        gerar_senhas(opcao, tamanho)

if __name__ == "__main__":
    main()

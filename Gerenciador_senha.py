"""Gerador de senhas no terminal.

Usa o módulo `secrets`, feito para gerar valores imprevisíveis (o `random`
não serve para senhas: a sequência dele pode ser prevista).
"""
import secrets
import string

MINUSCULAS = string.ascii_lowercase
MAIUSCULAS = string.ascii_uppercase
NUMEROS = string.digits
SIMBOLOS = '[]{}()*#;/,-_%'

TIPOS = {
    '1': ('Senha completa', [MINUSCULAS, MAIUSCULAS, NUMEROS, SIMBOLOS]),
    '2': ('Senha com maiúsculas e números', [MAIUSCULAS, NUMEROS]),
    '3': ('Senha com minúsculas e maiúsculas', [MINUSCULAS, MAIUSCULAS]),
}


def gerar_senha(grupos, tamanho):
    """Gera a senha garantindo pelo menos um caractere de cada grupo."""
    if tamanho < len(grupos):
        raise ValueError(f'O tamanho mínimo para esse tipo é {len(grupos)}.')
    todos = ''.join(grupos)
    senha = [secrets.choice(g) for g in grupos]
    senha += [secrets.choice(todos) for _ in range(tamanho - len(grupos))]
    # Embaralha para os caracteres obrigatórios não ficarem sempre no início.
    for i in range(len(senha) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        senha[i], senha[j] = senha[j], senha[i]
    return ''.join(senha)


def ler_tamanho():
    while True:
        try:
            tamanho = int(input('Digite o tamanho da senha: '))
        except ValueError:
            print('Por favor, insira um número válido.')
            continue
        if tamanho <= 0:
            print('O tamanho da senha deve ser maior que 0.')
        else:
            return tamanho


def menu():
    print('\nEscolha o tipo de senha a ser gerada:')
    for opcao, (nome, _) in TIPOS.items():
        print(f'{opcao} - {nome}')
    print('4 - Sair')
    return input('Digite a opção desejada: ').strip()


def main():
    tamanho = ler_tamanho()
    while True:
        opcao = menu()
        if opcao == '4':
            print('Saindo...')
            break
        if opcao not in TIPOS:
            print('Opção inválida. Tente novamente.')
            continue
        nome, grupos = TIPOS[opcao]
        try:
            print(f'{nome}: {gerar_senha(grupos, tamanho)}')
        except ValueError as erro:
            print(erro)


if __name__ == '__main__':
    main()

# Gerador de senhas em Python

Programa de terminal que gera senhas aleatórias de três tipos:

1. Completa: minúsculas, maiúsculas, números e símbolos
2. Maiúsculas e números
3. Minúsculas e maiúsculas

As senhas são geradas com o módulo [`secrets`](https://docs.python.org/3/library/secrets.html), próprio para valores que não podem ser previstos, e sempre têm pelo menos um caractere de cada tipo escolhido.

## Como usar

Requer Python 3.6 ou superior, sem dependências externas.

```bash
python Gerenciador_senha.py   # versão em português
python Password_manager.py    # versão em inglês
```

```
Digite o tamanho da senha: 16

Escolha o tipo de senha a ser gerada:
1 - Senha completa
2 - Senha com maiúsculas e números
3 - Senha com minúsculas e maiúsculas
4 - Sair
Digite a opção desejada: 1
Senha completa: q7#Rb-x2M{fT9a_K
```

## Próximos passos

- Guardar as senhas geradas em um arquivo criptografado, protegido por uma senha mestra.

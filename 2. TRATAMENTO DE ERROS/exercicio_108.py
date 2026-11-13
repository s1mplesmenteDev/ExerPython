# Reescreva a função leiaInt() que fizemos no exercicio 101, 
# incluindo agora as possibilidade de digitação de um numero de tipo inválido.
#  Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt():
    while True:
        entradaInt = input('Digite um numero inteiro: ')
        try:
            if int(entradaInt):
                # print(f'Você digitou o numero {entradaInt}')
                return entradaInt

        except (ValueError, TypeError):
            print('Erro de valor ou tipo de dados.')
        except KeyboardInterrupt:
            print('O usuário interrompeu o programa.')


def leiaFloat():
    while True:
        entradaFloat = input('Digite um numero real: ').replace(',','.').strip()
        try:
            if float(entradaFloat) >= 0:
                # print(f'Você digitou o numero {entradaFloat}')
                return entradaFloat
        except (ValueError, TypeError):
            print('Erro de valor ou tipo de dados.')
        except KeyboardInterrupt:
            print('O usuário interrompeu o programa.')

n = 0
while n == 0:
    entradaInt = leiaInt()
    entradaFloat = leiaFloat()
    n+=1
    print(f'O numero inteiro é {entradaInt} e o numero real é {entradaFloat}')
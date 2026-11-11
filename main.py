from exercicio_107.moedas import moeda
from exercicio_107.dados import dado

valor = dado.leiaDinheiro()
pAumentar = int(input('Digite a porcentagem de aumento: '))
pDiminuir = int(input('Digite a porcentagem de redução: '))
p = str(input('Deseja mostrar o valor formatado? [S/N]')).lower()

if p in 'sS':
    real = True
else:
    real = False
    
moeda.resumo(valor, pAumentar,pDiminuir,real)

# print(f'A metade de R${valor:,.2f} é {exercicio_107.moedas.metade(valor,real)}')
# print(f'O dobro de R${valor:,.2f} é {exercicio_107.moedas.dobro(valor,real)}')
# print(f'Aumentado 10%, temos {exercicio_107.moedas.aumentar(valor,10,real)}')
# print(f'Reduzindo 10%, temos {exercicio_107.moedas.diminuir(valor,10,real)}')


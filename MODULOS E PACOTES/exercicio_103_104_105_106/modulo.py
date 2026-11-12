def aumentar (valor, porcentagem = 10,real = False): #10%
    valor *= 1 + porcentagem/100
    if real:
        return f'R${valor:,.2f}'
    return valor

def diminuir(valor, porcentagem = 15,real = False): #15%
    valor *= 1 - porcentagem/100
    if real:
        return f'R${valor:,.2f}'
    return valor

def dobro(valor, real = False):
    valor *= 2
    if real:
        return f'R${valor:,.2f}'
    return valor    

def metade (valor, real = False):
    valor /= 2
    if real:
        return f'R${valor:,.2f}'
    return valor

def moeda(valor):
    return f'R${valor:,.2f}'

def resumo (valor, pAumentar = 10, pDiminuir = 15, real = False):
    print('-='*30)
    print('RESUMO DO VALOR'.center(30))
    print('-='*30)
    print(f'A metade de R${valor:,.2f} é {metade(valor,real)}')
    print(f'O dobro de R${valor:,.2f} é {dobro(valor,real)}')
    print(f'Aumentado {pAumentar}%, temos {aumentar(valor,pAumentar,real)}')
    print(f'Reduzindo {pDiminuir}%, temos {diminuir(valor,pDiminuir,real)}')
    print('-='*30)
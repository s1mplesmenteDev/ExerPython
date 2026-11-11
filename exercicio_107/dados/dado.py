def leiaDinheiro():
    while True:
        entrada = input('Digite um valor: ').replace(',','.').strip()
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
        except ValueError:
            print('Digite um valor válido!')
#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto,
#o sistema só vai ter 3 opções: cadastrar uma nova pessoa e listar todas as pessoas e sair

from pathlib import Path

arquivo = Path('exercicio_110.txt')

if not arquivo.is_file():
    with open('exercicio_110.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Arquivo criado com sucesso!\n')

def cadastrarPessoas():
    with open('exercicio_110.txt', 'a', encoding='utf-8') as arquivo:
        nome = input('Digite o nome da pessoa: ')
        idade = input('Digite a idade da pessoa: ')
        arquivo.write(f'Nome: {nome} - Idade: {idade}\n')
        print(f'Pessoa {nome} cadastrada com sucesso!')
        

def listarPessoas():
    with open('exercicio_110.txt', 'r', encoding='utf-8') as arquivo:
        print('-='*30)
        print(arquivo.read().center(60))
        print('-='*30)

def sair():
    print('-='*30)
    print('Saindo do sistema...'.center(60))
    print('-='*30)
    exit()

def menu():
    while True:
        print('-='*30)
        print('MENU PRINCIPAL'.center(60))
        print('-='*30)
        print('1 - Cadastrar nova pessoa')
        print('2 - Listar todas as pessoas')
        print('3 - Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            cadastrarPessoas()
        elif opcao == '2':
            listarPessoas()
        elif opcao == '3':
            sair()
        else:
            
            print('Opção inválida! Tente novamente.')


menu()
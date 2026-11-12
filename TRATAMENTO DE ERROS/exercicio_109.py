# Crie um teste para verifica se o site do google está acessivel

import requests

def verificador(url):
    url = url.strip()
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
        
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print('o site está acessível.')
        else:
            print('o site está inácessível.')
    except requests.exceptions.RequestException as error:
        print(f'Erro ao acessar o site. {error}')

while True:
    url = input('Digite a url do site: ')
    verificador(url)

    q = str(input('Deseja verificar outro site? (s/n): '))
    if q not in 'sS':
        break
    
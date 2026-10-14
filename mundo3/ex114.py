# Importações
from urllib import error
import urllib.request

# Programa Principal
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except error.URLError:
    print('\033[1;31mO site Pudim não está acessível no momento.')
else:
    print('\033[1;32mO site Pudim está disponível.')

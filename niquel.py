import random
import time
import os

SIMBOLOS = [ 'U0001F600' ]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_maquina(colunas, status):
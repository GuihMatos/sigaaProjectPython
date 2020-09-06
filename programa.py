#Project algorithms 'DISCIPLINAS CURSADAS'.
from funcoes import *
                    
while True:    
    print('Bem vindo ao sistema de disciplinas')
    print('Faça Login ou Cadastre-se para acessar o sistema\n')
    print('[1] Login [0] Cadastro\n')
    a = input('Selecione a opção: ')
    if a == '0':
        cadastro()
    elif a == '1':
        login()    
    else:
        print('\nOpção invalida\n')

    
    



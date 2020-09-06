D = {'DEMA0090':['MATEMATICA APLICADA',60,float(7.8)],'DCCET0010':['CALCULO INTEGRAL',90,float(6.9)]}
C = {'admin':'admin'}
def main ():
    global D
    while True:
        print('\nPRESSIONE O NÚMERO DA OPÇÃO PREFERIDA ABAIXO: ')
    
        print('''\n[1]CADASTRAR DISCIPLINA
[2]ALTERAR DISCIPLINA
[3]EXCLUIR DISCIPLINA
[4]LOCALIZAR DISCIPLINA
[5]LISTAR TODAS AS DISCIPLINAS
[6]SAIR\n''')
        a = input('Selecione a opção: ')
        if a == '1':
            cadastro_d()
        elif a == '2':
            alterar_d()
        elif a == '3':
            exclusao_d()
        elif a == '4':
            localizar_d()
        elif a == '5':
            listar_d()
        elif a == '6':
            break
        else:
            print("Opção invalida")
 
def cadastro ():
    global C
    a = input("Defina um login a ser cadastrado: ")
    b = input ("Defina uma senha: ")
    if a not in C.keys():
       C[a] = b
       print("Cadastro realizado com sucesso.")
    else:
        print("Usuário já existente.")
def login ():
    global C
    a = input("Insira seu login:  ")
    b = input("Insira sua senha: ")
    if a not in C.keys():
        print("\nUsuario não cadastrado\n") 
   
    elif b == C[a]:
        main() 
   
    else:
        print("\nSenha ou Usuario incorreto\n")

def cadastro_d():
    global D
    cad_d = []
    a1 = input('\nDigite o código da disciplina: ').upper()
    a2 = str(input('Digite o nome da disciplina: ')).upper()
    a3 = int(input('Digite a ch da disciplina: '))
    a4 = float(input('Digite a nota da disciplina: '))
    
    cad_d.append(a2)
    cad_d.append(a3)
    cad_d.append(a4)
    D[a1] = cad_d
    print('\nDISCIPLINA CADASTRADA!')

    alt_d = []
    
def alterar_d():
    global D
    alt_d=[]
    a1 =input('\nDigite o código da disciplina p/ alterar: ').upper()
    if a1 in D.keys():
       print(D.get(a1))
       a2 = str(input('Digite o novo nome da disciplina: ')).upper()
       a3 = int(input('Digite a nova ch da disciplina: '))
       a4 = float(input('Digite a nova nota da disciplina: '))
            
       alt_d.append(a2)
       alt_d.append(a3)
       alt_d.append(a4)
       D[a1] = alt_d
       print('\nDISCIPLINA ALTERADA COM SUCESSO!')
       print('\n',D[a1])
            
    else:
       print('\nDisciplina não cadastrada.')
    
def exclusao_d():
    global D
    a1 = input('\nDigite o código da disciplina p/ excluir: ').upper()
    if a1 in D.keys():
       del D[a1]
       print('\nDISCIPLINA DELETADA COM EXITO!')

    else:
       print('\nDisciplina não cadastrada.')
def localizar_d():
    global D
    a1 = input('\nDigite o código da disciplina p/ localiza-la: ').upper()
    if a1 in D.keys():
       print(D[a1])
    else:
       print('\nDisciplina não cadastrada.')
def listar_d():
    global D
    contador = 0
    soma_int = 0
    soma_f = 0
    cont_f = 0
 
    print("Legenda")
    print('CODIGO:[ MATERIA, CH, NOTA]\n')
    print('\nDisciplinas')
    for x in D.keys():
        print(str(x)+':'+str(D[x]))
        contador+= 1
    print("\nTotal:",str(contador))
    for e1 in D.values():
        for e2 in e1:
            if type(e2) == int:
                soma_int += e2
            elif type(e2) == float:
                soma_f += e2
    media = float(soma_f/contador)
    print('\nTotal de CH'+':'+str(soma_int))
    print('\nCR(Media de desempenho):'+str(media))

from dados import estoque_prodotos, dados_usuarios, nomes_categorias
from datetime import datetime
import time
import os

agora = datetime.now()
hora = agora.hour
minutos = agora.second
logado = False

# login- CriarUsuario - mostrar_estoque - ExcluirUsuario -


# - AdicionarProduto 
# -- Nome
# -- Quantidade
# -- Valor


# ExcluirProduto -  - 
def banner():
    print('-'*40)
    print('        Mercadinho Jerico ')
    print('-'*40)

banner()
def login(data):
    logado = False
    tentativas = 0
    while tentativas < 3:
        print('        Faça o Login')
        usuario = input('Digite o seu Usuario')
        if usuario in data:
            senha = input('Digite a sua senha')
            if senha == data[usuario]:
                print('Acesso Liberado')
                logado = True
        if logado == False:
            print('Usuario ou Senha Incorreto')
            time.sleep(1)
        tentativas += 1
        os.system('clear')
    return logado, usuario

#logado, usuario = login(dados_usuarios)


def excluir_usuario(data, usuario):
    print('        Excluir Usuario')
    confirmacao = input(f'Realmente Deseja Excluir o usuario: {usuario} [y/n]')
    if confirmacao == 'y':
        senha = input('Digite a sua Senha ')
        if senha == data[usuario]:
            data.pop(usuario, None)
            print('Usuario foi exckuido')
            logado = False
    else:
        print('Obrigadopor Continuar Conosco')
    time.sleep(1)
    os.system('clear')    
    return data, logado
#excluir_usuario, logado = excluir_usuario(dados_usuarios, usuario)

def criar_usuario(data):
    tentativas = 0
    while tentativas < 2:
        print('        Criar Usuario')
        novo_usuario = input('Digite um nome para o seu usuario ')
        if novo_usuario in data:
            print('Já existe um usuario com esse nome')
        else:
            senha = input('Crie uma senha ')
            senha2 = input('Digite de novo a senha ')
            if senha != senha2:
                print('As Senha não são iguais')
                print('')
                print('Tente Novamente')    
                
            else:
                data[novo_usuario] = senha
                print('Usuarios Criado')
                log = True
                tentativas = 5
                
        tentativas += 1
        time.sleep(1)
        os.system('clear')
        return data, log
#dados_usuarios, logado = criar_usuario(dados_usuarios)



def escolha_categoria(n_catergoria):
    loop = True
    while loop:
        os.system('clear')
        print('Escoolha uma catergoria | -1 para cancelar')
        for id_cate, cate in enumerate(n_catergoria): 
            print(f'{id_cate} - {cate}')
        try:
            categoria = int(input(''))
            if categoria >= 0 and categoria < len(n_catergoria):
                return categoria  
            elif categoria == -1:
                break
            else:    
                print('Valor Invalido')
                time.sleep(1)
        except:
            time.sleep(1)
            print('Valor Invalido')   
        

def mostrar_estoque(data):

    categoria= escolha_categoria(nomes_categorias)
    print(categoria)
    for produto in data[categoria]:
        print('ID: ', data[categoria][produto][0])
        print(f'Nome: {produto}')
        print(f'Quantidade: {data[categoria][produto][1]}')
        print(f'Valor: {data[categoria][produto][2]}')
        print('-'*28)
mostrar_estoque(estoque_prodotos)




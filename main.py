from dados import estoque_prodotos, dados_usuarios, nomes_categorias
from datetime import datetime
import requests
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
                tentativas += 5
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
        return data, log, novo_usuario
#dados_usuarios, logado = criar_usuario(dados_usuarios)



def escolha_categoria(n_catergoria):
    loop = True
    while loop:
        os.system('clear')
        banner()

        print('Escoolha uma catergoria | -1 Menu')
        for id_cate, cate in enumerate(n_catergoria): 
            print(f'{id_cate} - {cate}')
        try:
            categoria = int(input(''))
            if categoria >= 0 and categoria < len(n_catergoria):
                return categoria  
            elif categoria == -1:
                return categoria 
                break
            else:    
                print('Valor Invalido')
                time.sleep(1)
        except:
            time.sleep(1)
            print('Valor Invalido')   
        

def mostrar_estoque(data):

    categoria= escolha_categoria(nomes_categorias)
    if categoria != -1:
        for produto in data[categoria]:
            print('ID: ', data[categoria][produto][0])
            print(f'Nome: {produto}')
            print(f'Quantidade: {data[categoria][produto][1]}')
            print(f'Valor: {data[categoria][produto][2]}')
            print('-'*28)
    else:
        os.system('clear')
        menu()
#mostrar_estoque(estoque_prodotos)


def adcionar_produto():
    pass

def carrinho_compra():
    pass

def endereco_cliente():
    print('        Endereço')
    print('-'*20)
    #cep = input(int('Digite o seu Cep: '))
    cep = "69909230"
    endereco = buscar_endereco(cep)
    chaves_endereco = ['cep', 'estado', 'bairro', 'uf', 'logradouro', 'regiao']
    if type(endereco) == str:
        print(endereco)
    else:    
        for chave in chaves_endereco:
            valor = endereco.get(chave, 'Chave Não Encontrada')
            print(f'{chave}: {valor}')
            print('-'*10)

def buscar_endereco(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            return "CEP não encontrado."
        return dados
    else:
        return "Erro na requisição."
#endereco_cliente()


def menu():
    print('         MENU ')
    print('Oque Deseja  fazer ? \n 1 - Ver Produtos \n 2 - Ver Carrinho \n 0 - Sair')
    valor = input('')
    if valor == '1':
        mostrar_estoque(estoque_prodotos)
    elif valor == '2':    
        pass
    elif valor == '0':
        desligar()
        loop = False
        return loop
    else:
        print('valor invalido')    
    return True

def desligar():
    for n in range(0,5):
        banner()
        print('Desligando em: ', n)
        time.sleep(1)
        os.system('clear')
    banner()    
    print('Sistema Desligado ')
    
    


loop_master = True
while loop_master:
    banner()

    if logado: 
        loop_master  = menu()
        print('Vamos lá')
    else:
        print('Tem Usuario Criado no Sistema ? \n 0 - Desligar \n 1 - Sim \n 2 - Não')
        inicio = input('  ')
        os.system('clear')
        if inicio == '1':
            logado, usuario = login(dados_usuarios)
        elif inicio == '2':
              dados_usuarios, logado, usuario = criar_usuario(dados_usuarios)
        elif inicio == '0':
            desligar()
            loop_master = False
        else:
            print('Opção Invalida')       
        
        
 #       print(logado, usuario)



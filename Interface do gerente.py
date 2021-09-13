# INTERFACE DO GERENTE
import pickle  # importando a biblioteca do pickle
from random import *  # importando uma biblioteca random para utilizar quando gerar o número de conta corrente

# PRIMEIRA INTERFACE DO GERENTE
print("~" * 20)
print("Interface do Gerente")
print("~" * 20)
# da linha 5 ate a 8 temos a identificação do tipo da interface separados por "~", por uma questão de estética

def loop():  # fizemos uma função com as opções que o gerente tem
    print("Cadastrar nova conta = 1" "\nPesquisar conta = 2" "\nDefinir senha de conta existente = 3")
    gerente = int(input("Digite a ação que deseja:")) # print das funções que da para executar na interface do gerente
    if gerente == 1:  # nova conta
        Cadastro_de_nova_conta()  # Aqui chamamos a função para cadastrar uma nova conta
    elif gerente == 2:  # pesquisa de conta
        busca_de_conta_corrente()  # Aqui chamamos a função para pesquisar um conta ja existente
    elif gerente == 3:  # redefinir senha
        definição_de_nova_senha()  # Aqui chamamos a função para cadastrar uma nova senha de conta corrente
    else:
        print("Sem ação correspondente.")  # Mensagem que da para usuário caso digite uma ação diferente de 1, 2 e 3

try:
    file = open("Numeros", "rb")
    file.close()
    file = open("contas", "rb")
    file.close()
# da linha 23 até a linha 28, ele verifica se tem um arquivo pickle aberto
except:
    x = [0]
    file = open("contas", "wb")
    pickle.dump(x, file)
    file.close()
    x = [0]
    file = open("contas", "wb")
    pickle.dump(x, file)
    file.close()
# da linha 29 até a linha 37, se nao tem nenhum arquivo pickle aberto, ele cria um

def testar_numero_duplicado():  # Função para testar se tem número da conta duplicada
    numero_aleatorio = pickle.load(open("Numeros", "rb"))  # Carrega o arquivo pickle
    numero_conta_corrente = randint(10000, 99999)  # gera um número aleatorio para a conta corrente
    erro = 0
    for i in numero_aleatorio:
        if i == numero_conta_corrente:
            erro = 1
    if erro == 1:
        testar_numero_duplicado()  # chama a função novamente para testar a conta
    else:
        file.close()  # fecha o arquivo
        y = pickle.load(open('Numeros', 'rb'))  # carrega o arquivo pickle
        y.append(numero_conta_corrente)  # adiciona no arquivo pickle
        pickle.dump(y, open("Numeros", "wb"))  # abre o arquivo pickle
        return numero_conta_corrente  # retorna o número da conta correnteg


def padrao_de_senha():  # Definir se a senha tem apenas os caracteres permitidos
    digitos_permitidos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                          "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B",
                          "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                          "V", "W", "X", "Y",
                          "Z"]  # Aqui temos os caracteres permitidos, diferente desses caracteres ele não aceita
    senha = str(input("Digite a sua senha:"))  # local onde o usuário vai digitar a senha desejada
    senha_separada = []  # Pasta para armazenar os caracteres separados da senha do usuário, para testar cada letra/numero da senha
    soma = 0
    for i in senha:  # Aqui temos um laço de repetição para verificar a senha
        senha_separada.append(senha[soma])
        soma += 1
    erro = 0
    for i in senha_separada:
        if i != digitos_permitidos[0] and i != digitos_permitidos[1] and i != digitos_permitidos[2] and i != \
                digitos_permitidos[3] and i != digitos_permitidos[4] and i != digitos_permitidos[5] and i != \
                digitos_permitidos[6] and i != digitos_permitidos[7] and i != digitos_permitidos[8] and i != \
                digitos_permitidos[9] and i != digitos_permitidos[10] and i != digitos_permitidos[11] and i != \
                digitos_permitidos[12] and i != digitos_permitidos[13] and i != digitos_permitidos[14] and i != \
                digitos_permitidos[15] and i != digitos_permitidos[16] and i != digitos_permitidos[17] and i != \
                digitos_permitidos[18] and i != digitos_permitidos[19] and i != digitos_permitidos[20] and i != \
                digitos_permitidos[21] and i != digitos_permitidos[22] and i != digitos_permitidos[23] and i != \
                digitos_permitidos[24] and i != digitos_permitidos[25] and i != digitos_permitidos[26] and i != \
                digitos_permitidos[27] and i != digitos_permitidos[28] and i != digitos_permitidos[29] and i != \
                digitos_permitidos[30] and i != digitos_permitidos[31] and i != digitos_permitidos[32] and i != \
                digitos_permitidos[33] and i != digitos_permitidos[34] and i != digitos_permitidos[35] and i != \
                digitos_permitidos[36] and i != digitos_permitidos[37] and i != digitos_permitidos[38] and i != \
                digitos_permitidos[39] and i != digitos_permitidos[40] and i != digitos_permitidos[41] and i != \
                digitos_permitidos[42] and i != digitos_permitidos[43] and i != digitos_permitidos[44] and i != \
                digitos_permitidos[45] and i != digitos_permitidos[46] and i != digitos_permitidos[47] and i != \
                digitos_permitidos[48] and i != digitos_permitidos[49] and i != digitos_permitidos[50] and i != \
                digitos_permitidos[51] and i != digitos_permitidos[52] and i != digitos_permitidos[53] and i != \
                digitos_permitidos[54] and i != digitos_permitidos[55] and i != digitos_permitidos[56] and i != \
                digitos_permitidos[57] and i != digitos_permitidos[58] and i != digitos_permitidos[59] and i != \
                digitos_permitidos[60] and i != digitos_permitidos[61]:
            # No 'if' ele testa todos os dígitos da senha
            erro = 1
            print(f"{i} é um digito inválido")  # mensagem que da para o gerente mostrando qual digito é incorreto
    if erro == 1:
        print(
            "Senha errada")  # mensagem que da para o gerente caso a senha nao seja permitida, no '{i}' ele mostra a senha que foi digitada anteriormente
        padrao_de_senha()  # aqui ele chama a função novamente para que possa cadastrar uma senha de forma correta
    else:
        return senha  # se a senha entrar em todos os requisitos, ele vai mostrar a senha como ficou


def padrao_de_nome():  # função para verificar o padrao do nome
    digitos_permitidos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                          "S", "T", "U", "V", "W", "X", "Y", "Z"]  # todos os dígitos permitidos para inserir no nome
    nome = str(input(
        "Digite o seu primeiro nome (digite-o em maiúsculo):"))  # local onde o gerente digita o primeiro nome do cliente
    nome_separado = []
    soma = 0
    for i in nome:  # laço de repetição para testar o nome
        nome_separado.append(nome[soma])  # adiciona o "nome_separado" ao arqivo pickle
        soma += 1
        erro = 0
        for i in nome_separado:
            if i != digitos_permitidos[0] and i != digitos_permitidos[1] and i != digitos_permitidos[2] and i != \
                    digitos_permitidos[3] and i != digitos_permitidos[4] and i != digitos_permitidos[5] and i != \
                    digitos_permitidos[6] and i != digitos_permitidos[7] and i != digitos_permitidos[8] and i != \
                    digitos_permitidos[9] and i != digitos_permitidos[10] and i != digitos_permitidos[11] and i != \
                    digitos_permitidos[12] and i != digitos_permitidos[13] and i != digitos_permitidos[14] and i != \
                    digitos_permitidos[15] and i != digitos_permitidos[16] and i != digitos_permitidos[17] and i != \
                    digitos_permitidos[18] and i != digitos_permitidos[19] and i != digitos_permitidos[20] and i != \
                    digitos_permitidos[21] and i != digitos_permitidos[22] and i != digitos_permitidos[23] and i != \
                    digitos_permitidos[24] and i != digitos_permitidos[25]:  # aqui testa dígito por dígito do nome do cliente
                print(f"{i} é um digito inválido")  # Mostra qual dígito esta errado no nome do cliente
                erro = 1
                if erro == 1:
                    print(
                        "Digite o nome em letras maiúsculas")  # Mensagem que da para o gerente falado que deve ser digitado o nome do cliente apenas em letras maiúsculas
                    padrao_de_nome()  # se der errado o nome, chama a função para recomeçar o processo
                else:
                    return nome  # se tudo estiver correto, vai retornar o nome


def padrao_de_sobrenome():  # função para padronizar o sobrenome
    digitos_permitidos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                          "T", "U", "V", "W", "X", "Y", "Z"]  # digitos que sao permitidos, diferente disso vai dar erro
    sobrenome = str(
        input("Digite o seu sobrenome (digite-o em maiúsculo):"))  # local para digitar o sobrenome do cliente
    sobrenome_separado = []
    soma = 0
    for i in sobrenome:  # laço de repetição para testar o sobrenome
        sobrenome_separado.append(sobrenome[soma])  # adiciona o "nome_separado" para o arquivo pickle
        soma += 1
    erro = 0
    for i in sobrenome_separado:
        if i != digitos_permitidos[0] and i != digitos_permitidos[1] and i != digitos_permitidos[2] and i != \
                digitos_permitidos[3] and i != digitos_permitidos[4] and i != digitos_permitidos[5] and i != \
                digitos_permitidos[6] and i != digitos_permitidos[7] and i != digitos_permitidos[8] and i != \
                digitos_permitidos[9] and i != digitos_permitidos[10] and i != digitos_permitidos[11] and i != \
                digitos_permitidos[12] and i != digitos_permitidos[13] and i != digitos_permitidos[14] and i != \
                digitos_permitidos[15] and i != digitos_permitidos[16] and i != digitos_permitidos[17] and i != \
                digitos_permitidos[18] and i != digitos_permitidos[19] and i != digitos_permitidos[20] and i != \
                digitos_permitidos[21] and i != digitos_permitidos[22] and i != digitos_permitidos[23] and i != \
                digitos_permitidos[24] and i != digitos_permitidos[25]:
            # na linha de cima temos a verificação dígito por dígito do nome do cliente
            print(f"{i} é um digito inválido")  # mostra para o gerente qual o dígito errado
            erro = 1
    if erro == 1:
        print(
            "Digite o sobrenome em letras minúsculas letras minúsculas")  # mensagem que vai dar caso o sobrenome nao seja digitado em maiusculo
        padrao_de_sobrenome()  # caso o sobrenome seja incorreto, chama a função novamente para realizar o processo
    else:
        return sobrenome  # se tudo estiver certo, vai retornar o sobrenome


def Cadastro_de_nova_conta():  # função para cadastrar uma nova conta
    nome = padrao_de_nome()  # chamamos a função "padrao_de_nome para definir o nome e guardamos em uma variável chamada "nome"
    sobrenome = padrao_de_sobrenome()  # chamamos função "padrao_de_sobrenome para definir o sobrenome e guardamos em uma variável chamada sobrenome
    profissao = str(input("Qual a sua profissão:"))  # local onde o gerente digita a profissão do cliente
    renda_mensal = str(input("Qual a sua renda mensal:"))  # local onde o gerente digita a renda mensal do cliente
    endereco = str(
        input("Digite o nome da sua rua + número + complemento:"))  # local onde o gerente digita o endereço do cliente
    numero_telefone = str(
        input("Digite o seu número:((DDD) + número)"))  # local onde o gerente digita o número de telefone do cliente
    deposito_inicial = float(
        input("Digite o valor do depósito:"))  # local onde o gerente digita o depósito inicial do cliente
    dinheiro_em_conta = deposito_inicial  # guaramos a variável "deposito_inicial" na variável "dinheiro_em_conta"
    senha = padrao_de_senha()  # chamamos a função "padrao_de_senha" para definir a senha e guarmos na variável "senha"
    numero_conta_corrente = testar_numero_duplicado()  # chamamos a função "testar_numero_duplicado" para definir o nuemro da conta corrente e guardamos na veriável "numero_conta_corrente"
    print(
        f"O número da sua conta corrente é:{numero_conta_corrente}")  # mostra para o gerente qual o número da conta corrente do cliente
    file = open('contas', 'rb')  # abre o arquivo pickle para escrita
    y = pickle.load(file)  # carrega o arquivo pickle
    y.append(nome)  # adiciona o nome no arquivo pickle
    y.append(sobrenome)  # adiciona o sobrenome no arquivo pickle
    y.append(profissao)  # adiciona a profissão no arquivo pickle
    y.append(renda_mensal)  # adiciona a renda mensal no arquivo pickle
    y.append(endereco)  # adiciona o endereço no arquivo pickle
    y.append(numero_telefone)  # adiciona o número de telefone no arquivo pickle
    y.append(senha)  # adiciona a senha no arquivo pickle
    y.append(dinheiro_em_conta)  # adiciona o saldo no arquivo pickle
    y.append(numero_conta_corrente)  # adiciona o número de conta corrente no arquivo pickle
    file = open('contas', 'wb')  # abre o arquivo pickle para leitura
    pickle.dump(y, file)  # adiciona o "y" a um "file"
    file.close()  # fecha o arquivo
    loop()  # chama a função novamente para escolher ação


# BUSCA DE CONTA CORRENTE
def busca_de_conta_corrente():
    nome_conta = str(input("Insira o nome da conta do cliente que deseja buscar:")) # local onde o gerente vai colocar o nome do cliente para tentar achar a conta corrente do mesmo
    file = open('contas', 'rb') # abre o arquivo pickle para ler
    conta = pickle.load(file) # carrega os arquivos pickle
    erro = 1
    counter = 0
    teste = 0
    for i in conta:
        if teste == 0 and i == nome_conta: # nesse "if" ele mostra a conta que tem apenas um nome
            print(f"Nome:{conta[counter]}") # mostra o nome do cliente
            print(f"Sobrenomeome:{conta[counter + 1]}") # mostra o sobrenome do cliente
            print(f"Profissão:{conta[counter + 2]}") # mostra a profissão do cliente
            print(f"Renda mensal:{conta[counter + 3]}") # mostra a renda mensal do cliente
            print(f"Endereço:{conta[counter + 4]}") # mostra o endereço do cliente
            print(f"Telefone:{conta[counter + 5]}") # mostra o telefone do cliente
            print(f"Senha:{conta[counter + 6]}") # mostra a senha do cliente
            print(f"Saldo:{conta[counter + 7]}") # mostra o saldo do cliente
            print(f"Número da conta:{conta[counter + 8]}") # mostra o número da conta do cliente
            print("//////////////////////////////////////////") # separação das contas
            erro = 0
            teste = 1
        elif teste == 1 and i == nome_conta: # nesse elif serve caso o nome do cliente tenha mais de uma conta
            counter +=1
            print(f"Nome:{conta[counter]}")  # mostra o nome do cliente
            print(f"Sobrenomeome:{conta[counter + 1]}")  # mostra o sobrenome do cliente
            print(f"Profissão:{conta[counter + 2]}")  # mostra a profissão do cliente
            print(f"Renda mensal:{conta[counter + 3]}")  # mostra a renda mensal do cliente
            print(f"Endereço:{conta[counter + 4]}")  # mostra o endereço do cliente
            print(f"Telefone:{conta[counter + 5]}")  # mostra o telefone do cliente
            print(f"Senha:{conta[counter + 6]}")  # mostra a senha do cliente
            print(f"Saldo:{conta[counter + 7]}")  # mostra o saldo do cliente
            print(f"Número da conta:{conta[counter + 8]}")  # mostra o número da conta do cliente
            print("//////////////////////////////////////////")  # separação das contas
        else:
            counter+=1
    if erro == 1:
        print("Nome da conta inexistente (talvez você não esteja pesquisando o nome em letras maiúsculas)") # mensagem caso nenhuma conta seja encontrada
    loop() # chama a função "loop" para realizar uma nova ação


# DEFINIÇÃO DE NOVA SENHA
def definição_de_nova_senha():  # função para redefinir a senha da conta corrente
    numero_conta = int(input(
        "Insira o número da conta, para mudar a senha dela:"))  # local onde o gerente colocara o número da conta corrente do cliente
    file = open('contas', 'rb')  # Abre o arquivo pickle
    conta = pickle.load(file)  # carrega o arquivo pickle

    counter = 0
    for i in conta: # laço de repetição para verificar o número da conta
        if i == numero_conta: # Se os dados forem iguais, a senha é substituida
            senha_atual = conta[counter - 2]
        else:
            counter += 1
    tentativa_de_senha = str(input(f"{conta[counter - 7]}, digite a sua senha atual:"))  # local onde o gerente ira digitar a senha do cliente

    if tentativa_de_senha == senha_atual:  # verificação para ver se a senha digitada é a mesma que tem no arquivo pickle
        print("Senha correta!")  # mostra essa mensagem caso a senha seja correta
        print("Agora vamos fazer troca de senha:")  # mensagem de que vai começar o procedimento de troca de senha
        print("_" * 10) # separação para deixar o código mais organizado
        novaSenha = str(input("Digite uma nova senha para a sua conta corrente:")) # local onde a nova senha vai ser digitada
        conta[counter - 2] = novaSenha # posição da nova senha
        file = open('contas', 'wb') # abre o arquivo pickle para escrita
        pickle.dump(conta, file) # Substitui a senha antiga pera a senha atual no arquivo pickle
    else:
        print("Senha incorreta.") # mensagem caso a senha seja incorreta, impossibilitando a troca de senha
loop() # chama a função loop para realizar outra ação
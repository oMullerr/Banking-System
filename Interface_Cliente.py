# INTERFACE DO CLIENTE

import pickle # importando a biblioteca pickle para armazenar os dados

def saque(): # função para realizar o saque
    numero_conta = int(input("Insira o número da conta, para realizar o saque:")) # local onde o cliente o seu nome
    file = open('contas', 'rb') # abre o arquivo pickle  para leitura
    conta = pickle.load(file) # carrega o arquivo pickle

    counter = 0
    for i in conta: # laço de repetição para tesar o número da conta
        if i == numero_conta:
            senha_atual = conta[counter - 2]

        else:
            counter += 1 # caso nao encontre, vai adicioar +1 para procurar no próximo

    def teste_de_senha(): # função para testar a senha
        tentativa_de_senha = str(input(f"{conta[counter - 8]}, digite a sua senha atual:")) # local onde o cliente digitara a sua senha atual
        if tentativa_de_senha != senha_atual:
            print("Senha incorreta, tente novamente") # mensagem caso a senha informada for incorreta
            teste_de_senha() # chama a função para testar a senha novamente

    teste_de_senha() # rodar a função

    dinheiro_em_conta = (conta[counter - 1]) # variavel para guardar o dinheiro que tem em conta

    def retirada(): # função para saque
        print(f"Você tem R${dinheiro_em_conta} na sua conta") # mensagem que da mostrando o dinheiro que tem disponível para sacar
        valor_a_ser_retirado = float(input("Digite o valor do saque que deseja realizar:")) # local que o cliente digita a quantia que deseja sacar
        if valor_a_ser_retirado <= 0: # um dos requisitos é o saque ser maior que R$0,00
            print("O valor do saque deve ser maior que R$0,00.") # mensagem que da caso o valor de saque seja R$ 00,00
            retirada() # chama a função para poder realizar a ação novamente
        else:
            return valor_a_ser_retirado # se tudo estiver certo, ele retorna o valor do saque

    def teste_de_saque_negativo(): # função para testar se o cliente esta querendo sacar mais que o disponível
        valor_a_ser_retirado = retirada()
        conta_nova = dinheiro_em_conta - valor_a_ser_retirado # fazemos a opração e guardamos na variável 'conta_nova'
        if conta_nova < 0: # se a operação for menor do que 0
            print("Você está tentando sacar mais do que o disponível") # retorna essa mensagem de erro
            teste_de_saque_negativo() # chama a função para testar o valor do saque novamente
        else:
            return conta_nova # se tudo estiver certo, ele retorna o valor retirado

    conta_nova = teste_de_saque_negativo() # tira a conta nova do saque negativo

    print(f"Seu novo saldo é: R${conta_nova}") # mostra para o cliente o seu novo saldo

    conta[counter - 1] = conta_nova # substitui o valor disponível no arquivo pickle
    file = open('contas','wb') # abre o arquivo pickle para escrita
    pickle.dump(conta,file)
    file.close() # fecha o arquivo pickle
    loop() # chama a função loop para poder fazer outras ações

# FUNÇÃO DEPÓSITO
def deposito(): # função para a realização do depósito
    numero_conta = int(input("Insira o número da conta, para realizar o depósito:")) # local onde o cliente coloca o número da sua conta corrente
    conta = pickle.load(open('contas', 'rb')) # abre o arquivo pickle para leitura

    counter = 0
    for i in conta: # laço de repetição para testar a senha
        if i == numero_conta:
            senha_atual = conta[counter - 2]

        else:
            counter += 1 # caso nao encontre, vai adicioar +1 para procurar no próximo

    def teste_de_senha(): # função para testar a senha do cliente
        tentativa_de_senha = str(input(f"{conta[counter - 8]}, digite a sua senha atual:")) # local onde o cliente digitará a sua senha atual
        if tentativa_de_senha != senha_atual: # verificação para ver se a senha digitada é a mesma que consta nos arquivos
            print("Senha incorreta, tente novamente") # se for diferente, mostra a mensagem de que a senha esta errada
            teste_de_senha() # chama a função para digitar uma nova senha

    teste_de_senha() # rodar a função

    dinheiro_em_conta = (conta[counter - 1]) # substituir o saldo no arquivo

    def testar_valor(): # função para testar o valor do depósito
        print(f"Você tem R${dinheiro_em_conta} na sua conta") # local onde o cliente verifica o saldo da sua conta
        valor_a_ser_depositado = float(input("Digite o valor do depósito que deseja realizar:")) # local onde o cliente colocará o valor desejado
        if valor_a_ser_depositado <= 0 or valor_a_ser_depositado > 10000: # esses são os limites para o depósito
            print("O valor do depósito deve ser entre 0 e 10000 reais.") # mensagem que da caso o valor seja incorreto
            testar_valor() # chama a função para testar o valor novamente
        else:
            return valor_a_ser_depositado # caso tudo esteja certo, ele vai dar 'print' no valor depósito

    valor_a_ser_depositado = testar_valor() # o 'valor_a_ser_depositado quarda o valor que ficou no 'testar_valor()'
    conta_nova = dinheiro_em_conta + valor_a_ser_depositado # a variável 'conta_nova'guarda o resultado do 'dinheiro_em_conta + valor_a_ser_depositado'

    print(f"Seu novo saldo é: R${conta_nova}") # mensagem que o sistema da sobre o novo saldo do cliente

    conta[counter - 1] = conta_nova # pegamos a posição no arquivo e substituimos o valor do saldo
    file = open('contas', 'wb') # abrimos a conta para leitura
    pickle.dump(conta, file) # adicionamos a informação no arquivo
    file.close() # fecha o arquivo
    loop() # chama a função loop para realizar outra ação


# FUNÇÃO VISU NO SALDO
def visu_saldo(): # função para visualização do saldo do cliente
    numero_conta = int(input("Insira o número da conta, para visualizar o seu saldo:")) # local onde o cliente vai digitar o numero da sua conta corrente
    conta = pickle.load(open('contas', 'rb')) # abre o arquivo para leitura

    counter = 0
    for i in conta: # laço de repetição para verificar a conta
        if i == numero_conta:
            senha_atual = conta[counter - 2]

        else:
            counter += 1

    def teste_de_senha(): # função para testar a senha
        tentativa_de_senha = str(input(f"{conta[counter - 8]}, digite a sua senha atual:")) # ele mostra o nome do titular da conta e pede para digitar a senha atual
        if tentativa_de_senha != senha_atual: # verifica se a senha digitada é a mesma que consta nos arquivos
            print("Senha incorreta, tente novamente") # mensagem que a senha esta incorreta
            teste_de_senha() # chama a função para testar novamente a função

    teste_de_senha() # serve para rodar a função

    print(f"{conta[counter - 8]}, você tem R${(conta[counter - 1])} na sua conta, e seu número de conta corrente é:{conta[counter]}")# nessa mensagem ele da o 'print' do nome do titular, o saldo e o numero da conta corrente

    loop() # Chama a função loop para realizar outra ação

def investimento(): # função para calcular o investimento
    meses = int(input("Digite a quantidade de meses:")) # local onde o cliente vai digitar os meses que quer investir
    valor_inicial = float(input("Digite o aporte inicial:")) # local onde o cliente vai digitar a quantia inicial
    montante = valor_inicial * (1 + 0.005) ** meses # calculo dos juros compostos
    resultado = montante * 0.005 # calculo caso o investimento dure 5 ou mais anos
    resultado_2 = montante * 0.01 # calculo caso o investimento dure menos de 5 anos
    if meses > 60: # condição para o investimento seja mais que 5 anos
        print(f"O seu investimento sera de:{resultado}") # mensagem com o resultado
    elif meses <= 60: # condição parao investimento seja menos ou igual a 5 anos
        print(f"O seu investiemnto sera de:{resultado_2}") # mensagem com o resultado
    loop() # chamamos a função para poder realizar outra ação

def loop(): # função com todas as opções do cliente
    print("\nPara fazer um saque  = 1" "\nPara fazer um depósito = 2" "\nPara visualizar seu saldo = 3" "\nPara simular um investimento = 4")
    # Opções que o cliente tem
    cliente = int(input("\nDigite a ação que deseja:")) # local onde o cliente coloca a ação desejada
    if cliente == 1:  # saque
        saque() # chamamos a função saque
    elif cliente == 2:  # Depósito
        deposito() # chamamos a função depósito
    elif cliente == 3:  # saldo
        visu_saldo() # chamamos a função para visualização do saldo
    elif cliente == 4:
        investimento() # # chamamos a função para simular um investimento
    else:
        print("\nSem ação correspondente.") # mensagem que da caso seja digitado um número diferente de 1, 2, 3 e 4
        loop() # chama a função para poder fazer

try:
    open("Numeros", "rb")
    open("contas", "rb")
# da linha 23 até a linha 28, ele verifica se tem um arquivo pickle aberto
except:
    print("Você precisa executar a interface do gerente primeiro") # da a mensagem caso não de certo
else:
    print("~" * 20)
    print("Interface do Cliente")
    print("~" * 20)
    # da linha 162 ate a linha 164 temos a identificação da interface seguido de "~" por uma questão de estética
    loop() # chama a função para fazer outras ações
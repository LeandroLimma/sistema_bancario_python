# Sistema bancário em Python para a atividade da plataforma DIO.me

# Mensagem de boas vindas ao usuário
print("Olá, seja bem vindo ao nosso caixa eletrônico!")

# Informar a apoção que o usuário deseja utilizar no nosso caixa
opcao = int(input("Informe a opção desejada \n[1] Depositar \n[2] Sacar \n[3] Extrato \n[0]Sair: "))
# Operação para Depósito
if opcao == 1:
    valor = float(input("Informe o valor do depósito: "))
    print("Depósito realizado com sucesso...")
# Operação para Sacar
if opcao == 2:
    valor = float(input("Informe o valor que você deseja sacar: "))
    print("Saque realizado com sucesso...")
# Operação para ver o Extrato
if opcao == 3:
    print("Exibindo o extrato...")
# Opção para encerrar a utilização do caixa eletrônico
if opcao == 0:
    print("Obrigado por utilizar nossos serviços, lhe vejo em breve ;)")
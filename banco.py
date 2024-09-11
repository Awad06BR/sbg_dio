import datetime



menu = """############### SGB - v0.2 ##############
#                                       #
# [d]Depositar        [e]Extrato        #
#                                       #
# [s]Sacar            [u] Criar Usuario #
#                                       #
# [c] Criar Conta                       #
#                                       #
#                     [q] Sair          #
#########################################
=> """

saldo = 0
limite = 500
extrato = ''
numero_transacoes = 0
usuarios = []
contas=[]

LIMITE_SAQUES = 3
AGENCIA = "0001"


def gravarExtrato(tipomovimentacao,valor):
  global extrato 
  data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
  extrato = extrato + (f" {data} - {tipomovimentacao}.....................R${valor:.2f}\n")

def validaLimiteTransacoesDiaria(numerotransacao):
  limite = 10 
  if numerotransacao>limite:
     print ("Você excedeu o limite de transação permitida para o dia de hoje!")
     return False
  return True

def deposito(valor,saldo):
  if (valor)>0:
    saldo += valor
    print(f"Valor depositado com sucesso! Seu novo saldo é igual à R${saldo}")
  else:
    print("Valor invalido! insira um valor acima de 0")

  return saldo
  

def saque(valor,saldo):
  if(valor<=limite):
    saldo -= valor
    print (f"Saque Realizado! Seu saldo é {saldo}")
  else:
    print("Valor maior que o permitido para saque!")

  return saldo

def exibir_extrato(saldo,/,*,extrato):
  print("########## Extrato Bancario - v1.0 ##########")
  print("Não existe Movimentação" if not extrato else extrato)
  print(f"\n Saldo{saldo:.2f}" )

def criar_usuario(usuarios):
  cpf = input("Informe o CPF (APENAS NUMEROS):")

  usuario = validar_usuario(usuarios,cpf)

  if usuarios:
    print("CPF Já Cadastrado!")
    return

  nome = input("Digite o Nome do usuario:")
  dt_nascimento = input("Digite a Data de Nascimento:")
  endereco = input("informe o endereço (lougradouro, n° - bairro - cidade/sigla estado):")

  usuarios.append({"nome":nome,"data_nascimento":dt_nascimento,"cpf":cpf,"endereco":endereco})

  print ("Usuario Cadastrado!")
  

def validar_usuario(usuarios,cpf):
  usuario_validado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuario_validado[0] if usuario_validado else None

def criar_conta(contas,usuarios,agencia):
  cpf = input("informe o CPF")
  usuario = validar_usuario(usuarios,cpf)

  if usuario:
    nr_conta = len(contas)+1
    print(f"Iniciando cadastro de conta para o usuario {cpf}!")
    return {"agencia":agencia, "conta":nr_conta,"usuario":usuario}
  
  else:
    print("Usuario não encontrado")




  

   
   

while True:

    opcao = input(menu)

    if opcao == "d":
      if(validaLimiteTransacoesDiaria(numero_transacoes)):
        numero_transacoes += 1 
        deposito = float(input("Digite o valor à ser depositado: "))
        deposito(deposito, saldo)
    
    elif opcao == "s":
      
     if(validaLimiteTransacoesDiaria(numero_transacoes)): 
        numero_transacoes += 1 
        print (f"Seu saldo atual é igual à R${saldo:.2F}.")
        saque = float(input(" Informe o valor que deseja sacar: "))
        saque(valor=saque, saldo=saldo)
        gravarExtrato("saque",saque)


      

    elif opcao == "e":
      exibir_extrato(saldo,extrato=extrato)
      

    elif opcao == "u":
      criar_usuario(usuarios)

    elif opcao == "c":
      conta = criar_conta(contas,usuarios,AGENCIA)  

      if conta:
        contas.append(conta)
        print ("Conta cadastrada")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
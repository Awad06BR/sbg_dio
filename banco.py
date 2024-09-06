menu = """############ SGB - v0.1 ###########
#                                 #
# [d]Depositar        [e]Extrato  #
#                                 #
# [s]Sacar            [i]Investir #
#                                 #
#                     [q] Sair    #
#                                 #
###################################
=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


def gravarExtrato(tipomovimentacao,valor):
  global extrato 
  extrato = extrato + (f"{tipomovimentacao}.....................R${valor:.2f}\n")

while True:

    opcao = input(menu)

    if opcao == "d":
      print("Digite o valor à ser depositado:")
      deposito = float(input("informe o valor: "))
      if(deposito>0):
        saldo += deposito
        print (f"Deposito Realizado! Seu novo saldo é: R${saldo:.2F}")
        gravarExtrato("deposito",deposito)
      else:
         print("Valor invalido! informe um valor positivo e maior que R$ 0,00.")

    elif opcao == "s":
      
      
      print (f"Seu saldo atual é igual à R${saldo:.2F}.")
      saque = float(input(" Informe o valor que deseja sacar: "))

      ultrapassou_limite = saque > limite
      ultrapassou_limite_saque = numero_saques >= LIMITE_SAQUES


      if(ultrapassou_limite):
         print("Valor de saque informado maior que o permitido!")
         
      
      elif(ultrapassou_limite_saque):
         print("Você ultrapassou o limite de saque!")
         

      elif (saque>0):
        saldo -= saque
        numero_saques += 1
        print(f"Saque realizado com sucesso! Seu novo saldo é R$ {saldo:.2F}.")
        gravarExtrato("saque",saque)
      else:
         print("Valor invalido, informe um novo valor!")

      

    elif opcao == "e":
      print("########## Extrato Bancario - v1.0 ##########")
      print("Não existe Movimentação" if not extrato else extrato)
      print(f"\n Saldo{saldo:.2f}" )
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
def obter_limite():
      print("Esta é a Loja de Bruno da Silva Batista") 
      print("_________________________________________")
      print("")
      print("Olá, agora iremos iniciar uma analise de crédito: ")
      print("") #Pula uma lina na saida 
      cargo = input("Cargo: ")
      salario = float(input("Salário: "))
      anonasc = int(input("Qual ano você nasceu? "))
      print ("Seu cargo é : {},  com salário de {:.2f},  nascido em:  {}".format(cargo,salario,anonasc))
      anoatual = int(2021)
      idadeaprox = anoatual - anonasc   #Calculo idade
      print("Idade aproximada: ", idadeaprox, "Idade")
      limitecompras = salario * (idadeaprox/1000)+100
      print("Limite disponivel é de: %.2f"%limitecompras)
      return (limitecompras, idadeaprox)
      print("")  #pula linha na saida
def verificar_produto(limite):
        print("")
        nome_produto = str(input("Nome produto:"))
        preco_produto = float(input("Preço do produto:"))
        nome_completo = str(input("Informe seu nome completo: "))
        tamanho_nome_completo = len(nome_completo)
        primeiro_nome = (nome_completo.split()[0])
        tamanho_primeiro_nome = len(primeiro_nome)
        print("Seu primeiro nome é: ",primeiro_nome)
        print("Seu primeiro nome tem",tamanho_primeiro_nome,"caracteres")
        print("Seu nome completo tem",tamanho_nome_completo,"caracteres")
        desconto=0 
        bloqueado=0 
        if preco_produto < (0.6*limite):
                print("Liberado!")
        elif preco_produto < (0.9*limite):
           
                print("Liberado ao parcelar em até 2 vezes")
        elif preco_produto < limite:
                print("Liberado ao parcelar em 3 ou mais vezes")
        else:
                print("Bloqueado")
                bloqueado=1
        if (not bloqueado):
            if (tamanho_nome_completo<preco_produto<idadeaprox):
                desconto = tamanho_primeiro_nome
                print("O desconto foi de: %d reais" %desconto)
                preco_produto = preco_produto - desconto
                print("Valor com desconto:%.2f" %preco_produto)
            else:
                print("Não há desconto.")
            limite-=preco_produto   
        print("")
        return(limite)
limitecompras, idadeaprox = obter_limite()
qtdade_produtos = int(input("Quantos produtos você deseja comprar? "))
for i in range(qtdade_produtos):
        limite = verificar_produto(limitecompras)
        print("Seu limite atualizado é de:%.2f"%limitecompras) 

input("Pressione qualquer tecla...")         


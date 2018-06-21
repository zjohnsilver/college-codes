## CODIGO      ESPECIFICACAO      PRECO
## 1           Cachorro Quente    R$ 4.00
## 2           X-Salada           R$ 4.50
## 3           X-Bacon            R$ 5.00
## 4           Torrada Simples    R$ 2.00
## 5           Refrigerante       R$ 1.50

## Com base nessa tabela, receba o codigo e a quantidade
## e informe ao usuario o valor a pagar.
## URI ONLINE - Problema 1038 - Iniciante
##
## Created by Jon on 07.03.2016
##

string = raw_input().split() ## Recebe dois valores

codigo = int(string[0])
qtd = int(string[1])

if codigo==1:
    print ("Total: R$ %.2f"%(qtd*4.00))
if codigo==2:
    print ("Total: R$ %.2f"%(qtd*4.50))
if codigo==3:
    print ("Total: R$ %.2f"%(qtd*5.00))
if codigo==4:
    print ("Total: R$ %.2f"%(qtd*2.00))
if codigo==5:
    print ("Total: R$ %.2f"%(qtd*1.50))

    









produto = input("Tipo de carne (File duplo, Alcatra, Picanha): ")
peso = float(input("Insira o peso (kg): "))

#função para definir preço por produto e peso promocional 
def valor_produto():
   if produto == "File duplo" and peso <= int(5):
      return 4.90
   elif produto == "File duplo" and peso > int(5):
      return 5.80
   elif produto == "Alcatra" and peso <= int(5):
      return 5.90
   elif produto == "Alcatra" and peso > int(5):
      return 6.80
   elif produto == "Picanha " and peso <= int(5):
      return 6.90
   elif produto == "Alcatra" and peso > int(5):
      return 7.80
   


total = valor_produto() * float(peso)

forma_pagamento = input("Pagamento realizado com cartão tabajara? ")


#função para definir possibilidade de desconto
def func_desconto():
  if forma_pagamento == "sim":
      return float(0.05)  
  else:
      return float(0)
  

  
valor = total * func_desconto()

print("Cupom Fiscal", "\n" "Produto: ", produto,"\n" "Quantidade: ",peso,"Kg","\n" "desconto: R$" ,func_desconto(), "\n" "Total: R$", valor)
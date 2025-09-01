preco_hamburguer = 8.00
preco_cheeseburger = 9.50
preco_fritas = 5.50
preco_refrigerante = 5.00
preco_milkshake = 8.00

quantidade_hamburguer = int(input("Quantos Hambúrgueres você consumiu? "))
quantidade_cheeseburger = int(input("Quantos Cheeseburgers você consumiu? "))
quantidade_fritas = int(input("Quantas Fritas você consumiu? "))
quantidade_refrigerante = int(input("Quantos Refrigerantes você consumiu? "))
quantidade_milkshake = int(input("Quantos Milkshakes você consumiu? "))

valor_hamburguer = quantidade_hamburguer * preco_hamburguer
valor_cheeseburger = quantidade_cheeseburger * preco_cheeseburger
valor_fritas = quantidade_fritas * preco_fritas
valor_refrigerante = quantidade_refrigerante * preco_refrigerante
valor_milkshake = quantidade_milkshake * preco_milkshake

valortotal = (valor_hamburguer + valor_cheeseburger +
               valor_fritas + valor_refrigerante + valor_milkshake)

print(f"\nO valor total da sua conta é: R$ {valortotal:.2f}\n")

print(f"{quantidade_hamburguer} x Hambúrguer ........... R$ {valor_hamburguer:.2f}")
print(f"{quantidade_cheeseburger} x Cheeseburger ........ R$ {valor_cheeseburger:.2f}")
print(f"{quantidade_fritas} x Fritas .................. R$ {valor_fritas:.2f}")
print(f"{quantidade_refrigerante} x Refrigerante .......... R$ {valor_refrigerante:.2f}")
print(f"{quantidade_milkshake} x Milkshake .............. R$ {valor_milkshake:.2f}")

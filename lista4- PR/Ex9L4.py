x1 = int(input("Digite o 1º valor: "))
x2 = int(input("Digite o 2º valor: "))
x3 = int(input("Digite o 3º valor: "))
x4 = int(input("Digite o 4º valor: "))

x1 = x1 + x2
x3 = x3 - x4

x2 = x1 + x3

if x2 > 10:
    print(x2 , " é maior que 10")

else:
    print(x2 , " é menor ou igual a 10")
                        

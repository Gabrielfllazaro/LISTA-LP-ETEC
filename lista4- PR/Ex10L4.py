x = int(input("Digite o 1º valor: "))
y = int(input("Digite o 2º valor: "))


if x < y:
    x = x * 10
    y = y / 2
   

elif x > y:
    y = y * 10
    x = x / 2
    

x = x + y
if x % 2 == 0:
    print(x, "é par")
else:
    print(x, "é ímpar")





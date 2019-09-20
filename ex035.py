print('-='*20)
print('Analizador de Triângulos')
print('-='*20)
a = int(input("Primeira reta: "))
b = int(input("Segunda: "))
c = int(input("Terceira: "))

if (a+b) > c and (a+c) > b and (b+c) > a:
    print("Forma um triângulo")
else:
    print('Não é um triângulo')
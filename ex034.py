n = float(input('Qual o seu salário: '))

if n <= 1250.00:
    total = n + (n*15/100)
else:
    total = n + (n*10/100)
print('Total do aumento foi: R${:.2f}'.format(total))

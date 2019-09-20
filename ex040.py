n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('\033[31mREPROVADO\033[m')
elif media >= 7:
    print('\033[32mAPROVADO\033[m')
else:
    print('\033[33mRECUPERAÇÃO')

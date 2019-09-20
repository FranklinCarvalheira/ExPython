n = float(input('Digite a velocidade: '))

if n > 80:
    total = (n - 80) * 7
    print('Você foi multado')
    print('Total a pagar {:.2f}' .format(total))
else:
    print('Sem multa')

n = float(input('Distância da viagem: '))
'''
if n <= 200:
    total = n * 0.50
else:
    total = n * 0.45
 '''
total = n * 0.50 if n <= 200 else n * 0.45
print('Total: R${:.2f}'.format(total))

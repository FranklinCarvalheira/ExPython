valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int (input('Em quantos anos você pretende pagar: '))

mes = anos * 12
prestacao = valor / mes

exceder = salario * 30 / 100

if prestacao <= exceder:
    print('\033[33m-=\033[m' * 20)
    print('\033[32mEmprestimo aprovado\033[m')
    print(' Você pagara em {} prestações, {} anos, um valor de R${:.2f}'.format(mes, anos, prestacao))
    print('\033[33m-=\033[m' * 20)
else:
    print('\033[31m-=\033[m' * 20)
    print('\033[31mEmpréstimo negado!!!\033[m')
    passa = prestacao - salario
    print('Prestação ultrapassa os 30% do seu salário em R${:.2f}'.format(passa))
    print('\033[31m-=\033[m' * 20)

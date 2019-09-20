from datetime import date

data_atual = date.today()
ano = data_atual.year

n = int(input('Que ano você nasceu: '))
total = ano - n

if total < 18:
    falta = 18 - total
    print("Ainda vai se alistar no serviço militar")
    print('Falta {} anos para o seu alistamento'.format(falta))
elif total == 18:
    print('Ano do seu alistamento')
else:
    falta = total - 18
    print('\033[32mMocorango!!!!\033[m já passou a data do seu alistamento em {} anos'.format(falta))
    print('Ta preso guerreiro')

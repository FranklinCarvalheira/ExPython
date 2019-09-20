nome = str(input('Digite seu nome completo: ')).strip()

print('Maiúsculo {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))
print('Total de letras: {}'.format(len(nome) - nome.count(' ')))
#print('Primeiro nome: {}' .format(nome.find(' ')))
#ou
separa = nome.split()
print('Seu promeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))
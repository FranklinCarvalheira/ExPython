from math import radians, sin, cos, tan
a = float(input("Digite um angulo: "))
seno = sin(radians(a))
coss = cos(radians(a))
tang = tan(radians(a))

print("Seno {:.2f}\ncosseno {:.2f}\nTangente{:.2f}" .format(seno, coss, tang))

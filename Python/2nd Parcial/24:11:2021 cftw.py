print('Areas que puedo calcular: triangulo, rectangulo, pentagono.' )

print('Triangulo')
b=int(input('Pon la medida de la base:'))
altura=int(input('Pon la medida de la altura:'))
print('El Are de triangulo es:',(b*altura/2))

print('Rectangulo')
b1=int(input('Pon la medida de la base:'))
altura1=int(input('pon la medida de la altura:'))
print('El area del rectangulo es:',(b1*altura1))

print('Pentagono')
p=int(input('Pon la medida del perimetro:'))
apo=int(input('Pon la medida del apotema:'))
print('Multiplicar el perimetro por los lados del pentagono:',(p*p))
print('Multiplicar perimetro por apotema y dividirlo entre 2:',(p*p*apo/2))
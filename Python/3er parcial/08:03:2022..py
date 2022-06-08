import random
 #agregar el resto del abecedario

 #volver el codigo infinito usando un while True
base="abcdefghijklmnopqrstuvwxyz"

passw=""
  
 #permite que el usuario seleccione la longitud de su password
while True:
  for i in range (7):
    passw=passw+random .choice(base)
  print("password:", passw)
  input()



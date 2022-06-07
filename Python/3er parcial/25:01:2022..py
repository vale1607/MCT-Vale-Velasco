compara=9

while True:
  numero=int(input('Calification 1: '))
  numero2=int(input('Calification 2: '))
  numero3=int(input('Calification 3: '))
  
  print('The sum total is:', (numero+numero2+numero3))

  print('Your avarage is: ', (numero+numero2+numero3/3))

  if(numero==9):
    print("You did it")
    
  else:
    print("You fail")
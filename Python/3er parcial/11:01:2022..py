#generen un codigo que adivine un numero, si te pasas avisa, si te falta avisa, y si le atinas di felicidades
#debe ser infinito

while True:
  v= int(input("Guess the number "))
  number=21

if(v<21):
  print("It's a bigger number")

if (v>21):
  print("It's a smaller number")

if (v==21):
  print('Congratulations')






import datetime

dia= datetime.date.today()

w= dia.weekday()+1

if(w==0):
  print('Feliz Domingo')

elif(w==2):
  print('Yuju Es Martes')

else:
  print ("Yahoo Es Sabado")
  

import datetime

dia= datetime.date.today()

w= dia.weekday()+1

if(w==0):
  print('Feliz Lunes')

elif(w==2):
  print('Yuju Es Viernes')

elif(w==4):
  print('Siiii es Jueves')

else:
  print ("Yahoo Es Miercoles")
  


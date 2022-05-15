#!/usr/bin/python3.8

# Calcular numeros perfectos
#
# Los numeros perfectos son aquellos iguales a la suma de sus divisores
# ej: 6 = 1 + 2 + 3

from datetime import datetime

i=2
divisor=0
suma=1
strSuma=""

while True:
	suma=1
	divisor=i-1
	#print ("*** Revision del numero "+str(i)+"***")
	while divisor > 1:
		if i%divisor == 0:
			#print ("Encontrado divisor de "+str(i)+": "+str(divisor))
			suma = suma + divisor
			strSuma=strSuma+str(suma)+"+"
			#print ("Suma de divisores: "+str(suma))
		divisor=divisor-1
	if suma == i:
		print ("*********************************")
		print (str(datetime.now()))
		print(str(i)+" es un numero perfecto.")
		#print(i)
		#print(strSuma)
		#print()
	i=i+1

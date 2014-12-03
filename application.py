#-*- coding: utf-8-*-
#******************************************************************
#********************Número Factoria*******************************
#******************************************************************
print "NUMERO FACTORIAL RECURSIVO"
#******************************************************************
def factorial(n):  
	if n == 0 or n == 1:
		resultado = 1
	elif n > 1:
		resultado = n*factorial(n-1)
	return resultado

numero=int(input("Ingrese Numero: "))
print "Su Factorial es: %s"%factorial(numero)


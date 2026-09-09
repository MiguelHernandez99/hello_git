print("hola git")
print("un cambio")
#otro cambio
#---------------------->
cantidad_numeros = int(input("¿Cuantos numeros de Fibonacci quieres?"))

if cantidad_numeros <= 0:
	print('El numero debe ser > a 0!!!')
else:
	a = 0
	b = 1
	print('Los primeros', cantidad_numeros, "numeros de Fibonacci son:")
	for i in range(cantidad_numeros):
		print(a)
		siguiente = a + b
		a = b
		b = siguiente




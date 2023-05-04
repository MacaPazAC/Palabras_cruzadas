"""Palabras cruzadas
debe pedir 2 palabras y contar cuantas coincidencias existen
Ejemplo:
palabra1 = "hola"
palabra2 = "hola como estas"
h = 2
o = 3
l = 2
a = 3"""

contador = 0
palabra1 = input("Ingrese palabra1:")
palabra2 = input("Ingrese palabra2:")
for letra1 in palabra1: 
  #print(letra1)
	contador = 0 #reinicio
	for letra2 in palabra2:
		#print(letra2)
		if letra1 == letra2:
			contador = contador + 1
	
print("La letra " + letra1 + "aparece" + str(contador))



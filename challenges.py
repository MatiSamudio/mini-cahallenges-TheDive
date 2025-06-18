# Dia 1 - Inversión de una Cadena 
# Escribe un programa que invierta una cadena de caracteres dada por el 
# usuario. 

# #metodo 1
# text = input("Ingresa palabra/oracion: ")

# invert_text = text[::-1]

# print("Tu palabra/oracion invertida: ", invert_text)

# #metodo 2
# text = input("Ingrea palabra/oracion para invertir caracteres : ")

# invert_text = ""

# for i in range(len(text) - 1, -1, -1):
#     invert_text += text[i]

# print("Tu palabra/oracion invertida: ", invert_text)



# Dia 2 - Tabla de Multiplicar 
# Escribe un programa que muestre la tabla de multiplicar de un número 
# dado por el usuario. 

# num = int(input("Ingresa numero: "))

# print(f"Tabla de multiplicar del numero {num}\n")
# for i in range(1, 11):
#     result = num * i
#     print(f"{numero} x {i} = {result}")



# Dia 3 - Contar Vocales 
# Escribe un programa que cuente el número de vocales en una cadena 
# dada. 

# text = input("Ingresa cadena: ").lower()

# vocals = "aeiou"

# vocals_amount = 0

# for letra in text:
#     if letra in vocals:
#         vocals_amount += 1

# print("Cantidad de vocales en tu cadena: ", vocals_amount)



# Dia 4 -  Ordenar Lista 
# Escribe un programa que ordene una lista de números dada por el usuario 
# en orden ascendente. 

# nums_des_ord = input("Ingresa numeros separados por comas o espacios: (Ej:1,2,3. 1 2 3)")

# nums_des_ord = nums_des_ord.replace(","," ")


# nums_ord = [int(n) for n in nums_des_ord.split()]

# nums_ord.sort()

# print("Lista Ordenada: ", nums_ord)



# Dia 5 -  Crear un Diccionario 
# Escribe un programa que cree un diccionario a partir de dos listas dadas: 
# una de claves y otra de valores. 

# keys_input = input("Ingresa claves, separadas por comas: ")
# values_input = input("Ingresa valores, separadas por comas: ")


# keys = keys_input.split(",")
# values = values.split(",")

# dictionary = dict(zip(keys, values))

# print("Diccionario creado: ")
# print(dictionary)



# Dia 6 -  Conversión de Temperatura 
# Escribe un programa que convierta una temperatura dada en grados 
# Celsius a grados Fahrenheit. 

## formula para pasar a fahrenheit = C * 9/5) + 32

# celsius = float(input("Ingresa la temperatura en grados celsius: "))

# fahrenheit = (celsius * 9/5) + 35

# print(f"{celsius}°C equivale a {fahrenheit}°F")





import random
import string

while True:
    amount = input("Cuantas contrasenhas queres generar?: ")
    if amount.isdigit() and int(amount) > 0:
        amount = int(amount)
        break
    print("Ingresa un numero mayor a 0")


while True:
    longitud = input("longitud para la contrasenha")
    if longitud.isdigit():
        longitud = int(longitud)
        if 8 <= longitud <= 16:
            break
    
    print("Ingreesa uun numero entre 8 y 16")


mayus = string.ascii_uppercase
minus = string. ascii_lowercase
nums = string.digits
symbols = string.punctuation
everything = mayus + minus + nums + symbols


print("\nContrasenhas generadas: ")

for i in range(amount):
    password = [
        random.choice(mayus),
        random.choice(minus),
        random.choice(nums),
        random.choice(symbols)
    ]

    rest = longitud - len(password)
    password += random.choices(all, k=rest)
    random.shuffle(password)
    print(f"{i+1}: {''.join(password)}")

import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("¿De que longitud queres la contraseña?"))
contrasena = "H"
for i in range(longitud):
    numero = random.randint(1,71)
    if i == 0:
        contrasena = caracteres[numero]
    else:
        contrasena += caracteres[numero]
print(contrasena)

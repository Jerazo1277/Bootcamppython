x=5
if x > 5:
    print("x es mayor que 5")
elif x == 5:
   print("x es igual a 5")
#else:
#    print("x es menor o igual a 5")
x = 15
y = 26
"""if x > 10 and y > 25: # ambas condiciones deben ser verdaderas
    print("x es mayor que 10 y y es mayor que 25")
if x > 10 or y > 25: # una de las dos debe ser verdadera
    print("x es mayor que 10 o y es mayor que 25")
if not x>10:
    print("x es menor o igual a 10")"""
is_member = True
age = 15

if is_member:
    if age >= 15:
    print("Es miembro")
else:
    print("No puedes entrar a la fiesta")
else:
    print("No es miembro y no tienes acceso")
    if age >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("No es miembros")
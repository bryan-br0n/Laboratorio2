print("-------------------------------------------------------------------------")
print("Bienvenido al programa para determinar que numero es mayor, medio y menor")
print("-------------------------------------------------------------------------")

num1 = int(input("Dame un numero -> "))
num2 = int(input("Dame un segundo numero -> "))
num3 = int(input("Dame un tercer numero -> "))

if num1 >= num2 and num1 >= num3:
    maxnum = num1
elif num2 >= num1 and num2 >= num3:
    maxnum = num2
else:
    maxnum = num3
    
if num1 <= num2 and num1 <= num3:
    minnum = num1
elif num2 <= num1 and num2 <= num3:
    minnum = num2
else:
    minnum = num3
    
mednum = num1 + num2 + num3 - maxnum - minnum

print("El numero ", maxnum, "es el mas grande de los 3")
print("El numero ", minnum, "es el menor de los 3")
print("El numero medio ", mednum, "es el numero medio")

print("Fin :)")
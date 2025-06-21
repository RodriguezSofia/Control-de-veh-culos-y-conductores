#RONDA 1
#Ejercicio 9
print("Verificador de palindromos")
word=input("Ingrese una palabra a identificar: ").lower()
if word == word[::-1]:
    print(f"la palabra {word} es un polindromo")
else:
    print(f"La palabra {word} NO es un polindromo")
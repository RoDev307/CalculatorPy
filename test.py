Opciones = ['1.Suma', '2.Resta', '3.Multiplicacion', '4.Division']
print("Bienvenido a la calculadora en Python")
print(Opciones[0])
print(Opciones[1])
print(Opciones[2])
print(Opciones[3])
try:
    Operacion= int(input("Escoja su operacion a realizar "))
    if Operacion <=1:
        print("Opcion escojida: ", Opciones[0])
        Num1 = int(input("Ingrese su primer numero: "))
        Num2 = int(input("Ingrese su primer numero: "))
        Resultado = Num1 + Num2
        print("Resultado: ", Resultado)

    elif Operacion <=2:
        print("Opcion escojida: ", Opciones[1])
        Num1 = int(input("Ingrese su primer numero: "))
        Num2 = int(input("Ingrese su primer numero: "))
        Resultado = Num1 - Num2
        print("Resultado: ", Resultado)

    elif Operacion <=3:
        print("Opcion escojida: ", Opciones[2])
        Num1 = int(input("Ingrese su primer numero: "))
        Num2 = int(input("Ingrese su primer numero: "))
        Resultado = Num1 * Num2
        print("Resultado: ", Resultado)
    
    elif Operacion <=4:
        print("Opcion escojida: ", Opciones[3])
        Num1 = int(input("Ingrese su primer numero: "))
        Num2 = int(input("Ingrese su primer numero: "))
        Resultado = Num1 / Num2
        print("Resultado: ", Resultado)
except ValueError:
    print("Numero invalido, ingrese un numero entero")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

match operacion:
    case "+":
        print("Resultado:", num1 + num2)
    case "-":
        print("Resultado:", num1 - num2)
    case "*":
        print("Resultado:", num1 * num2)
    case "/":
        if num2 == 0:
            print("Error: División por cero")
        else:
            print("Resultado:", num1 / num2)
    case _:
        print("Operación no válida.")

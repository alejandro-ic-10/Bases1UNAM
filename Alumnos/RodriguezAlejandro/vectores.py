import math


def sumaVectors(v1, v2):
    resul = []
    for i in range(len(v1)):
        resul.append(v1[i] + v2[i])
    return resul


def restaVectors(v1, v2):
    resul = []
    for i in range(len(v1)):
        resul.append(v1[i] - v2[i])
    return resul

def productoVectors(v, e):
    resul = []
    for i in range(len(v)):
        resul.append(v[i]*e)
    return resul

def normaVectors(v):
    resul=0
    for i in range(len(v)):
        resul+=v[i]*v[i]
    resul = resul**(1/2)
    return resul

def anguloVectors(v1, v2):
    resul=0
    v1N = normaVectors(v1)
    v2N = normaVectors(v2)
    for i in range(len(v1)):
        resul+=v1[i]*v2[i]
    resul1 = resul/(v1N*v2N)
    resul1 = math.degrees(math.acos(resul1))
    return resul1

opcion = 0
while opcion != 6 and opcion < 6:
    resul = []
    resul1 = 0
    menu = "\nCALCULADORA DE VECTORES\n 1.SUMA\n 2.RESTA\n 3.PRODUCTO CON UN ESCALAR\n 4.NORMA\n 5.ANGULO ENTRE DOS VECTORES\n 6.SALIR"
    print(menu)
    opcion = int(input("\nIngresa el numero de la operacion que quieras realizar: \n"))

    if opcion == 1:
        vec1 = input("Ingresa tu primer vector (separando los valores por comas)\n") 
        vec2 = input("Ingresa tu segundo vector (separando los valores por comas)\n")
        vec1 = vec1.split(',')
        vec2 = vec2.split(',')
        vec1 = list(map(int, vec1))
        vec2 = list(map(int, vec2))
        resul = sumaVectors(vec1, vec2)
        print(resul)

    elif opcion == 2:
        vec1 = input("Ingresa tu primer vector (separando los valores por comas)\n") 
        vec2 = input("Ingresa tu segundo vector (separando los valores por comas)\n")
        vec1 = vec1.split(',')
        vec2 = vec2.split(',')
        vec1 = list(map(int, vec1))
        vec2 = list(map(int, vec2))
        resul = restaVectors(vec1, vec2)
        print(resul)

    elif opcion == 3:
        vec1 = input("Ingresa tu primer vector (separando los valores por comas)\n") 
        vec2 = int(input("Ingresa tu escalar\n"))
        vec1 = vec1.split(',')
        vec1 = list(map(int, vec1))
        resul = productoVectors(vec1, vec2)
        print(resul)

    elif opcion == 4:
        vec1 = input("Ingresa tu vector (separando los valores por comas)\n") 
        vec1 = vec1.split(',')
        vec1 = list(map(int, vec1))
        resul1 = normaVectors(vec1)
        print("{0:.2f}".format(resul1))

    elif opcion == 5:
        vec1 = input("Ingresa tu primer vector (separando los valores por comas)\n") 
        vec2 = input("Ingresa tu segundo vector (separando los valores por comas)\n")
        vec1 = vec1.split(',')
        vec2 = vec2.split(',')
        vec1 = list(map(int, vec1))
        vec2 = list(map(int, vec2))
        resul1 = anguloVectors(vec1, vec2)
        print(resul1)
    
    else:
        print("\nMuchas gracias!")


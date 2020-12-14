# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:45:43 2020
 Alvaro Muruchi
"""
# In[]
"""
Para realizar la maximizacion de la poblacion usando la 
funcion y= x**3+x**2+x, se realiza el cruce de dos 
instancias aleatorias de entre 1-20, cruzando los primeros 
digitos de su complemento en binario y posteriormente 
mutando el penultimo digito del correspondiente cruce 
"""
# In[]

def conversion (num):
    lista = []
    if num == 0:
        resultado = "0"
    else:
        while num >= 1:
            lista.insert(0, num%2)
            num = num // 2
        resultado = "".join(str(i) for i in lista)
    return resultado

def complemento (lista):
    lista2 = []
    for i in range(10):
        while len(lista[i]) < 6:
            lista[i] = "0" + lista[i]
        lista2.append(lista[i])
    return lista2

import random

def cruce (lista):
    a = 0
    ls = []
    aux1 = ""
    aux2 = ""
    aux3 = ""
    aux = ""
    while a < 10:
        aux2 = lista[0][a]
        print(a,'->',aux2)
        aux3 = lista[0][a + 1]
        print((a+1),'->',aux3,'\n')
        aux1 = aux3[:2] + aux2[2:]
        print(a,'->',aux1)
        aux = aux2[:2] + aux3[2:]
        print((a+1),'->',aux,'\n')
        ls.append(aux1)
        ls.append(aux)
        a = a + 2
    return ls


def mutacion (lista):
    aux = ""
    i = 0
    while i < 10:
        aux = lista[0][i]
        if aux[4] == '0':
            lista[0][i] = aux[:4] + '1' + aux[5:]
        else:
            lista[0][i] = aux[:4] + '0' + aux[5:]
        i = i + 1
    return lista

def binario_a_decimal(numero_binario):
    numero_decimal = 0
    for posicion, digito_string in enumerate(numero_binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal



x = []
binX = []
comp =[]
cruc = []
mutac = []
func = []
cont = 1
for i in range(10):
    x.append(random.randint(0, 20))
while(cont <= 3):
    print("\n GENERACION N°",cont)
    print(x)
    x.sort()
    x.reverse()
    print(x)
    for i in range(10):
        binX.append(conversion(x[i]))
    for i in range(10):
        func.append(x[i]*x[i]*x[i] + x[i]*x[i] + x[i])
    print("\n Funcion aplicada a poblacion : ")
    print(func,'\n')
    print(binX)
    comp.append(complemento(binX))
    print(comp)
    cruc.append(cruce(comp))
    print('Origen: ',comp)
    print('Cruce: ',cruc)
    mutac.append(mutacion(cruc))
    print('Mutacion: ',mutac)
    for i in range(10):
        x[i] = binario_a_decimal(mutac[0][0][i])
    print(x)
    cont+=1
    binX = []
    comp =[]
    cruc = []
    mutac = []
    func = []


#https://docs.google.com/forms/d/e/1FAIpQLSdQfRSXNn0p4e2xzwHMdHiRE1C2W0rrh1c2AtB2bEGnZ2HdPw/viewform

'''
16
13
Regresa 0 cuando n es múltiplo de 3, o 1 en caso contrario
O(N + M) time, O(N + M) space
se ejecuta pero no da el resultado correcto
'''


#def calcula(n):
#    if n == 4:
#        return n
#    else:
#        return 2* calcula(n+1)    

# print(calcula(2))


#def calcula(x,y):
#    if x == 0:
#        return y
#    else:
#        return calcula(x-1,x+y)    

#print(calcula(4,3))

#def calcula(n):
#    if (n == 0 or n == 1):
#        return n
#    if (n%3 != 0):
#        return 0
    
#    return calcula(n/3)

#print(calcula(300))




'''
def parentesisAnindados(n):
    cadena="{"
    for i in range(0,n):
        cadena+="{}"
    cadena+="}"
    return cadena
    

def parentesisBalanceados(n):
    cadena=""
    if type(n) is int:
        if n > 0:
            for i in range(0,n):
                cadena += "{}"   
            if n > 1:
                cadena+=","+parentesisAnindados(n-1)    
    else:
        cadena= "SOLO NUMEROS ENTEROS"
    return cadena   

print(parentesisBalanceados(3))
'''
'''
def superDigito(n,m,z=1):
    if len(str(n)) > 1:
        if z:
            n=str(n)*m
        suDigito=0
        for digito in str(n):
            suDigito+=int(digito)    
        return superDigito(suDigito,m,0) if (len(str(suDigito)) > 1) else suDigito  
    else:
        return n  

print(superDigito(148,3))    
'''

def substrings(cad,pos):
    arreglo=[]
    for letra in cad:
        arreglo.append(letra)
    return arreglo

print(substrings("dbac",3))
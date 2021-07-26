def recur_fibo(n: int):
    lista=[0,1]
    listacubo=[0,1]
    for x in range(2, n):
        if len(lista)==n:
            break
        acum=1
        for y in lista:
            suma= y+acum
            acum=suma
            lista.append(suma)
            listacubo.append(suma**3)
            if len(lista)==n:
                break
    return lista, listacubo
    
# def iniciar_aplicacion(n: int):
#     resultado = list ( map(lambda elemento : elemento**3, recur_fibo(n)) ) 
#     return resultado

print(recur_fibo(5))
# print(iniciar_aplicacion(5))
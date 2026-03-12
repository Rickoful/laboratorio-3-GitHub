import sys

def resolver():
    MAX = 10000000
    
    primo = [True] * (MAX + 1)
    primo[0] = False
    primo[1] = False

    for i in range(2, 3163):
        if primo[i]:
            for j in range(i * i, MAX + 1, i):
                primo[j] = False

    conteo_primos = [0] * (MAX + 1)
    contador = 0
    for i in range(MAX + 1):
        if primo[i]:
            contador += 1
        conteo_primos[i] = contador

    datos = sys.stdin.read().split()
    if not datos:
        return
        
    t = int(datos[0])
    idx = 1
    
    salida = []
    for _ in range(t):
        a = int(datos[idx])
        b = int(datos[idx+1])
        idx += 2
        
        if a == 0:
            respuesta = conteo_primos[b]
        else:
            respuesta = conteo_primos[b] - conteo_primos[a - 1]
            
        salida.append(str(respuesta))
        
    print('\n'.join(salida))

if __name__ == '__main__':
    resolver()
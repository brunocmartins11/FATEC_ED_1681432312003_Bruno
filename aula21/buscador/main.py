import time

inicio = time.time()
def busca(valor, array):
    for i, num in enumerate(array):
        if num == valor:
            return i
    return -1

elementos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

numero = int(input("Digite o número que deseja encontrar: "))

posicao = busca(numero, elementos)

if posicao == -1:
    print(-1)
else:
    print(posicao)

fim = time.time()

print(fim - inicio)
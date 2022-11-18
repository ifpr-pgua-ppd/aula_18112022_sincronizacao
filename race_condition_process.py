from multiprocessing import Process, Value

def soma(n):
    for a in range(1000):
        n.value += 1.0

def subtracao(n):
    for a in range(1000):
        n.value -= 1.0


if __name__ == '__main__':
    #a classe Value aceita como parâmetro o tipo de dado (i=inteiro,d=double) e também 
    #se um objeto lock será inicializado para auxiliar no controle de acesso do 
    #dado compartilhado
    num = Value('d', 0.0)

    pSoma = Process(target=soma, args=(num,))
    pSoma.start()
    
    pSubtracao = Process(target=subtracao, args=(num,))
    pSubtracao.start()
    
    pSoma.join()
    pSubtracao.join()

    print(num.value)
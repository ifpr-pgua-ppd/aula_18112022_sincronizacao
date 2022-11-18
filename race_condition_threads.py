from threading import Thread

contador=0
repeticoes=1000000

def incrementa():
    global contador
    #print("Incrementando...")
    contador += 1

def decrementa():
    global contador
    #print("Decrementando...")
    contador -= 1

def incrementador(): #será executado pela thread 01
    for i in range(repeticoes):
        incrementa()

def decrementador(): #será executado pela thread 02
    for i in range(repeticoes):
        decrementa()

def main():
    global contador

    print("Iniciando testes...")
    t1 = Thread(target=incrementador)
    t2 = Thread(target=decrementador)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Resultado final {contador}")

main()


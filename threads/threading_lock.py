from threading import Thread, Lock

contador=0
repeticoes=10000000
lock = Lock()

# região crítica
def incrementa():
    global contador
    contador +=1

# região crítica
def decrementa():
    global contador
    contador -=1

def incrementador(): #será executado pela thread 01
    for i in range(repeticoes):
        lock.acquire()  #solicita acesso a região crítica
        incrementa()
        lock.release() #libera acesso a região crítica

def decrementador(): #será executado pela thread 02
    for i in range(repeticoes):
        lock.acquire() #solicita acesso a região crítica
        decrementa()
        lock.release() #libera acesso a região crítica


if __name__=="__main__":

    print("Iniciando testes...")
    t1 = Thread(target=incrementador)
    t2 = Thread(target=decrementador)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Resultado final {contador}")

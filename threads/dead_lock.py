from threading import Thread,Lock
import threading
import time
import random

contador=0
repeticoes=100000
lock1 = Lock()
lock2 = Lock()

def incrementa():
    global contador
    print("Incrementou...")
    contador +=1
    
def decrementa():
    global contador
    print("Decrementou...")
    contador -=1
    
def incrementador():
    name = threading.current_thread().name
    for i in range(repeticoes):
        print(f"{name} - adquirindo Lock01")
        lock1.acquire()
        print(f"{name} - adquirindo Lock02")
        lock2.acquire()
        incrementa()
        lock1.release()
        lock2.release()
        print(f"{name} - finalizei!!")

def decrementador():
    name = threading.current_thread().name
    for i in range(repeticoes):
        print(f"{name} - adquirindo Lock02")
        lock2.acquire()
        print(f"{name} - adquirindo Lock01")
        lock1.acquire()
        decrementa()
        lock2.release()
        lock1.release()

if __name__=="__main__":

    print("Iniciando testes...")
    t1 = Thread(target=incrementador)
    t2 = Thread(target=decrementador)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Resultado final {contador}")

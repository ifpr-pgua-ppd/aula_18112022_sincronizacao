from threading import Thread,Semaphore
import time
import random

item=0
semaforo=Semaphore(1)

def consumidor():
    global item
    print("aguardando produção...")
    semaforo.acquire()
    print(f"consumindo item {item}")

def produtor():
    global item
    time.sleep(1)
    item = random.randint(0,10000)
    print(f"produzindo item {item}")
    semaforo.release()

if __name__ == '__main__':
    for i in range (0,5) :
        t1 = Thread(target=produtor)
        t2 = Thread(target=consumidor)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    
    print ("program terminated")
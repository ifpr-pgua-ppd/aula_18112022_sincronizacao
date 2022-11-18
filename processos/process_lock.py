from multiprocessing import Process, Lock
import random
import time

def impressao(id, lock):
    
    time.sleep(random.randint(1,5))
    lock.acquire()
    for i in range(5):
        print(f'{id} msg {i}')
        time.sleep(random.randint(1,2))
    lock.release()
    

if __name__=="__main__":

    l = Lock()
    nProcs = 10
    print("Iniciando testes...")
    
    procs = []

    for i in range(nProcs):
        p = Process(target=impressao,args=(i,l))
        procs.append(p)
        p.start()

    
    for p in procs:
        p.join()


    print("Fim!")

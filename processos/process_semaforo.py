from multiprocessing import Process,Semaphore
import multiprocessing
import time
import random
from datetime import datetime

def processamento(pid,sem):

    #pid = multiprocessing.current_process().pid

    for i in range(10):
        sem.acquire()
        print(f"{pid} fazendo consulta {datetime.now()}")
        #simulando uma consulta longa
        time.sleep(5)
        sem.release()
        #simulando um processamento qualquer
        time.sleep(random.uniform(1,3))


if __name__=="__main__":
    MAX_CON = 3

    sem = Semaphore(3)
    nProcs = 10
    print("Iniciando testes...")
    
    procs = []

    for i in range(nProcs):
        p = Process(target=processamento,args=(i,sem))
        procs.append(p)
        p.start()

    
    for p in procs:
        p.join()


    print("Fim!")
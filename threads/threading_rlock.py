from threading import Thread,RLock, Lock
import time

class Caixa():
    lock = RLock()

    def __init__(self):
        self.total_items=0
    
    def execute(self,v):
        Caixa.lock.acquire()
        self.total_items += v
        Caixa.lock.release()
    
    def add(self):
        Caixa.lock.acquire()
        self.execute(1)
        Caixa.lock.release()
    
    def remove(self):
        Caixa.lock.acquire()
        self.execute(-1)
        Caixa.lock.release()
        
def adicionador(caixa,items):
    while(items > 0):
        print("Adicionando 1 na caixa...")
        caixa.add()
        time.sleep(1)
        items -=1

def removedor(caixa,items):
    while(items > 0):
        print("Removendo 1 da caixa...")
        caixa.remove()
        time.sleep(1)
        items -=1


if __name__=="__main__":

    caixa = Caixa()
    items = 10

    t1 = Thread(target=adicionador,args=(caixa,items))
    t2 = Thread(target=removedor,args=(caixa,items))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Resultado final:{}".format(caixa.total_items))
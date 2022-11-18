from threading import Thread, Semaphore
import time
import random

class Garfo(Semaphore):

    def __init__(self):
        Semaphore.__init__(self)
        self.usado = False
    
    def pegar(self,esperar):
        return self.acquire(esperar)
        
        
    def soltar(self):
        self.release()


class Filosofo(Thread):

    def __init__(self, id:int, esquerda:Garfo, direita:Garfo) -> None:
        Thread.__init__(self)
        self.id = id
        self.esquerda = esquerda
        self.direita = direita

    def pensar(self):
        print(f"Filosofo {self.id} pensando...")
        time.sleep(random.uniform(1,5))
    
    def comer(self):
        print(f"Filosofo {self.id} comendo...")
        time.sleep(random.uniform(2,3))
    

    def soltar(self):
        print(f"Filosofo {self.id} soltando...")
        self.esquerda.soltar()
        self.direita.soltar()

    def pegar(self):
        print(f"Filosofo {self.id} pegando...")
        while(True):
            self.esquerda.pegar(True)
            pegou = self.direita.pegar(False)
            if(pegou):
                return True
            self.esquerda.soltar()
        
    def run(self):
        while(True):
            self.pensar()
            if (self.pegar()):
                self.comer()
                self.soltar()


if __name__ == '__main__':

    NUM_FILOSOFOS = 5

    garfos = []
    filosofos = []

    #inicializa garfos
    for g in range(NUM_FILOSOFOS):
        garfos.append(Garfo())
    
    for f in range(NUM_FILOSOFOS):
        esquerda = garfos[f-1]
        direita = garfos[f]

        filosofos.append(Filosofo(f, esquerda,direita))
    

    for f in filosofos:
        f.start()
    
    for f in filosofos:
        f.join()
    
    print("Fim...")

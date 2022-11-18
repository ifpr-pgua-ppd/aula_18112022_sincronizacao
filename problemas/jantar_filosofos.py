from threading import Thread
import time

class Garfo():

    def __init__(self):
        self.usado = False
    
    def pegar(self):
        if(not self.usado):
            self.usado = True
            return True
        
        return False
    
    def soltar(self):
        self.usado = False

class Filosofo(Thread):

    def __init__(self, id:int, esquerda:Garfo, direita:Garfo) -> None:
        Thread.__init__(self)
        self.id = id
        self.esquerda = esquerda
        self.direita = direita

    def pensar(self):
        #print(f"Filosofo {self.id} pensando...")
        time.sleep(0.5)
    
    def comer(self):
        print(f"Filosofo {self.id} comendo...")
        time.sleep(0.5)
    

    def soltar(self):
        #print(f"Filosofo {self.id} soltando...")
        self.esquerda.soltar()
        self.direita.soltar()

    def pegar(self):
        while(not self.esquerda.pegar()):
            #print(f"Filosofo {self.id} aguardando esquerda...")
            time.sleep(0.5)
        
        while(not self.direita.pegar()):
            #print(f"Filosofo {self.id} aguardando direita...")
            time.sleep(0.5)
            

        return True
        
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

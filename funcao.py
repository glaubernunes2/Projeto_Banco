
#Aqui vai fica as funções pro banco

class Banco():
    
    def __init__(self,):
        self.__saldo = 10
   
        
    
    @property
    def VerSaldo(self): 
        return print(self.__saldo)  
         
    @property
    def Fazer_Deposito(self):
       pass
    @Fazer_Deposito.setter
    def Fazer_Deposito(self,valor):
        self.__saldo += valor
        
        

    @property 
    def Fazer_saque(self):
        pass
    @Fazer_saque.setter
    def Fazer_saque(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
           
            
        else:
            print('Saldo insuficiente')
            
    



#Aqui vai fica as funções pro banco
class Banco():
    def __init__(self,):
        self.__saldo = 0
        

    
        
    
    @property
    def VerSaldo(self,): 
        return self.__saldo
         
    @property
    def Fazer_Deposito(self):
       pass
    @Fazer_Deposito.setter
    def Fazer_Deposito(self,valor):
        self.__saldo += valor
     
        
        
        
        

    @property 
    def Fazer_saque(self):
        return self.__saldo
    @Fazer_saque.setter
    def Fazer_saque(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return self.__saldo
           
            
        else:
            print('Saldo insuficiente')
            
    


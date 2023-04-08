import sqlite3
import funcao

class Criar_tabela():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (usuario TEXT PRIMARY KEY, senha TEXT, email TEXT, cpf TEXT, saldo REAL)")
    conn.commit()
    conn.close()
    

def Criaçao_usuario(usuario, senha,email,cpf,saldo):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes VALUES (?, ?,? ,?,  ?)", (usuario, senha,email,cpf,saldo))
    conn.commit()
    conn.close()

def validar_login(usuario, senha):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT senha FROM clientes WHERE usuario=?", (usuario,))
    result = cursor.fetchone()
    conn.close()
    if result is not None and result[0] == senha:
        return True
    else:
        return False

class Update():
    def __init__(self,saldo,usuario):
   
    
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET saldo= ? WHERE usuario=?", (saldo,usuario,))
        conn.commit()
        conn.close()


class Usuario():
    def __init__(self,usuario):
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()

        cursor.execute("SELECT usuario FROM clientes WHERE usuario=?",(usuario,) )

        # Obtenha o resultado da consulta
        resultado = cursor.fetchone()

        # Imprima o valor da chave primária
        self.a= print(resultado[0])
        conn.close()
        #return resultado[0]
    
    
   # def salvar(self):
   #     return self.a




class Saldo():
    def __init__(self,usuario):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT saldo FROM clientes WHERE usuario=?",(usuario,))
        resultado = cursor.fetchone()
        self.saldo = float(resultado[0])
        print("Saldo do cliente: ", self.saldo)
        # Fecha a conexão com o banco de dados
        conn.close()
            
    def retorno(self):
        return self.saldo
   
    


class Saque_saldo():
    def __init__(self,usuario,valor):
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute("SELECT saldo FROM clientes WHERE usuario=?", (usuario,))
        resultado = cursor.fetchone()
        self.saldo = float(resultado[0])
        #o saldo daqui ta float
        if self.saldo >= valor:
            self.saldo -= valor
            cursor.execute("UPDATE clientes SET saldo= ? WHERE usuario=?", (self.saldo,usuario,))
            conn.commit()

        
        
            conn.close()
       
  


class Deposito_saldo():
    def __init__(self,usuario,valor):
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute("SELECT saldo FROM clientes WHERE usuario=?", (usuario,))
        resultado = cursor.fetchone()
        self.saldo = float(resultado[0])
        #o saldo daqui ta float
        self.saldo += valor
        cursor.execute("UPDATE clientes SET saldo= ? WHERE usuario=?", (self.saldo,usuario,))
        conn.commit()

        
        
        conn.close()
       

        
            
            
        



        

    
        
        
    
        
    
   

    









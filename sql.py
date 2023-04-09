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

class Atualizar_info():
    def __init__(self,senha, email,cpf,usuario):
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET senha= ?, email=? , cpf = ? WHERE usuario=?", (senha,email,cpf,usuario,))
        conn.commit()
        conn.close()


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
       
class informações():
    def __init__(self,usuario):

        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute("SELECT senha ,email, cpf FROM clientes WHERE usuario=?", (usuario,))
        resultado = cursor.fetchone()
        self.senha = str(resultado[0])
        self.email =str(resultado[1])
        self.cpf = str(resultado[2])
        conn.close()

    def retorno_email(self):
        return self.email

    def retorno_cpf(self):
        return self.cpf
    
    def retorno_senha(self):
        return self.senha

        
            
            
        



        

    
        
        
    
        
    
   

    









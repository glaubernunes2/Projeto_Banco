import sqlite3

class Criar_tabela():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, email TEXT, cpf TEXT)")
    conn.commit()
    conn.close()

def Criaçao_usuario(usuario, senha,email,cpf):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?,? ,?)", (usuario, senha,email,cpf))
    conn.commit()
    conn.close()

def validar_login(usuario, senha):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (usuario,))
    result = cursor.fetchone()
    conn.close()
    if result is not None and result[0] == senha:
        return True
    else:
        return False
    




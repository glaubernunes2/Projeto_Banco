#aqui vai fica a parte da interface do tkinter
from tkinter import * 
from tkinter import ttk
from ttkthemes import ThemedTk

from funcao import Banco
import sql

#from funcao import *


       

class Janelas():

    def __init__(self,) :
        self.janelaInicio= ThemedTk( theme='equilux')
        # Configuraçao da tela
        self.janelaInicio.title('minha janela')
        self.janelaInicio.state('zoomed')
        self.janelaInicio.configure(bg='#2d73b9')
        #==========ESTILOS===========================
        fonte = ('arial,20')
        cor_fundo = '#2d73b9'
        cor_letra =  'white'
        fonte = ('arial',30)
        self.estilo = ttk.Style()
        self.estilo.configure('titulo.TLabel',font=('ariel',50),background='#C64132',foreground=cor_letra,)
        self.estilo.configure('mesagem.TLabel',font=fonte,background=cor_fundo, foreground=cor_letra)
        self.estilo.configure('butao.TButton',borderwidth=50,padding=6, relief='flat',background='red')
        self.estilo.map('butao.TButton',foreground=[('pressed','#ffffff'), ('active','#000000')],background=[('pressed', '!disabled', 'red'), ('active', '#C64132')], )
        #==========ESTILOS===========================
        frame = Frame(self.janelaInicio)

        # Cria as Labels para os campos do formulário
        mesagem_titulo= ttk.Label(self.janelaInicio,text='Banco Infinity', style='titulo.TLabel',relief='solid')
        mesagem_email = ttk.Label(self.janelaInicio, text='Email',style='mesagem.TLabel')
        mesagem_senha = ttk.Label(self.janelaInicio, text='Senha',style='mesagem.TLabel')
        #atribuição de variavel
        self.Usuario = StringVar()
        self.Senha = StringVar()

        # Cria os campos de entrada de texto para o formulário
        self.entrada_email = ttk.Entry(self.janelaInicio,width=30,textvariable=self.Usuario,)
        self.entrada_senha = ttk.Entry(self.janelaInicio,width=30,show='*',textvariable=self.Senha)

        # Posiciona as Labels e os campos de entrada usando o método pack
        mesagem_titulo.pack(side='top', pady=(50,0))
        mesagem_email.pack(side='top',pady=(200,1)) #no pady(y1 , y2) y1== top e y2== boton
        self.entrada_email.pack(side='top',)
        mesagem_senha.pack(side='top',pady=5)
        self.entrada_senha.pack(side='top',)
        
        # Cria um botão para enviar os dados do formulário
        button_enviar = ttk.Button(self.janelaInicio, text='Enviar',style='butao.TButton',width=20,cursor='hand2',command=self.registra)
        button_enviar.pack(side='top',padx=1,pady=(15,1),)
        # Cadastra o novo usuario
        button_cadastro = ttk.Button(self.janelaInicio,text='Criar nova conta',command=self.abrir_nova_janela)
        button_cadastro.pack(side='top',pady=(45,1))
        

        self.janelaInicio.mainloop()
    
    def abrir_nova_janela(self):
        self.janelaInicio.destroy()
        outra_janela = Cadastro ()

    def abrir_loob(self):
        self.janelaInicio.destroy()
        outra_janela = Loob()
    
    
    def registra(self):
        usuario = self.Usuario.get()
        senha = self.Senha.get()
        if sql.validar_login(usuario, senha):
            self.janelaInicio.destroy()
            outra_janela = Loob()
        else:
           #colocar uma mini janela de error
           pass
           
    


    
    
class Cadastro():
    def __init__(self,):
      
        self.janelaCadastro= ThemedTk(theme='equilux')
        # Configuraçao da tela
        self.janelaCadastro.title('cadastro')
        self.janelaCadastro.state('zoomed')
        self.janelaCadastro.configure(bg='#2d73b9')
        frame = Frame(self.janelaCadastro)
        #==========ESTILOS===========================
        cor_fundo = '#2d73b9'
        cor_letra =  'white'
        fonte = ('arial',30)
        self.estilo = ttk.Style()
        self.estilo.configure('titulo.TLabel',font=('ariel',50),background='#C64132',foreground=cor_letra,)
        self.estilo.configure('mesagem.TLabel',font=fonte,background=cor_fundo, foreground=cor_letra)
        self.estilo.configure('butao.TButton',borderwidth=50,padding=6, relief='flat',background='red')
        self.estilo.map('butao.TButton',foreground=[('pressed','#ffffff'), ('active','#000000')],background=[('pressed', '!disabled', 'red'), ('active', '#C64132')], )
        self.estilo.configure("sair.TButton",font = fonte, background= 'red', padding=20)
        #==========ESTILOS===========================

        # Cria as Labels para os campos do formulário
        mesagem_titulo= ttk.Label(self.janelaCadastro,text='Seja Bem-vindo ao Banco Infinity', style='titulo.TLabel')
        mesagem_nome = ttk.Label(self.janelaCadastro, text='Digite o seu nome',style='mesagem.TLabel')
        mesagem_cpf = ttk.Label(self.janelaCadastro,text='digite o seu cpf', style='mesagem.TLabel')
        mesagem_email = ttk.Label(self.janelaCadastro, text='Digte seu Email',style='mesagem.TLabel')
        mesagem_senha = ttk.Label(self.janelaCadastro, text='Digite uma senha',style='mesagem.TLabel')
        mesagem_senha2 = ttk.Label(self.janelaCadastro, text='Digite novamente a senha',style='mesagem.TLabel')
       
        #criar variaveis
        self.cpf_criacao = StringVar()
        self.usuario_criacao = StringVar()
        self.senha_criacao = StringVar()
        self.email_criacao = StringVar()


        # Cria os campos de entrada de texto para o formulário
        entrada_nome = ttk.Entry(self.janelaCadastro,width=30,textvariable=self.usuario_criacao)
        entrada_cpf = ttk.Entry(self.janelaCadastro,width=30,textvariable=self.cpf_criacao)
        entrada_email = ttk.Entry(self.janelaCadastro,width=30,textvariable=self.email_criacao)
        entrada_senha = ttk.Entry(self.janelaCadastro,width=30,textvariable=self.senha_criacao)
        entrada_senha2 = ttk.Entry(self.janelaCadastro,width=30,)

        # Posiciona as Labels e os campos de entrada usando o método pack
        mesagem_titulo.pack(side='top', pady=(50,0))
        mesagem_nome.pack(side='top',pady=(150,1))
        entrada_nome.pack(side='top',pady=5)
        mesagem_cpf.pack(side='top',pady=5)
        entrada_cpf.pack(side='top')
        mesagem_email.pack(side='top',pady=5) #no pady(y1 , y2) y1== top e y2== boton
        entrada_email.pack(side='top',)
        mesagem_senha.pack(side='top',pady=5)
        entrada_senha.pack(side='top',)
        mesagem_senha2.pack(side='top',pady=5)
        entrada_senha2.pack(side='top',pady=5)
       
        # Cria um botão para salvar os dados do formulário
        button_enviar = ttk.Button(self.janelaCadastro, text='Enviar',command=self.registra)
        button_enviar.pack(side='top',padx=1,pady=(15,1),)
        button_sair = ttk.Button(self.janelaCadastro,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)
        button_sair.pack(side='bottom',padx=(1000,1))
        #Atalhos de teclas
        self.janelaCadastro.bind('<Escape>', self.volta_janela)

        self.janelaCadastro.mainloop()

    def abrir_nova_janela(self):
       self.janelaCadastro.destroy()
       outra_janela = Janelas()
    def volta_janela(self,evento):
       self.janelaCadastro.destroy()
       outra_janela = Janelas()
    
    

    def registra(self):
        usuario = self.usuario_criacao.get()
        senha = self.senha_criacao.get()
        email = self.email_criacao.get()
        cpf = self.cpf_criacao.get()
        sql.Criaçao_usuario(usuario, senha,email,cpf)
        self.janelaCadastro.destroy()
        outra_janela = Janelas()
        

    

    

class Loob():
    def __init__(self):
        self.janelaloob= ThemedTk( theme='equilux')
        # Configuraçao da tela
        self.janelaloob.title('loob')
        self.janelaloob.state('zoomed')
        self.janelaloob.configure(bg='#2d73b9')
        #frame = Frame(self.janelaloob)
        #==========ESTILOS===========================
        cor_fundo = '#2d73b9'
        cor_letra =  'white'
        fonte = ('arial',20)
        self.estilo = ttk.Style()
        self.estilo.configure('titulo.TLabel',font=('ariel',50),background='#C64132',foreground=cor_letra,)
        self.estilo.configure('mesagem.TLabel',font=fonte,background=cor_fundo, foreground=cor_letra)
        self.estilo.configure('butao.TButton',borderwidth=50,padding=6, relief='flat',background='red',)
        self.estilo.map('butao.TButton',foreground=[('pressed','#ffffff'), ('active','#000000')],background=[('pressed', '!disabled', 'red'), ('active', '#C64132')],)
        self.estilo.configure("sair.TButton",font = fonte, background= 'red',padding=20)
        #==========ESTILOS===========================

        # Cria as Labels para os campos do formulário
        mesagem_titulo= ttk.Label(self.janelaloob,text='Seja Bem-vindo', style='titulo.TLabel',)

        # Cria os campos de entrada de texto para o formulário

        # Posiciona as Labels e os campos de entrada usando o método pack
        
        mesagem_titulo.pack(side='top', pady=(150,0))
        
        # Cria um botão para saque
        
        button_saque = ttk.Button(self.janelaloob, text='Saque',style='botao.TButton', command=self.abrir_saque)

        # Cria um botão para deposito
       
        button_deposito = ttk.Button(self.janelaloob, text='Deposito',style='botao.TButton', command=self.abrir_deposito)
        
        # Cria um botão para extrato
        
        button_extrato = ttk.Button(self.janelaloob, text='Extrato',style='botao.TButton')

        # Cria um botão para colsutar saldo
       
        button_saldo = ttk.Button(self.janelaloob, text='Saldo',style='botao.TButton', command=self.abrir_saldo)
        # Criar um botão de sair
        button_sair = ttk.Button(self.janelaloob,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)

        # Posicinamentos dos botões
       
        button_saldo.pack(side='top',padx=1,pady=(150,1),)
        button_deposito.pack(side='top',padx=1,pady=(30,1),)
        button_saque.pack(side='top',padx=1,pady=(30,1),)
        button_extrato.pack(side='top',padx=1,pady=(30,1),)
        button_sair.pack(side='bottom',padx=(1250,1)) 

        #Atalhos de teclas
        self.janelaloob.bind('<Escape>', self.volta_janela)

        
        
        self.janelaloob.mainloop()  

    def volta_janela(self,evento):
       self.janelaloob.destroy()
       outra_janela = Janelas()    
        
        
    def abrir_nova_janela(self):
       self.janelaloob.destroy()
       outra_janela = Janelas()
    
    def abrir_saque(self):
       self.janelaloob.destroy()
       outra_janela = Saque()
    
    def abrir_deposito(self):
       self.janelaloob.destroy()
       outra_janela = Deposito()
    
    #so tirar dos comentarios quadno fazer a janela saldo
    def abrir_saldo(self):
       self.janelaloob.destroy()
       outra_janela = Extrato()
 



class Saque():
    def __init__(self):
        self.janela_saque= ThemedTk( theme='equilux')
        self.janela_saque.state('zoomed')
        self.janela_saque.title('Saque')
        self.janela_saque.configure(bg='#2d73b9')
        #==========ESTILOS===========================
        cor_fundo = '#2d73b9'
        cor_letra =  'white'
        fonte = ('arial',30)
        self.estilo = ttk.Style()
        self.estilo.configure('titulo.TLabel',font=('ariel',50),background='#C64132',foreground=cor_letra,)
        self.estilo.configure('mesagem.TLabel',font=fonte,background=cor_fundo, foreground=cor_letra)
        self.estilo.configure('butao.TButton',borderwidth=50,padding=6, relief='flat',background='red')
        self.estilo.map('butao.TButton',foreground=[('pressed','#ffffff'), ('active','#000000')],background=[('pressed', '!disabled', 'red'), ('active', '#C64132')], )
        self.estilo.configure("sair.TButton",font = fonte, background= 'red', padding=20)
        #==========ESTILOS===========================
        # Cria as Labels para os campos do formulário
        mensagem_titulo= ttk.Label(self.janela_saque,text='Saque',style='titulo.TLabel')
        mensagem_saque = ttk.Label(self.janela_saque,text='qual o valor que voçe vai sacar: R$',style='mesagem.TLabel')
        self.mensagem_sucesso=ttk.Label(text='', style='mensagem.TLabel')
        #criar variaveis
        self.saque = DoubleVar()
       
        #criar campos de entrada de textos
        entrada_saque = ttk.Entry(self.janela_saque,width=10, textvariable=self.saque)


        #posicionamentos das mensagens
        mensagem_titulo.pack(side='top', pady=(50,0))
        mensagem_saque.pack(side='top',pady=(150,1))
        entrada_saque.pack(side='top',pady=5)
        self.mensagem_sucesso.pack(side='top',pady=(150,1))
        # Cria um botão para executa os eventos
        botao_saque= ttk.Button(self.janela_saque,text='Sacar',command=self.Saque)
        botao_saque.pack(side='top',padx=1,pady=(15,1))
        button_sair = ttk.Button(self.janela_saque,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)
        button_sair.pack(side='bottom',padx=(1000,1))

        #Atalhos de teclas
        self.janela_saque.bind('<Escape>', self.volta_janela)


        self.janela_saque.mainloop()

    def Saque(self):
        banco = Banco
        valor = self.saque.get()
        banco.Fazer_saque = valor
        self.mensagem_sucesso.configure(text=(f'Saque de R${valor} feito'))
        
    def abrir_nova_janela(self):
        self.janela_saque.destroy()
        outra_janela = Loob()
    def volta_janela(self,evento):
       self.janela_saque.destroy()
       outra_janela = Loob()

class Deposito():
    def __init__(self):
        self.janela_deposito= ThemedTk( theme='equilux')
        self.janela_deposito.state('zoomed')
        self.janela_deposito.title('Deposito')
        self.janela_deposito.configure(bg='#2d73b9')

        #==========ESTILOS===========================
        cor_fundo = '#2d73b9'
        cor_letra =  'white'
        fonte = ('arial',30)
        self.estilo = ttk.Style()
        self.estilo.configure('titulo.TLabel',font=('ariel',50),background='#C64132',foreground=cor_letra,)
        self.estilo.configure('mesagem.TLabel',font=fonte,background=cor_fundo, foreground=cor_letra)
        self.estilo.configure('butao.TButton',borderwidth=50,padding=6, relief='flat',background='red')
        self.estilo.map('butao.TButton',foreground=[('pressed','#ffffff'), ('active','#000000')],background=[('pressed', '!disabled', 'red'), ('active', '#C64132')], )
        self.estilo.configure("sair.TButton",font = fonte, background= 'red', padding=20)
        #==========ESTILOS===========================
        # Cria as Labels para os campos do formulário
        mensagem_titulo= ttk.Label(self.janela_deposito,text='deposito',style='titulo.TLabel')
        mensagem_deposito = ttk.Label(self.janela_deposito,text='qual o valor que voçe vai depositar: R$',style='mesagem.TLabel')

        #criar variaveis
        self.deposito = DoubleVar()
        #criar campos de entrada de textos
        entrada_deposito = ttk.Entry(self.janela_deposito,text='qual o valor que voçe vai depositar: R$',textvariable=self.deposito)
        self.mensagem_sucesso=ttk.Label(text='', style='titulo.TLabel')
        #posicionamentos das mensagens
        mensagem_titulo.pack(side='top', pady=(50,0))
        mensagem_deposito.pack(side='top',pady=(150,1))
        entrada_deposito.pack(side='top',pady=5)
        self.mensagem_sucesso.pack(side='top',pady=(150,1))


        # Cria um botão para executa os eventos
        botao_deposito= ttk.Button(self.janela_deposito,text='Depositar',command=self.Depositar)
        botao_deposito.pack(side='top',padx=1,pady=(15,1))
        button_sair = ttk.Button(self.janela_deposito,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)
        button_sair.pack(side='bottom',padx=(1000,1))
        #Atalhos de teclas
        self.janela_deposito.bind('<Escape>', self.volta_janela)


        self.janela_deposito.mainloop()

    def Depositar(self):
        banco = Banco
        valor = self.deposito.get()
        banco.Fazer_Deposito = valor
        self.mensagem_sucesso.configure(text=(f'deposito de R${valor} feito'))
        print(f'seu saldo e{Banco.VerSaldo}')          
        
    def abrir_nova_janela(self):
       self.janela_deposito.destroy()
       outra_janela = Loob()
    def volta_janela(self,evento):
       self.janela_deposito.destroy()
       outra_janela = Loob()

#falta saber como voçe pegar pra ver a movimentação

class Extrato():
    def __init__(self):
        self.janela_extrato= ThemedTk( theme='equilux')
        self.janela_extrato.geometry('500x300')
        self.janela_extrato.state('zoomed')
        self.janela_extrato.title('saldo')
        self.janela_extrato.configure(bg='#2d73b9')
        #==========ESTILOS===========================
        cor_fundo = '#2d73b9'
        cor_letra =  'white'
        fonte = ('arial',30)
        self.estilo = ttk.Style()
        self.estilo.configure('titulo.TLabel',font=('ariel',50),background='#C64132',foreground=cor_letra,)
        self.estilo.configure('mesagem.TLabel',font=fonte,background=cor_fundo, foreground=cor_letra)
        self.estilo.configure('butao.TButton',borderwidth=50,padding=6, relief='flat',background='red')
        self.estilo.map('butao.TButton',foreground=[('pressed','#ffffff'), ('active','#000000')],background=[('pressed', '!disabled', 'red'), ('active', '#C64132')], )
        self.estilo.configure("sair.TButton",font = fonte, background= 'red', padding=20)
        #==========ESTILOS===========================
        # Cria as Labels para os campos do formulário
        mensagem_titulo= ttk.Label(self.janela_extrato,text='Aperte ENTER pra ver po saldo',style='titulo.TLabel')
        
        #criar variaveis
        

        #criar campos de entrada de textos

        #posicionamentos das mensagens
        
        mensagem_titulo.pack()

        # Cria um botão para executa os eventos
        
        
        button_sair = ttk.Button(self.janela_extrato,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)
        button_sair.pack(side='bottom',padx=(1000,1))
        #Atalhos de teclas
        self.janela_extrato.bind('<Escape>', self.volta_janela)
        self.janela_extrato.bind('<Return>', self.Saldo)


        self.janela_extrato.mainloop()

    
    def Saldo(self,evento):
        banco =Banco
        saldo =banco.VerSaldo
        mensagem_evento = ttk.Label(self.janela_extrato,text=(f'seu saldo é {saldo}'), style='titulo.TLabel',width=50)
        print(saldo)
        mensagem_evento.pack(side='top',pady=(150,1))
        
    
    
    def abrir_nova_janela(self):
       self.janela_extrato.destroy()
       outra_janela = Loob()
    def volta_janela(self,evento):
       self.janela_extrato.destroy()
       outra_janela = Loob()




    
   
   



if __name__ == '__main__':
    janela = Janelas()
    
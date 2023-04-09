#aqui vai fica a parte da interface do tkinter
from tkinter import * 
from tkinter import ttk
from ttkthemes import ThemedTk

from funcao import Banco
import sql


#from funcao import *
class Janelas():

    def __init__(self,) :
        super().__init__()
        # vairaveis universais nessa class

        #ttk
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
        
        # Criar um botão de sair
        button_sair = ttk.Button(self.janelaInicio,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.sair)
       
        # Cadastra o novo usuario
        button_cadastro = ttk.Button(self.janelaInicio,text='Criar nova conta',command=self.abrir_nova_janela)
        button_cadastro.pack(side='top',pady=(45,1))
        button_sair.pack(side='bottom',padx=(1250,1))
        
        #Atalhos de teclas
        self.janelaInicio.bind('<Escape>', self.sair_evento)


        self.janelaInicio.mainloop()
    
    def abrir_nova_janela(self):
        self.janelaInicio.destroy()
        outra_janela = Cadastro ()
    
    def sair(self,):
        self.janelaInicio.destroy()
    
    def sair_evento(self,evento):
        self.janelaInicio.destroy()
    
    def abrir_loob(self):
        self.janelaInicio.destroy()
        outra_janela = Loob(self.usuario_master)
    
    
    def registra(self):
        self.usuario_master = self.Usuario.get()
        senha = self.Senha.get()
        
        
        
        if sql.validar_login(self.usuario_master, senha):           
            self.janelaInicio.destroy()
            outra_janela = Loob(self.usuario_master, )
            
        else:
           #colocar uma mini janela de error
           pass
    
    
class Cadastro():
    def __init__(self,):
        # vairaveis universais nessa class
        
        #ttk
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
        __saldo = 0
        usuario = self.usuario_criacao.get()
        senha = self.senha_criacao.get()
        email = self.email_criacao.get()
        cpf = self.cpf_criacao.get()
        sql.Criaçao_usuario(usuario, senha,email,cpf,__saldo)
        self.janelaCadastro.destroy()
        outra_janela = Janelas()
        

    



    

class Loob():
    def __init__(self,usuario_master,):
        super().__init__()
        # vairaveis universais nessa class
        self.usuario_master = usuario_master
        #ttk
        self.janelaloob= ThemedTk( theme='equilux')
        # Configuraçao da tela
        self.janelaloob.title(f'bem vindo loob')
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
        mesagem_titulo= ttk.Label(self.janelaloob,text=f'Seja Bem-vindo {self.usuario_master} ', style='titulo.TLabel',)

        # Cria os campos de entrada de texto para o formulário

        # Posiciona as Labels e os campos de entrada usando o método pack
        
        mesagem_titulo.pack(side='top', pady=(150,0))
        
        # Cria um botão para saque
        
        button_saque = ttk.Button(self.janelaloob, text='Saque',style='botao.TButton', command=self.abrir_saque)

        # Cria um botão para deposito
       
        button_deposito = ttk.Button(self.janelaloob, text='Deposito',style='botao.TButton', command=self.abrir_deposito)

        # Cria um botão para colsutar saldo
       
        button_saldo = ttk.Button(self.janelaloob, text='Saldo',style='botao.TButton', command=self.abrir_saldo)
        
        #criar um botão pra modificar as informações
        button_atualizacao = ttk.Button(self.janelaloob, text='Atualizaçõ de perfil',style='botao.TButton', command=self.abrir_atualização)
       
        # Criar um botão de sair
        button_sair = ttk.Button(self.janelaloob,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)

        # Posicinamentos dos botões
       
        button_saldo.pack(side='top',padx=1,pady=(150,1),)
        button_deposito.pack(side='top',padx=1,pady=(30,1),)
        button_saque.pack(side='top',padx=1,pady=(30,1),)
        button_atualizacao.pack(side='top',padx=1,pady=(30,1),)
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
       outra_janela = Saque(self.usuario_master)
    def abrir_atualização(self):
       self.janelaloob.destroy()
       outra_janela = Atualizar_informacao(self.usuario_master)
    
    def abrir_deposito(self):
       self.janelaloob.destroy()
       outra_janela = Deposito(self.usuario_master,)
    
    #so tirar dos comentarios quadno fazer a janela saldo
    def abrir_saldo(self):
       self.janelaloob.destroy()
       outra_janela = Extrato(self.usuario_master,)
       
 



class Saque():
    def __init__(self,usuario_master):
        super().__init__()
        # vairaveis universais nessa class
        self.usuario_master = usuario_master
        #ttk
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
        
        valor = self.saque.get()
        sql.Saque_saldo(self.usuario_master,valor)
        retorno= sql.Saldo(self.usuario_master)
        self.saldo = retorno.retorno()
        self.mensagem_sucesso.configure(text=(f'Saque de R${valor} feito'))
        
    def abrir_nova_janela(self,):
        self.janela_saque.destroy()
        outra_janela = Loob(self.usuario_master)
    def volta_janela(self,evento):
       self.janela_saque.destroy()
       outra_janela = Loob(self.usuario_master)

class Deposito():
    def __init__(self,usuario_master,):
        super().__init__()
        # vairaveis universais nessa class
        self.usuario_master = usuario_master
        #ttk
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
        self.mensagem_saldo=ttk.Label(text='', style='titulo.TLabel')
        #posicionamentos das mensagens
        mensagem_titulo.pack(side='top', pady=(50,0))
        mensagem_deposito.pack(side='top',pady=(150,1))
        entrada_deposito.pack(side='top',pady=5)
        self.mensagem_sucesso.pack(side='top',pady=(150,1))
        self.mensagem_saldo.pack(side='top',pady=(150,1))


        # Cria um botão para executa os eventos
        botao_deposito= ttk.Button(self.janela_deposito,text='Depositar',command=self.Depositar)
        botao_deposito.pack(side='top',padx=1,pady=(15,1))
        button_sair = ttk.Button(self.janela_deposito,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)
        button_sair.pack(side='bottom',padx=(1000,1))
        #Atalhos de teclas
        self.janela_deposito.bind('<Escape>', self.volta_janela)


        self.janela_deposito.mainloop()

    def Depositar(self):
        valor = self.deposito.get()

        sql.Deposito_saldo(self.usuario_master,valor)
        retorno= sql.Saldo(self.usuario_master)
        self.saldo = retorno.retorno()
        self.mensagem_sucesso.configure(text=(f'deposito de R${valor} feito'))
        self.mensagem_saldo.configure(text=(f'Seu saldo é de R$ {self.saldo}.'))
                 
        
    def abrir_nova_janela(self):
       self.janela_deposito.destroy()
       outra_janela = Loob(self.usuario_master)
       
    def volta_janela(self,evento):
       self.janela_deposito.destroy()
       outra_janela = Loob(self.usuario_master)

#falta saber como voçe pegar pra ver a movimentação

class Extrato():
    def __init__(self,usuario_master,):
        super().__init__()
        # vairaveis universais nessa class
        self.usuario_master = usuario_master
    
        #ttk
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
        mensagem_titulo= ttk.Label(self.janela_extrato,text=f'{self.usuario_master} aperte ENTER pra ver po saldo',style='titulo.TLabel')
        
        #criar variaveis
        

        #criar campos de entrada de textos

        #posicionamentos das mensagens
        
        mensagem_titulo.pack()

        # Cria um botão para executa os eventos
        
        
        button_sair = ttk.Button(self.janela_extrato,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)
        button_sair.pack(side='bottom',padx=(1000,1))
        #Atalhos de teclas
        self.janela_extrato.bind('<Escape>', self.volta_janela)
        self.janela_extrato.bind('<Return>', self.ver_saldo)


        self.janela_extrato.mainloop()

    
    def ver_saldo(self,evento):
        retorno= sql.Saldo(self.usuario_master)
        self.saldo = retorno.retorno()
        mensagem_evento = ttk.Label(self.janela_extrato,text=(f'seu saldo é {self.saldo}'), style='titulo.TLabel',width=50)

        mensagem_evento.pack(side='top',pady=(150,1))
        
    
    
    def abrir_nova_janela(self):
       self.janela_extrato.destroy()
       outra_janela = Loob(self.usuario_master,)
    def volta_janela(self,evento):
       self.janela_extrato.destroy()
       outra_janela = Loob(self.usuario_master,)

class Atualizar_informacao():
    def __init__(self,usuario_master,):
        super().__init__()
        # vairaveis universais nessa class
        self.usuario_master = usuario_master
        retorno =sql.informações(self.usuario_master)
        self.cpf_master = retorno.retorno_cpf()
        self.email_master = retorno.retorno_email()
        self.senha_master = retorno.retorno_senha()
        #ttk
        self.janela_atualizacao= ThemedTk( theme='equilux')
        self.janela_atualizacao.geometry('500x300')
        self.janela_atualizacao.state('zoomed')
        self.janela_atualizacao.title('Atualização')
        self.janela_atualizacao.configure(bg='#2d73b9')
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
        mensagem_titulo= ttk.Label(self.janela_atualizacao,text=f'hey {self.usuario_master} digite as informações que voçê quer modificar. ',style='titulo.TLabel')
        mesagem_cpf = ttk.Label(self.janela_atualizacao,text='Digite o seu novo cpf', style='mesagem.TLabel')
        mesagem_email = ttk.Label(self.janela_atualizacao, text='Digte seu novo email Email',style='mesagem.TLabel')
        mesagem_senha = ttk.Label(self.janela_atualizacao, text='Digite uma senha',style='mesagem.TLabel')
        mostrar_cpf = ttk.Label(self.janela_atualizacao,text=f'o seu cpf é {self.cpf_master}', style='mesagem.TLabel')
        mostrar_email = ttk.Label(self.janela_atualizacao,text=f'o seu email é {self.email_master}', style='mesagem.TLabel')
        self.mostrar_senha = ttk.Label(self.janela_atualizacao,text=f'A aperter ENTER caso queirar ver sua senha', style='mesagem.TLabel')
        #criar variaveis
       
        
        self.cpf_modificado = StringVar()
        self.email_modificado = StringVar()
        self.senha_modificado = StringVar()

        #criar campos de entrada de textos
        #entrada_nome = ttk.Entry(self.janela_atualizacao,width=30,textvariable=self.usuario_criacao)
        entrada_cpf = ttk.Entry(self.janela_atualizacao,width=30,textvariable=self.cpf_modificado)
        entrada_email = ttk.Entry(self.janela_atualizacao,width=30,textvariable=self.email_modificado)
        entrada_senha = ttk.Entry(self.janela_atualizacao,width=30,textvariable=self.senha_modificado)
        #posicionamentos das mensagens
        
        mensagem_titulo.pack(side='top', pady=(50,0))
        mostrar_cpf.pack(side='top',pady=(150,1))
        mostrar_email.pack(side='top',pady=(5,1))
        self.mostrar_senha.pack(side='top',pady=(5,1))
        '''entrada_nome.pack(side='top',pady=5)'''
        mesagem_cpf.pack(side='top',pady=(150,1))
        entrada_cpf.pack(side='top')
        mesagem_email.pack(side='top',pady=5) 
        entrada_email.pack(side='top',)
        mesagem_senha.pack(side='top',pady=5)
        entrada_senha.pack(side='top',)

        # Cria um botão para executa os eventos
        button_atualizar = ttk.Button(self.janela_atualizacao,text='Atualizar',style='sair.TButton',width=30,cursor='hand2', command=self.atualizar)
        button_atualizar.pack(side='top',pady=(100,1))
        button_sair = ttk.Button(self.janela_atualizacao,text='Sair',style='sair.TButton',width=30,cursor='hand2', command=self.abrir_nova_janela)
        button_sair.pack(side='bottom',padx=(1,1))
       
        #Atalhos de teclas
        self.janela_atualizacao.bind('<Escape>', self.volta_janela)
        self.janela_atualizacao.bind('<Return>', self.senha)


        self.janela_atualizacao.mainloop()
    
    def senha(self,evento):
        self.mostrar_senha.config(text=f'A sua senha é {self.senha_master}')
        
    def atualizar(self):
        senha = self.senha_modificado.get()
        email = self.email_modificado.get()
        cpf = self.cpf_modificado.get()
        print(senha,cpf,email)
        sql.Atualizar_info(senha,email,cpf,self.usuario_master)
        print('atualizado')
        self.janela_atualizacao.destroy()
        outra_janela = Loob(self.usuario_master, )
        
    def abrir_nova_janela(self):
       self.janela_atualizacao.destroy()
       outra_janela = Loob(self.usuario_master,)
    def volta_janela(self,evento):
       self.janela_atualizacao.destroy()
       outra_janela = Loob(self.usuario_master,)
   



if __name__ == '__main__':
    janela = Janelas()
    
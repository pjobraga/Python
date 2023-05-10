from tkinter import *

#Tk / Janela
janela = Tk()

#Altera o titulo
janela.title("Calculadora")

def enviarNumeroPara(char):

    global calculoOperacoes

    #calculoOperacoes = calculoOperacoes + str(char)
    calculoOperacoes += str(char) #Com o char que só permite 1 item. vou adicionando no final de cada operação
    textoDeEntrada.set(calculoOperacoes) #Estamos colocando todo o texto na variavel que está lincado com o campo Entry

def deletarNumero():

    global calculoOperacoes

    textoSemOUltimoDigito = calculoOperacoes[:-1] #Pego todo o texto que está no Entry e excluo apenas o último digito

    #Coloando na variavel o texto da operação sem o último digito
    calculoOperacoes = textoSemOUltimoDigito

    textoDeEntrada.set(calculoOperacoes)  # Estamos colocando todo o texto na variavel que está lincado com o campo Entry

def limparTudo():

    global calculoOperacoes

    calculoOperacoes = "" #Limpando todo o texto da variavel
    textoDeEntrada.set(calculoOperacoes)  # Estamos colocando todo o texto na variavel que está lincado com o campo Entry

def funcaoIgual():

    global calculoOperacoes

    #eval - Avalia se é um calculo valido e efetua o calculo
    resultadoCalculo = str(eval(calculoOperacoes))
    textoDeEntrada.set(resultadoCalculo)  # Estamos colocando todo o texto na variavel que está lincado com o campo Entry

    #Mudo a variavel que tinha a operação e coloco apenas o resultdo do calculo na variavel
    calculoOperacoes = resultadoCalculo

calculoOperacoes = ""
textoDeEntrada = StringVar()

#Caixa de texto que exibe o resulta e as operações
textoExibeOperecoesResultado = Entry(janela, font=("Arial 20 bold"),
                                     textvariable=textoDeEntrada, #Variavel
                                     border=5, #Borda
                                     background="#BBB", #Cor do fundo
                                     foreground="black", #Cor da Letra
                                     ).grid(row=1, columnspan=5, padx= 10, pady= 15)

#lambda - Permite enviar vários dados em uma função
#sticky - Ele estica / preenhe as laterais
#sticky - NSEW - Norte, Sul, Leste e Oeste
#grid - Divide a tela em partes / grades
botaoNumero7 = Button(janela,
                      text="7", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("7")).grid(row=2, column=0, sticky="NSEW")

#lambda - Permite enviar vários dados em uma função
#sticky - Ele estica / preenhe as laterais
#sticky - NSEW - Norte, Sul, Leste e Oeste
#grid - Divide a tela em partes / grades
botaoNumero8 = Button(janela,
                      text="8", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("8")).grid(row=2, column=1, sticky="NSEW")

#lambda - Permite enviar vários dados em uma função
#sticky - Ele estica / preenhe as laterais
#sticky - NSEW - Norte, Sul, Leste e Oeste
#grid - Divide a tela em partes / grades
botaoNumero9 = Button(janela,
                      text="9", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("9")).grid(row=2, column=2, sticky="NSEW")

#lambda - Permite enviar vários dados em uma função
#sticky - Ele estica / preenhe as laterais
#sticky - NSEW - Norte, Sul, Leste e Oeste
#grid - Divide a tela em partes / grades
botaoDeletar = Button(janela,
                      text="DEL", #Texto do botão
                      border= 5, #Borda
                      foreground= "#000", #Cor da letra
                      background= "#DB701F", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = deletarNumero).grid(row=2, column=3, sticky="NSEW")

#lambda - Permite enviar vários dados em uma função
#sticky - Ele estica / preenhe as laterais
#sticky - NSEW - Norte, Sul, Leste e Oeste
#grid - Divide a tela em partes / grades
botaoDeletarTudo = Button(janela,
                      text="AC", #Texto do botão
                      border= 5, #Borda
                      foreground= "#000", #Cor da letra
                      background= "#DB701F", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = limparTudo).grid(row=2, column=4, sticky="NSEW")

#lambda - Permite enviar vários dados em uma função
#sticky - Ele estica / preenhe as laterais
#sticky - NSEW - Norte, Sul, Leste e Oeste
#grid - Divide a tela em partes / grades
botaoNumero4 = Button(janela,
                      text="4", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("4")).grid(row=3, column=0, sticky="NSEW")


botaoNumero5 = Button(janela,
                      text="5", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("5")).grid(row=3, column=1, sticky="NSEW")


botaoNumero6 = Button(janela,
                      text="6", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("6")).grid(row=3, column=2, sticky="NSEW")


botaoMultiplicacao = Button(janela,
                      text="*", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("*")).grid(row=3, column=3, sticky="NSEW")

botaoDivisao = Button(janela,
                      text="/", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("/")).grid(row=3, column=4, sticky="NSEW")

botaoNumero1 = Button(janela,
                      text="1", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("1")).grid(row=4, column=0, sticky="NSEW")

botaoNumero2 = Button(janela,
                      text="2", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("2")).grid(row=4, column=1, sticky="NSEW")

botaoNumero3 = Button(janela,
                      text="3", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("3")).grid(row=4, column=2, sticky="NSEW")

botaoAdicao = Button(janela,
                      text="+", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("+")).grid(row=4, column=3, sticky="NSEW")

botaoSubtracao = Button(janela,
                      text="-", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("-")).grid(row=4, column=4, sticky="NSEW")

botaoNumero0 = Button(janela,
                      text="0", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara("0")).grid(row=5, column=0, sticky="NSEW")

botaoPonto = Button(janela,
                      text=".", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = lambda:enviarNumeroPara(".")).grid(row=5, column=1, sticky="NSEW")

#lambda - Permite enviar vários dados em uma função
#sticky - Ele estica / preenhe as laterais
#sticky - NSEW - Norte, Sul, Leste e Oeste
#grid - Divide a tela em partes / grades
#columnspan - Colocamos para dizer quantas colunas do grid o item vai oculpar
botaoIgual = Button(janela,
                      text="=", #Texto do botão
                      border= 5, #Borda
                      foreground= "black", #Cor da letra
                      background= "#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo
                      command = funcaoIgual).grid(row=5, column=2, columnspan=3, sticky="NSEW")



#mainloop - No Tkinter uma janela funciona como um loop infinito
#A janela que o Python mostra na verdade é um programa em funcionamento
janela.mainloop()
import tkinter as tk
import customtkinter

global xbotonFuncionObjetivo
global Y_botonAgregarRestriccion
global numeroVariable
global cantidadRestricciones
xbotonFuncionObjetivo = 195
numeroVariable = 2
Y_botonAgregarRestriccion = 35
cantidadRestricciones = 0

def agregar_entrada_variable_funcionObjetivo(x,y,listaEntrada):
    nueva_barra_entrada = customtkinter.CTkEntry(master=funcionObjetivo,width=26,height=26)
    nueva_barra_entrada.place(x= x,y= y)
    listaEntrada.append(nueva_barra_entrada)

def agregar_texto_variable_funcionObjetivo(x,y,numero,listaVariable):
    nueva_variable = customtkinter.CTkLabel(master=funcionObjetivo,text='X'+str(numero),font=('Bold',16))
    nueva_variable.place(x=x+25,y=y)
    listaVariable.append(nueva_variable)
    global numeroVariable
    numeroVariable = numero + 1

def agregar_suma_funcionObjetivo(x,y,listaSuma):
    suma = customtkinter.CTkLabel(master=funcionObjetivo,text='+',font=('Bold',16),text_color='#D02323')
    suma.place(x=x+50,y=y)
    listaSuma.append(suma)

def agregar_variable_funcionObjetivo(x,y,numero,listaEntrada,listaVariable,listaSuma):
    if (numero < 6):
        global xbotonFuncionObjetivo
        xbotonFuncionObjetivo = x + 65
        agregar_entrada_variable_funcionObjetivo(x,y,listaEntrada)
        agregar_texto_variable_funcionObjetivo(x,y,numero,listaVariable)
        agregar_suma_funcionObjetivo(x-65,y,listaSuma)
        botonAgregarVariable.place(x=xbotonFuncionObjetivo,y=5)
    else:
        ventanaAlerta = customtkinter.CTkToplevel()
        ventanaAlerta.title('No puedes agregar mas variables :(')

def agregar_entrada_variable_restriccion(x,y,listaEntrada):
    nueva_barra_entrada = customtkinter.CTkEntry(master=restricciones,width=26,height=26)
    nueva_barra_entrada.place(x= x,y= y)
    listaEntrada.append(nueva_barra_entrada)

def agregar_texto_variable_restriccion(x,y,numero,listaVariable):
    nueva_variable = customtkinter.CTkLabel(master=restricciones,text='X'+str(numero),font=('Bold',16))
    nueva_variable.place(x=x+25,y=y)
    listaVariable.append(nueva_variable)

def agregar_suma_restriccion(x,y,listaSuma):
    suma = customtkinter.CTkLabel(master=restricciones,text='+',font=('Bold',16),text_color='#D02323')
    suma.place(x=x+50,y=y)
    listaSuma.append(suma)

def agregar_menorIgual_restriccion(x,y,listaMenorIgual):
    menorIgual = customtkinter.CTkLabel(master=restricciones,text='<=',font=('Bold',16),text_color='#D02323')
    menorIgual.place(x=x,y=y)
    listaMenorIgual.append(menorIgual)

def agregar_entrada_valor_restriccion(x,y,listaValor):
    nueva_entrada = customtkinter.CTkEntry(master=restricciones,width=26,height=26)
    nueva_entrada.place(x=x+40,y=y)
    listaValor.append(nueva_entrada)

def agregar_restriccion(y,listaRestricciones):
    botonAgregarVariable.configure(state="disabled")
    x = 15

    listaRestriccion = []
    entradasRestriccion = []
    variablesRestriccion = []
    sumasRestriccion = []
    menorIgualRestriccion = []
    valorRestriccion = []
    global numeroVariable
    global Y_botonAgregarRestriccion
    global cantidadRestricciones

    cantidadRestricciones = cantidadRestricciones + 1

    Y_botonAgregarRestriccion = Y_botonAgregarRestriccion + 35
    botonAgregarRestriccion.place(x=15,y=Y_botonAgregarRestriccion)

    for num in range(numeroVariable-1):
        agregar_entrada_variable_restriccion(x,y,entradasRestriccion)
        agregar_texto_variable_restriccion(x,y,num+1,variablesRestriccion)
        if ((num+1) < (numeroVariable-1)):
            agregar_suma_restriccion(x,y,sumasRestriccion)
        x = x + 65
    
    agregar_menorIgual_restriccion(x,y,menorIgualRestriccion)
    agregar_entrada_valor_restriccion(x,y,valorRestriccion)

    listaRestriccion.append(entradasRestriccion)
    listaRestriccion.append(variablesRestriccion)
    listaRestriccion.append(sumasRestriccion)
    listaRestriccion.append(menorIgualRestriccion)
    listaRestriccion.append(valorRestriccion)
    listaRestricciones.append(listaRestriccion)

def estandarizar(entradasFuncionObjetivo,listaRestricciones):
    x = 10
    y = 35
    tituloFuncionObejito = customtkinter.CTkLabel(master=estandarizacion,text='Z',font=('Bold',20))
    tituloFuncionObejito.place(x=x,y=y)
    global numeroVariable
    funcionObjetivoTexto = '- Z'
    for variables in range(numeroVariable-1):
        funcionObjetivoTexto = funcionObjetivoTexto + ' - ' + entradasFuncionObjetivo[variables].get() + 'X' + str(variables+1)

    funcionObjetivoTexto = funcionObjetivoTexto + ' = 0'
    funcionObjetivo = customtkinter.CTkLabel(master=estandarizacion,text=funcionObjetivoTexto,font=('Bold',16))
    funcionObjetivo.place(x=x,y=y)

    for restriccion in range(cantidadRestricciones):
        textoRestriccion = ''
        y = y + 35
        for variables in range(numeroVariable-1):
            textoRestriccion = textoRestriccion + ' + ' + listaRestricciones[restriccion][0][variables].get() + 'X' + str(variables+1)

        textoRestriccion = textoRestriccion + ' + S' + str(restriccion+1) + ' = ' + listaRestricciones[restriccion][4][0].get()
        restriccion = customtkinter.CTkLabel(master=estandarizacion,text=textoRestriccion,font=('Bold',16))
        restriccion.place(x=x,y=y)
    
    botonAgregarRestriccion.configure(state="disabled")
    botonEstandarizar.configure(state="disabled")

ventana = customtkinter.CTk()
ventana.configure(fg_color='#FAFBF6')
ventana.title('METODO SIMPLEX')
ventana.geometry('1133x695')
ventana.resizable(width=True,height=True)
#--------------------------------------------------------------Frames------------------------------------------------------------------------------
hoja = customtkinter.CTkFrame(master=ventana,width=1118,height=674,corner_radius=62,fg_color='#FAFBF6',border_width=1.5,border_color='#0099DB')
hoja.place(x=8,y=10)
funcionObjetivo = customtkinter.CTkFrame(master=hoja,width=1075,height=41,fg_color='#FAFBF6')
funcionObjetivo.place(x=21,y=80)
restricciones = customtkinter.CTkFrame(master=hoja,width=537.5,height=487,fg_color='#FAFBF6',border_width=1.5,border_color='black')
restricciones.place(x=21,y=132)
estandarizacion = customtkinter.CTkFrame(master=hoja,width=537.5,height=487,fg_color='#FAFBF6',border_width=1.5,border_color='black')
estandarizacion.place(x=560,y=132)
#-------------------------------------------------------------Textos-----------------------------------------------
tituloHoja = customtkinter.CTkLabel(master=hoja,text='MÉTODO SIMPLEX',font=('Bold',20))
tituloHoja.place(x=467,y=12)
tituloFuncionObejito = customtkinter.CTkLabel(master=funcionObjetivo,text='Fob =',font=('Bold',20))
tituloFuncionObejito.place(x=5,y=5)
tituloRestricciones = customtkinter.CTkLabel(master=restricciones,text='Sujeto a:',font=('Bold',16))
tituloRestricciones.place(x=15,y=2)
tituloEstandarizacion = customtkinter.CTkLabel(master=estandarizacion,text='Estandarización:',font=('Bold',16))
tituloEstandarizacion.place(x=15,y=2)
#---------------------------------------------------------------Botones----------------------------------------------------------------------------
botonEstandarizar = customtkinter.CTkButton(master=ventana,width=285,height=33,fg_color='#63C74D',border_color='#63C74D',border_width=1.2,text_color='#FAFBF6',font=('Bold',20),text='Estandarizar',command=lambda:estandarizar(entradasFuncionObjetivo,listaRestricciones))
botonEstandarizar.place(x=147,y=643)
botonResolver = customtkinter.CTkButton(master=ventana,width=285,height=33,fg_color='#63C74D',border_color='#63C74D',border_width=1.2,text_color='#FAFBF6',font=('Bold',20),text='Resolver')
botonResolver.place(x=721,y=643)
botonAgregarRestriccion = customtkinter.CTkButton(master=restricciones,width=157,height=23,fg_color='#FE8C42',border_color='#FE8C42',border_width=1.2,text_color='#FAFBF6',font=('Bold',15),text='Agregar restricción',command=lambda:agregar_restriccion(Y_botonAgregarRestriccion,listaRestricciones))
botonAgregarRestriccion.place(x=15,y=Y_botonAgregarRestriccion)
botonAgregarVariable= customtkinter.CTkButton(master=funcionObjetivo,width=10,height=4,border_spacing=0,fg_color='#63C74D',border_color='#63C74D',border_width=1.2,
text_color='#FAFBF6',font=('Bold',22),text='+',command=lambda:agregar_variable_funcionObjetivo(xbotonFuncionObjetivo,5,numeroVariable,entradasFuncionObjetivo,variablesFuncionObjetivo,sumasFuncionObjetivo))
botonAgregarVariable.place(x=xbotonFuncionObjetivo,y=5)

entradasFuncionObjetivo = []
variablesFuncionObjetivo = []
sumasFuncionObjetivo = []
listaRestricciones = []

agregar_entrada_variable_funcionObjetivo(60,5,entradasFuncionObjetivo)
agregar_entrada_variable_funcionObjetivo(125,5,entradasFuncionObjetivo)
agregar_texto_variable_funcionObjetivo(60,5,1,variablesFuncionObjetivo)
agregar_texto_variable_funcionObjetivo(125,5,2,variablesFuncionObjetivo)
agregar_suma_funcionObjetivo(60,5,sumasFuncionObjetivo)

ventana.mainloop()
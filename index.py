import json
import os
from objectivo import objectivo as item
from tkinter import *
objectivosPath="M:\\PRJCTS\\Contador\\objectivos.txt"

window=Tk()
window.geometry("420x420")
window.title("GoalTinker")
if os.path.exists(objectivosPath):
    if os.path.isfile(objectivosPath):
        if os.path.isdir(objectivosPath):
            print("Path working")
else:
    print("Path Problems")


try:
    with open('objectivos.txt') as file:
        label=Label(window,text="Os seus objectivos são: "+file.read())
        label.pack()
except FileNotFoundError:
    print("Ficheiro não foi encontrado")
def criar():
    windowCriar=Tk()
    windowCriar.geometry("420x420")
    windowCriar.title("Crie novo Objectivo")
    lb_Titulo=Label(windowCriar,text="Crie um novo Objectivo: ")
    lb_Titulo.pack()
    lb_nome=Label(windowCriar,text="Crie um novo Objectivo: ")
    lb_nome.pack()
    entry_nome=Entry(windowCriar)
    entry_nome.pack()
    lb_valorIni=Label(windowCriar,text="Escreva o valor inicial: ")
    lb_valorIni.pack()
    entry_valorIni=Entry(windowCriar)
    entry_valorIni.pack()
    lb_valorFinal=Label(windowCriar,text="Escreva o valor final: ")
    lb_valorFinal.pack()
    entry_valorFinal=Entry(windowCriar)
    entry_valorFinal.pack()
    nome_item=entry_nome.get()
    valor_inicial=entry_valorIni.get()
    valor_final=entry_valorFinal.get()
    pushUps=item(nome_item, valor_inicial, valor_final)
    bt_Finalizar=Button(windowCriar,text='Finalizar',command=lambda: finalizar(pushUps))
    bt_Finalizar.pack()

def finalizar(pushUps):
    with open('objectivos.txt','w') as file:
        file.write(str(pushUps))
        print("Novo objectivo adicionado",pushUps)
bt_Criar=Button(window,text='Criar Objectivo', command=criar)
bt_Criar.pack()
window.mainloop()



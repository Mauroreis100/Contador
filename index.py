import json
import os
from objectivo import objectivo as item
from tkinter import *
import csv
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

objectivos=[['Nome','Actual','Inicial','Final']]
objectivos_nr=0
try:
    with open('objectivos.csv', mode='r') as file:
        csvFile = csv.reader(file)
        i=0
        label=Label(window,text="Os seus objectivos são: ")
        label.pack()
        for lines in csvFile:  
            labelObjectivo=Label(window,text=lines)
            labelObjectivo.pack()
            print(objectivos)
            objectivos_nr=objectivos_nr+1
except FileNotFoundError:
    print("Ficheiro não foi encontrado")
# print(objectivos)
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
    bt_Finalizar=Button(windowCriar,text='Finalizar',command=lambda: finalizar(nome_item))
    bt_Finalizar.pack()

# with open('objectivos.csv', 'w') as csvfile:  
#     # creating a csv dict writer object  
#     writer = csv.DictWriter(csvfile, fieldnames = ['Nome','Actual','Inicial','Final'])  
        
#     # writing headers (field names)  
#     writer.writeheader()

def finalizar(nome_item):
    objectivos.append([nome_item])
    print(objectivos)
    
    # with open('objectivos.csv','w') as file:
    #     csvwriter = csv.writer(file)  
        
    #     # writing the fields  
    #     csvwriter.writerow(objectivos[0])  
        
    #     for j in range(objectivos_nr):
    #         if j!=0:
    #             csvwriter.writerows(objectivos[j]) 
bt_Criar=Button(window,text='Criar Objectivo', command=criar)
bt_Criar.pack()
window.mainloop()



import webbrowser #Permite a exibição de docs web aos usuários
import tkinter #Interface padrão do python para o kit de ferramentas TK
from time import sleep
root = tkinter.Tk( ) #Nome do sistema == root
root.title('Abrir browser') 
root.geometry('300x200') #Tamanho do sistema

def opensite():
    site = str(input('Digite o site a ser aberto: ')).strip().lower() #Abrindo o site antes de clicar no botão. 
    webbrowser.open(site)
#if site != '':
mysite = tkinter.Button(root, text=f'acessar', command=opensite).pack(pady=20)
root.mainloop()

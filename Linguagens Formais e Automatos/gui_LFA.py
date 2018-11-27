'''
    PARA FAZER:
        -Colocar botão para confirmar o alfabeto
        -Só permitir a inserção do primeiro estado, após a inserção do alfabeto
        -Colocar o botão para conversão
        -Implementar a renderização do AFN de retorno
        -Ver o caso da auto-transição
        -Sinalizar o estado selecionado, ao realizar as transições
'''
from tkinter import *

def limitSize_a1(*args):
    value = a1_val.get()
    if len(value) > 1: 
        a1_val.set(value[:1])
    else:
        if value[:1] in alfabeto:
            a1.config({"background": "#FF6262"})
        else:
            a1.config({"background": "White"})
            alfabeto[0] = value[:1]
    if len(value) == 0:
        a1.config({"background": "White"})

def limitSize_a2(*args):
    value = a2_val.get()
    if len(value) > 1: 
        a2_val.set(value[:1])
    else:
        if value[:1] in alfabeto:
            a2.config({"background": "#FF6262"})
        else:
            a2.config({"background": "White"})
            alfabeto[1] = value[:1]
    if len(value) == 0:
        a2.config({"background": "White"})

def limitSize_a3(*args):
    value = a3_val.get()
    if len(value) > 1: 
        a3_val.set(value[:1])
    else:    
        if value[:1] in alfabeto:
            a3.config({"background": "#FF6262"})
        else:
            a3.config({"background": "White"})
            alfabeto[2] = value[:1]
    if len(value) == 0:
        a3.config({"background": "White"})

def create_alfa_box():
    global alfaBox_init
    alfaBox_init = True
    #--------------DESATIVAR AS CAIXAS DE TEXTOS -----------------------
    tag = "alfa_box"
    canvas.create_rectangle(200, 200, 600, 300, fill="White", tags=tag)
    x=300
    if alfabeto[0] != '':
        obj = canvas.create_text(x, 250, fill="black", font="Times 18 bold", text=alfabeto[0], tags=tag)
        canvas.tag_bind(obj, "<ButtonPress-1>", selec_element_0)
        x+=100
    if alfabeto[1] != '':
        obj = canvas.create_text(x, 250, fill="black", font="Times 18 bold", text=alfabeto[1], tags=tag)
        canvas.tag_bind(obj, "<ButtonPress-1>", selec_element_1)
        x+=100
    if alfabeto[2] != '':
        obj = canvas.create_text(x, 250, fill="black", font="Times 18 bold", text=alfabeto[2], tags=tag)
        canvas.tag_bind(obj, "<ButtonPress-1>", selec_element_2)
        x+=100
    canvas.itemconfigure(tag, state="hidden")  

def selec_element_0(event):
    global t_x1, t_y1, t_x2, t_y2
    elemento = alfabeto[0]
    canvas.itemconfigure("alfa_box", state="hidden")
    Transicao(canvas, t_x1, t_y1, t_x2, t_y2, elemento)
    t_x1=t_y1=t_x2=t_y2=elemento=None

def selec_element_1(event):
    global t_x1, t_y1, t_x2, t_y2
    elemento = alfabeto[1]
    canvas.itemconfigure("alfa_box", state="hidden")
    Transicao(canvas, t_x1, t_y1, t_x2, t_y2, elemento)
    t_x1=t_y1=t_x2=t_y2=elemento=None

def selec_element_2(event):
    global t_x1, t_y1, t_x2, t_y2
    elemento = alfabeto[2]
    canvas.itemconfigure("alfa_box", state="hidden")
    Transicao(canvas, t_x1, t_y1, t_x2, t_y2, elemento)
    t_x1=t_y1=t_x2=t_y2=elemento=None

def criar_transicao(canvas, x1, y1, x2, y2):
    global t_x1, t_y1, t_x2, t_y2
    canvas.itemconfigure("alfa_box", state="normal")
    t_x1 = x1
    t_y1 = y1
    t_x2 = x2
    t_y2 = y2

#------------------------------- INICIO DO TKINTER ---------------------------------
root = Tk()
root.title("Conversor de AFe - AFN")
root.resizable(0,0)

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

root.update()

canvas.create_text(385, 30, fill="black", font="Times 20 bold", text="Conversor de AFe para AFN")

#------------------------- DEFINIÇÃO ALFABETO -------------------------------------
a1_val = StringVar()
a1_val.trace('w', limitSize_a1)
a1 = Entry(canvas, font="Times 14 bold", textvariable=a1_val)
a2_val = StringVar()
a2_val.trace('w', limitSize_a2)
a2 = Entry(canvas, font="Times 14 bold", textvariable=a2_val)
a3_val = StringVar()
a3_val.trace('w', limitSize_a3)
a3 = Entry(canvas, font="Times 14 bold", textvariable=a3_val)
confirm_alfabeto = Button(canvas, text = "Confirmar", font="Times", command=create_alfa_box)

canvas.create_text(50, 100, fill="black", font="Times 14 bold", text="Alfabeto:")
canvas.create_window(120, 100, window=a1, height=25, width=50)
canvas.create_window(200, 100, window=a2, height=25, width=50)
canvas.create_window(280, 100, window=a3, height=25, width=50)
canvas.create_window(380, 100, window=confirm_alfabeto, height=25, width=100)
#------------------------- FIM DEFINIÇÃO ALFABETO --------------------------------

alfabeto = [ "", "", ""]
alfaBox_init = False #controle da criação da caixa do alfabeto
estados = 0
transicoes = 0
x0=10
y0=180
x1=65
y1=235

#posições para realização da criação de transições
x1_lig=y1_lig=x2_lig=y2_lig=x3_lig=y3_lig=x4_lig=y4_lig=None
t_x1=t_y1=t_x2=t_y2=None

class Estado:
    def __init__(self, canvas, tipo, func):
        global x0, y0, x1, y1, estados, alfaBox_init
        self.canvas = canvas 
        self.tipo = tipo
        self.func = func
        self.obj = self.canvas.create_oval(x0, y0, x1, y1, width=1, fill='orange')
        self.obj2 = None
        self._drag_data = {"x": 0, "y": 0, "item": None}
        if tipo == 'normal':
            x0+=100
            x1+=100
        elif tipo == 'final':
            x0+=3
            y0+=3
            x1-=3
            y1-=3
            self.obj2 = self.canvas.create_oval(x0, y0, x1, y1, width=1, fill='orange') #cria um novo circulo e adiciona a representação de um estado final
            x0-=3
            y0-=3
            x1+=3
            y1+=3
            if func:
                y1+=150
                y0+=150
            else:
                x0+=100
                x1+=100
        if func:
            self.canvas.tag_bind(self.obj, "<Button-1>", self.criar_novo)
        else:
            self.text_label = "q"+str(estados+1)
            self.canvas.itemconfig(self.obj, tags=self.text_label)
            if self.obj2 != None:
                self.canvas.itemconfig(self.obj2, tags=self.text_label)
            self.canvas.create_text(x0-75, y0+25, fill="black", font="Times 12 bold", text=self.text_label, tags=self.text_label)
            self.canvas.tag_bind(self.text_label, "<Double-Button-1>", self.fazer_ligacao)
            self.canvas.tag_bind(self.text_label, "<Double-Button-3>", self.excluir)
            self.canvas.tag_bind(self.text_label, "<ButtonPress-1>", self.on_token_press)
            self.canvas.tag_bind(self.text_label, "<ButtonRelease-1>", self.on_token_release)
            self.canvas.tag_bind(self.text_label, "<B1-Motion>", self.on_token_motion)
            if self.obj2 != None:
                self.canvas.tag_bind(self.obj2, "<Button-1>", self.criar_novo)
    
    def criar_novo(self, event):
        global estados
        if estados < 5 and alfaBox_init:
            global x1_lig, y1_lig, x2_lig, y2_lig, x3_lig, y3_lig, x4_lig, y4_lig
            if x1_lig != None or x3_lig != None:
                x1_lig=y1_lig=x2_lig=y2_lig=x3_lig=y3_lig=x4_lig=y4_lig=None
            Estado(self.canvas, self.tipo, False)
            estados+=1
    
    def fazer_ligacao(self, event):
        global x1_lig, y1_lig, x2_lig, y2_lig, x3_lig, y3_lig, x4_lig, y4_lig, transicoes
        if transicoes < 7:
            if (x1_lig and y1_lig and x2_lig and y2_lig) == None:
                x1_lig, y1_lig, x2_lig, y2_lig = self.canvas.coords(self.obj)
            elif (x3_lig and y3_lig and x4_lig and y4_lig) == None:
                x3_lig, y3_lig, x4_lig, y4_lig = self.canvas.coords(self.obj)
                pm1 = (x1_lig+x2_lig)/2
                pm2 = (x3_lig+x4_lig)/2
                pm3 = (y1_lig+y2_lig)/2
                pm4 = (y3_lig+y4_lig)/2
                
                if abs(x3_lig - x2_lig) <= 60 and abs(y2_lig - y3_lig) >= 50:             
                    if y2_lig > y3_lig:
                        criar_transicao(self.canvas, pm1, y1_lig, pm2, y4_lig)
                    else:
                        criar_transicao(self.canvas, pm1, y2_lig, pm2, y3_lig)
                else:
                    if x3_lig > x2_lig:
                        criar_transicao(self.canvas, x2_lig, pm3, x3_lig, pm4)
                    else:
                        criar_transicao(self.canvas, x1_lig, pm3, x4_lig, pm4)

                x1_lig=y1_lig=x2_lig=y2_lig=x3_lig=y3_lig=x4_lig=y4_lig=None#limpa o controle de transição
    
    def excluir(self, event):
        global estados
        self.canvas.delete(self.text_label)
        estados-=1
    
    def on_token_press(self, event):
        self._drag_data["items"] = self.canvas.find_withtag(self.text_label)
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def on_token_release(self, event):
        self._drag_data["items"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def on_token_motion(self, event):
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["items"][0], delta_x, delta_y)
        self.canvas.move(self._drag_data["items"][1], delta_x, delta_y)
        if len(self._drag_data["items"]) > 2:
            self.canvas.move(self._drag_data["items"][2], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

class Transicao:
    def __init__(self, canvas, x0, y0, x1, y1, elemento):
        global transicoes, alfabeto
        transicoes+=1
        self.canvas = canvas
        self.tag = "t"+str(transicoes)
        self.obj = self.canvas.create_line(x0, y0, x1, y1, arrow=LAST, tags=self.tag)
        self.canvas.create_text((x0+x1)/2, y0+10, fill="black", font="Times 12 bold", text=elemento, tags=self.tag)
        self.canvas.tag_bind(self.obj, "<Double-Button-1>", self.excluir)

    def excluir(self, event):
        global transicoes
        transicoes-=1
        self.canvas.delete(self.tag)
        
Estado(canvas, 'normal', True)
Estado(canvas, 'final', True)  

root.mainloop()

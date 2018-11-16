'''
    PARA FAZER:
        -Organizar melhor o direcionamento das setas para as transições de estado
        -Ver o caso da auto-transição
        -Leitura do alfabeto
        -Nomear os estados
        -Colocar os labels nos estados
        -Colocar os labels nas transições
        -Implementar as regras
        -Colocar o botão para conversão
        -Sinalizar o estado selecionado, ao realizar as transições
        -Implementar a renderização do AFN de retorno
'''

from tkinter import *

root = Tk()
root.title("Conversor de AFe - AFN")
root.resizable(0,0)

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

root.update()

canvas.create_text(385, 30, fill="black", font="Times 20 bold", text="Conversor de AFe para AFN")

estados = 0
x0=5
y0=175
x1=60
y1=230

x1_lig=None
y1_lig=None
x2_lig=None
y2_lig=None
x3_lig=None
y3_lig=None
x4_lig=None
y4_lig=None

class Estado:
    def __init__(self, canvas, tipo, func):
        global x0, y0, x1, y1
        self.canvas = canvas 
        self.tipo = tipo
        self.func = func
        self.obj = self.canvas.create_oval(x0, y0, x1, y1, width=1, fill='orange')
        self._drag_data = {"x": 0, "y": 0, "item": None}
        if tipo == 'normal':
            x0+=100
            x1+=100
        elif tipo == 'final':
            x0+=3
            y0+=3
            x1-=3
            y1-=3
            self.obj = self.canvas.create_oval(x0, y0, x1, y1, width=1, fill='orange') #cria um novo circulo e adiciona a representação de um estado final
            y1+=150
            y0+=150
        if func:
            self.canvas.tag_bind(self.obj, "<Button-1>", self.criar_novo)
        else:
            self.canvas.tag_bind(self.obj, "<Double-Button-1>", self.fazer_ligacao)
            self.canvas.tag_bind(self.obj, "<Double-Button-3>", self.excluir)
            self.canvas.tag_bind(self.obj, "<ButtonPress-1>", self.on_token_press)
            self.canvas.tag_bind(self.obj, "<ButtonRelease-1>", self.on_token_release)
            self.canvas.tag_bind(self.obj, "<B1-Motion>", self.on_token_motion)
    
    def criar_novo(self, event):
        global x1_lig, y1_lig, x2_lig, y2_lig, x3_lig, y3_lig, x4_lig, y4_lig
        if x1_lig != None or x3_lig != None:
            x1_lig=y1_lig=x2_lig=y2_lig=x3_lig=y3_lig=x4_lig=y4_lig=None
        Estado(self.canvas, self.tipo, False)
    
    def fazer_ligacao(self, event):
        global x1_lig, y1_lig, x2_lig, y2_lig, x3_lig, y3_lig, x4_lig, y4_lig
        if (x1_lig and y1_lig and x2_lig and y2_lig) == None:
            x1_lig, y1_lig, x2_lig, y2_lig = self.canvas.coords(self.obj)
        elif (x3_lig and y3_lig and x4_lig and y4_lig) == None:
            x3_lig, y3_lig, x4_lig, y4_lig = self.canvas.coords(self.obj)
            pm1 = (x1_lig+x2_lig)/2
            pm2 = (x3_lig+x4_lig)/2
            pm3 = (y1_lig+y2_lig)/2
            pm4 = (y3_lig+y4_lig)/2
            if x3_lig - x2_lig >= 50:
                Transicao(self.canvas, x2_lig, pm3, x3_lig, pm4)
            else:
                Transicao(self.canvas, pm1, y2_lig, pm2, y3_lig)
            x1_lig=y1_lig=x2_lig=y2_lig=x3_lig=y3_lig=x4_lig=y4_lig=None#limpa o controle de transição
    
    def excluir(self, event):
        self.canvas.delete(self.obj)
    
    def on_token_press(self, event):
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def on_token_release(self, event):
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def on_token_motion(self, event):
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

class Transicao:
    def __init__(self, canvas, x0, y0, x1, y1):
        self.canvas = canvas
        self.obj = self.canvas.create_line(x0, y0, x1, y1, arrow=LAST)
        self.canvas.tag_bind(self.obj, "<Double-Button-1>", self.excluir)

    def excluir(self, event):
        self.canvas.delete(self.obj)
        
Estado(canvas, 'normal', True)
Estado(canvas, 'final', True)

root.mainloop()

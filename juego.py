from tkinter import Tk, Button, Label, Entry, IntVar, messagebox

def botonReinicio():
    global contador, turno, puntaje, puntaje2
    contador = 0
    turno = 1
    puntaje.set(0)
    puntaje2.set(0)

    b1.config(text=" ")
    b2.config(text=" ")
    b3.config(text=" ")
    b4.config(text=" ")
    b5.config(text=" ")
    b6.config(text=" ")
    b7.config(text=" ")
    b8.config(text=" ")
    b9.config(text=" ")

def botonLimpiar():
    global contador, turno
    contador = 0
    turno = 1

    b1.config(text=" ")
    b2.config(text=" ")
    b3.config(text=" ")
    b4.config(text=" ")
    b5.config(text=" ")
    b6.config(text=" ")
    b7.config(text=" ")
    b8.config(text=" ")
    b9.config(text=" ")

def c1():
    global turno, contador
    if b1["text"] == " ":
        if turno == 1:
            turno = 2
            b1["text"] = "X"
        elif turno == 2:
            turno = 1
            b1["text"] = "O"
        contador = contador + 1 
        comparar()

def c2():
    global turno, contador
    if b2["text"] == " ":
        if turno == 1:
            turno = 2
            b2["text"] = "X"
        elif turno == 2:
            turno = 1
            b2["text"] = "O"
        contador = contador + 1 
        comparar()

def c3():
    global turno, contador
    if b3["text"] == " ":
        if turno == 1:
            turno = 2
            b3["text"] = "X"
        elif turno == 2:
            turno = 1
            b3["text"] = "O"
        contador = contador + 1 
        comparar()

def c4():
    global turno, contador
    if b4["text"] == " ":
        if turno == 1:
            turno = 2
            b4["text"] = "X"
        elif turno == 2:
            turno = 1
            b4["text"] = "O"
        contador = contador + 1 
        comparar()

def c5():
    global turno, contador
    if b5["text"] == " ":
        if turno == 1:
            turno = 2
            b5["text"] = "X"
        elif turno == 2:
            turno = 1
            b5["text"] = "O"
        contador = contador + 1 
        comparar()

def c6():
    global turno, contador
    if b6["text"] == " ":
        if turno == 1:
            turno = 2
            b6["text"] = "X"
        elif turno == 2:
            turno = 1
            b6["text"] = "O"
        contador = contador + 1 
        comparar()


def c7():
    global turno, contador
    if b7["text"] == " ":
        if turno == 1:
            turno = 2
            b7["text"] = "X"
        elif turno == 2:
            turno = 1
            b7["text"] = "O"
        contador = contador + 1 
        comparar()
        

def c8():
    global turno, contador
    if b8["text"] == " ":
        if turno == 1:
            turno = 2
            b8["text"] = "X"
        elif turno == 2:
            turno = 1
            b8["text"] = "O"
        contador = contador + 1 
        comparar()

def c9():
    global turno, contador
    if b9["text"] == " ":
        if turno == 1:
            turno = 2
            b9["text"] = "X"
        elif turno == 2:
            turno = 1
            b9["text"] = "O"
        contador = contador + 1 
        comparar()

def comparar():
    global contador

    if b1["text"]==b2["text"]  and b1["text"]==b3["text"]  and b1["text"]=="X":
        p =  puntaje.get()+1
        entr1.config(textvariable=puntaje.set(p))
        messagebox.showinfo("Tateti","Ganaste Jugador X ") 

    elif b1["text"]==b2["text"]  and b1["text"]==b3["text"]  and b1["text"]=="O":
        n =  puntaje2.get()+1
        entr2.config(textvariable=puntaje2.set(n))
        messagebox.showinfo("Tateti","Ganaste Jugador O ") 

    elif b4["text"]== b5["text"]  and b4["text"]==b6["text"]  and b4["text"]=="X":
        p =  puntaje.get()+1
        entr1.config(textvariable=puntaje.set(p))
        messagebox.showinfo("Tateti","Ganaste Jugador X ") 

    elif b4["text"]== b5["text"]  and b4["text"]==b6["text"]  and b4["text"]=="O":
        n =  puntaje2.get()+1
        entr2.config(textvariable=puntaje2.set(n))
        messagebox.showinfo("Tateti","Ganaste Jugador O ") 

    elif b7["text"] ==b8["text"]  and b7["text"] ==b9["text"] and b7["text"] =="X":
        p =  puntaje.get()+1
        entr1.config(textvariable=puntaje.set(p))
        messagebox.showinfo("Tateti","Ganaste Jugador X ") 

    elif b7["text"] ==b8["text"]  and b7["text"] ==b9["text"] and b7["text"] =="O":
        n =  puntaje2.get()+1
        entr1.config(textvariable=puntaje2.set(n))
        messagebox.showinfo("Tateti","Ganaste Jugador O ")

    elif b1["text"]==b4["text"] and b1["text"]==b7["text"]  and b1["text"]=="X":
        p =  puntaje.get()+1
        entr1.config(textvariable=puntaje.set(p))
        messagebox.showinfo("Tateti","Ganaste Jugador X ")

    elif b1["text"]==b4["text"] and b1["text"]==b7["text"]  and b1["text"]=="O":
        n =  puntaje2.get()+1
        entr2.config(textvariable=puntaje2.set(n))
        messagebox.showinfo("Tateti","Ganaste Jugador O ")

    elif b2["text"] == b5["text"]  and b2["text"] ==b8["text"]  and b2["text"] =="X":
        p =  puntaje.get()+1
        entr1.config(textvariable=puntaje.set(p))
        messagebox.showinfo("Tateti","Ganaste Jugador X ") 

    elif b2["text"] == b5["text"]  and b2["text"] ==b8["text"]  and b2["text"] =="O":
        n =  puntaje2.get()+1
        entr2.config(textvariable=puntaje2.set(n))
        messagebox.showinfo("Tateti","Ganaste Jugador O ") 

    elif b3["text"] ==b6["text"]  and b3["text"] ==b9["text"] and b3["text"] =="X":
        p =  puntaje.get()+1
        entr1.config(textvariable=puntaje.set(p))
        messagebox.showinfo("Tateti","Ganaste Jugador X ") 

    elif b3["text"] ==b6["text"]  and b3["text"] ==b9["text"] and b3["text"] =="O":
        n =  puntaje2.get()+1
        entr2.config(textvariable=puntaje2.set(n))
        messagebox.showinfo("Tateti","Ganaste Jugador O ")

    elif b1["text"]== b5["text"]  and b1["text"]==b9["text"] and b1["text"]=="X":
        p =  puntaje.get()+1
        entr1.config(textvariable=puntaje.set(p))
        messagebox.showinfo("Tateti","Ganaste Jugador X ") 

    elif b1["text"]== b5["text"]  and b1["text"]==b9["text"] and b1["text"]=="O":
        n =  puntaje2.get()+1
        entr2.config(textvariable=puntaje2.set(n))
        messagebox.showinfo("Tateti","Ganaste Jugador O ") 

    elif b7["text"] == b5["text"]  and b7["text"] ==b3["text"]  and b7["text"] =="X":
        p =  puntaje.get()+1
        entr1.config(textvariable=puntaje.set(p))
        messagebox.showinfo("Tateti","Ganaste Jugador X ") 

    elif b7["text"] == b5["text"]  and b7["text"] ==b3["text"]  and b7["text"] =="O":
        n =  puntaje2.get()+1
        entr2.config(textvariable=puntaje2.set(n))
        messagebox.showinfo("Tateti","Ganaste Jugador O ")

    elif contador == 9:
        messagebox.showinfo("Tateti","Empate")

def botonSalir():
    vn.destroy()

vn = Tk()
vn.title("Tres en raya")
vn.geometry("400x520")
vn.config(bg='#90EE90')
vn.resizable(False,False)

puntaje = IntVar()
puntaje2= IntVar()

contador = 0
turno = 1

limpiar=Button(vn,text="LIMPIAR",bg='#90EE90',font=("Liberation Mono", 10),height=3, width = 11,command=botonLimpiar)
limpiar.place(x=40, y=430)

reiniciar=Button(vn,text="REINICIAR",bg='#90EE90',font=("Liberation Mono", 10),height=3, width = 11,command=botonReinicio)
reiniciar.place(x=150, y=430)

salir=Button(vn,text="SALIR",bg='#90EE90',font=("Liberation Mono", 10),height=3, width = 11,command=botonSalir)
salir.place(x=260, y=430)

p1 = Label(vn, font=("Liberation Mono", 11),bg='#90EE90',text="Puntaje X : ")
p1.place(x=40, y=30)
entr1 = Entry(vn, font=("Liberation Mono", 11),bg='#90EE90',textvariable=puntaje, width=3)
entr1.place(x=120, y=30)

p2 = Label(vn, font=("Liberation Mono", 11),bg='#90EE90',text="Puntaje O : ")
p2.place(x=220, y=30)
entr2 = Entry(vn, font=("Liberation Mono", 11),bg='#90EE90',textvariable=puntaje2, width=3)
entr2.place(x=300, y=30)


b1 = Button(vn,text=" ",command=c1, height=6, width=15)
b1.place(x=25,y=90)
b2 = Button(vn, text=" ",command=c2,height=6, width=15)
b2.place(x=145, y=90)
b3 = Button(vn, text=" ",command=c3,height=6, width=15)
b3.place(x=265,y=90)
b4 = Button(vn, text=" ",command=c4,height=6, width=15)
b4.place(x=25,y=197)
b5 = Button(vn, text=" ",command=c5,height=6, width=15)
b5.place(x=145, y=197)
b6 = Button(vn, text=" ",command=c6,height=6, width=15)
b6.place(x=265, y=197)
b7 = Button(vn, text=" ",command=c7,height=6, width=15)
b7.place(x=25, y=304)
b8 = Button(vn, text=" ",command=c8,height=6, width=15)
b8.place(x=145, y=304)
b9 = Button(vn, text=" ",command=c9,height=6, width=15)
b9.place(x=265, y=304)

vn.mainloop()
from tkinter import *

co = Tk()
c1 = Frame(co)
c2= Frame(co)

#frame c1
bt1 = Label(c1, text='Tela Inicial', font='Arial 15')
bt2 = Button(c1, text='Cadastrar Peças', font='Arial 15', command=lambda: [c1.pack_forget(), c2.pack()])
bt3 = Button(c1, text='Listar Peças', font='Arial 15', command=lambda: [c1.pack_forget(), c2.pack()])

bt1.grid(row=0, column=0)
bt2.grid(row=1, column=0)
bt3.grid(row=2, column=0)

#frame c2
Tela_cadastro = Label(c2, text='Tela cadastro', font='Arial 15')
Cod = Label(c2, text='Cod.', font='Arial 15')
campo_Cod= Entry(c2)
Descrição = Label(c2, text='Descrição', font='Arial 15')
campo_descrição= Entry(c2)
Fabricante = Label(c2, text='Fabricante', font='Arial 15')
campo_fabricante= Entry(c2)
Quantidade = Label(c2, text='Quantidade', font='Arial 15')
campo_quantidade= Entry(c2)
bt1 = Button (c2, text='Finalizar ', font='Arial 15')
bt2 = Button (c2, text='Voltar', font='Arial 15', command = c1.destroy)

Tela_cadastro.grid(row=0,column=0)
Cod.grid(row=1,column=0)
campo_Cod.grid(row=1,column=1)
Descrição.grid(row=2,column=0)
campo_descrição.grid(row=2,column=1)
Fabricante.grid(row=3,column=0)
campo_fabricante.grid(row=3,column=1)
Quantidade.grid(row=4,column=0)
campo_quantidade.grid(row=4,column=1)
bt1.grid(row=5, column=0)
bt2.grid(row=5, column=1)

c1.pack()

co.mainloop()

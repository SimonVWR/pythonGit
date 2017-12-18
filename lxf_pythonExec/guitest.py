from tkinter import *
import tkinter.messagebox as messagebox

class application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.lblInof = Label(self, text='输入名字')
        self.lblInof.pack()
        self.txtNameInput = Entry(self)
        self.txtNameInput.pack()
        self.btnShowHello = Button(self, text ='Hello', command=self.btnClickShowHello)
        self.btnShowHello.pack()
        self.btnQuit = Button(self, text='Quit', command=self.quit)
        self.btnQuit.pack()

    def btnClickShowHello(self):
        username = self.txtNameInput.get() or 'guest'
        messagebox.showinfo('say hello', 'Hello %s'%username)

    def quit(self):
        Frame.quit(self)


app = application()
app.master.title( 'my first python gui app')
app.mainloop()
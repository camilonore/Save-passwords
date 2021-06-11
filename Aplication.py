from Functions import Functions
from tkinter import *

bg_color = '#031E25'
fg_color = '#FFF'


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=450, bg=bg_color)
        self.master = master
        self.pack()
        self.createMain()

# Interfaz principal
    def createMain(self):
        fr1 = Frame(self, bg=bg_color)
        fr1.place(x=45, y=50)
        Label(fr1, text='What do you want to do?', bg=bg_color,
              fg=fg_color).pack(padx=100, pady=10)
        Button(fr1, text='Delete a password', fg=fg_color,
               bg=bg_color, height=2, command=lambda: self.deleteFunction('delete')).pack(ipadx=95, pady=10)
        Button(fr1, text='Add a password', fg=fg_color,
               bg=bg_color, height=2, command=lambda: self.addFunction('add')).pack(ipadx=100, pady=10)
        Button(fr1, text='Know your save password',
               fg=fg_color, bg=bg_color, height=2, command=lambda: self.knowPassword('know')).pack(ipadx=75, pady=10)
        Button(fr1, text='Change your password', fg=fg_color,
               bg=bg_color, height=2, command=lambda: self.changeButton('change')).pack(ipadx=85, pady=10)
        Button(fr1, text='Quit', fg=fg_color, bg=bg_color,
                         command=self.master.destroy, height=2).pack(ipadx=75, pady=55)

# Interfaz para añadir nueva contraseña
    def addFunction(self, function):
        fr1 = Frame(self, bg=bg_color)
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg=bg_color, fg=fg_color)
        lbl1.pack()
        self.domain = Entry(fr1, bg=bg_color, fg=fg_color,
                            insertbackground=fg_color)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        lbl2 = Label(fr1, text='Write the email', bg=bg_color, fg=fg_color)
        lbl2.pack()
        self.email = Entry(fr1, bg=bg_color, fg=fg_color,
                           insertbackground=fg_color)
        self.email.pack(padx=80, pady=5, ipadx=80, ipady=5)
        lbl3 = Label(fr1, text='Write the password', bg=bg_color, fg=fg_color)
        lbl3.pack()
        self.password = Entry(fr1, bg=bg_color, fg=fg_color,
                              insertbackground=fg_color)
        self.password.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.buttons(fr1, 50)
        self.function = function

# Interfaz para conocer una contraseña
    def knowPassword(self, function):
        def doneButtonKnow():
            domain = self.domain.get()
            knowPasswordHowto = Functions(
                self.function, domain).KnowPassword(self.privatekey.get())
            self.domain.delete(0, 'end')
            fr1 = Frame(self, bg=bg_color)
            fr1.place(x=-10, y=50)
            lbl1 = Label(fr1, text='Your password is:',
                         bg=bg_color, fg=fg_color)
            lbl1.pack(padx=155, pady=20, ipadx=5)
            lbl2 = Label(fr1, text=knowPasswordHowto,
                         bg=bg_color, fg=fg_color)
            lbl2.pack(padx=155, pady=25, ipady=40)
            self.buttons(fr1, 175, 'doneButtonKnow')
        fr1 = Frame(self, bg=bg_color)
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg=bg_color, fg=fg_color)
        lbl1.pack()
        self.domain = Entry(fr1, bg=bg_color, fg=fg_color,
                            insertbackground=fg_color)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.function = function
        lbl2 = Label(fr1, text='Enter your private key',
                     bg=bg_color, fg=fg_color)
        lbl2.pack(pady=5)
        self.privatekey = Entry(
            fr1, show='*', bg=bg_color, fg=fg_color, insertbackground=fg_color)
        self.privatekey.pack(padx=80, pady=5, ipadx=80, ipady=5)
        donebtn = Button(fr1, text='Done!',
                         command=doneButtonKnow, fg=fg_color, bg=bg_color)
        donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
        returnbtn = Button(fr1, text='Return',
                           command=self.createMain, fg=fg_color, bg=bg_color)
        returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
        quitbtn = Button(fr1, text='Quit',
                         command=self.master.destroy, fg=fg_color, bg=bg_color)
        quitbtn.pack(pady=80, ipadx=70)

# Funcionalidad del boton cambiar contraseña
    def changeButton(self, function):
        def doneButtonDelete():
            Functions(self.function, self.domain.get(),
                      None, None, self.newpassword.get())
            self.domain.delete(0, 'end')
            self.newpassword.delete(0, 'end')
            fr1 = Frame(self, bg=bg_color)
            fr1.place(x=-10, y=50)
        self.function = function
        fr1 = Frame(self, bg=bg_color)
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg=bg_color, fg=fg_color)
        lbl1.pack()
        self.domain = Entry(fr1, bg=bg_color, fg=fg_color,
                            insertbackground=fg_color)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        lbl2 = Label(fr1, text='Write your new password',
                     bg=bg_color, fg=fg_color)
        lbl2.pack()
        self.newpassword = Entry(
            fr1, bg=bg_color, fg=fg_color, insertbackground=fg_color)
        self.newpassword.pack(padx=80, pady=10, ipadx=80, ipady=5)
        donebtn = Button(fr1, text='Done!',
                         command=doneButtonDelete, fg=fg_color, bg=bg_color)
        donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
        self.buttons(fr1, 95, 'doneButtonDelete')

# Interfaz para eliminar una contraseña
    def deleteFunction(self, function):
        fr1 = Frame(self, bg=bg_color)
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg=bg_color, fg=fg_color)
        lbl1.pack()
        self.domain = Entry(fr1, bg=bg_color, fg=fg_color,
                            insertbackground=fg_color)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.function = function
        self.buttons(fr1)

# Funcionalidad del boton completar
    def doneButton(self, frame):
        if self.function == 'add':
            domain = self.domain.get()
            email = self.email.get()
            password = self.password.get()
            Functions(self.function, domain, email, password)
            self.domain.delete(0, 'end')
            self.email.delete(0, 'end')
            self.password.delete(0, 'end')
        else:
            domain = self.domain.get()
            Functions(self.function, domain)
            self.domain.delete(0, 'end')

# Metodo para la creacion de botones
    def buttons(self, frame, pady=175, name=None):
        if name == None:
            donebtn = Button(frame, text='Done!',
                             command=lambda: self.doneButton(frame), fg=fg_color, bg=bg_color)
            donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
            returnbtn = Button(frame, text='Return',
                               command=self.createMain, fg=fg_color, bg=bg_color)
            returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
            quitbtn = Button(frame, text='Quit',
                             command=self.master.destroy, fg=fg_color, bg=bg_color)
            quitbtn.pack(pady=pady, ipadx=70)
        elif name == 'doneButtonKnow':
            returnbtn = Button(frame, text='Return',
                               command=lambda: self.knowPassword('know'), fg=fg_color, bg='yellow')
            returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
            quitbtn = Button(frame, text='Quit',
                             command=self.master.destroy, fg=fg_color, bg=bg_color)
            quitbtn.pack(pady=40, ipadx=80)
        elif name == 'doneButtonDelete':
            returnbtn = Button(frame, text='Return',
                               command=self.createMain, fg=fg_color, bg=bg_color)
            returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
            quitbtn = Button(frame, text='Quit',
                             command=self.master.destroy, fg=fg_color, bg=bg_color)
            quitbtn.pack(pady=pady, ipadx=70)


if __name__ == '__main__':
    Application

from Functions import Functions
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=450, bg='#40322F')
        self.master = master
        self.pack()
        self.createMain()

    def createMain(self):
        fr1 = Frame(self, bg='#40322F')
        fr1.place(x=45, y=50)
        Label(fr1, text='What do you want to do?', bg='#40322F',
              fg='#FFF').pack(padx=100, pady=10)
        Button(fr1, text='Delete a password', fg='#FFF',
               bg='red', command=lambda: self.deleteFunction('delete')).pack(ipadx=95, pady=10)
        Button(fr1, text='Add a password', fg='#FFF',
               bg='green', command=lambda: self.addFunction('add')).pack(ipadx=100, pady=10)
        Button(fr1, text='Know your save password',
               fg='#000', bg='yellow', command=lambda: self.knowPassword('know')).pack(ipadx=75, pady=10)
        Button(fr1, text='Change your password', fg='#000',
               bg='orange', command=lambda: self.changeButton('change')).pack(ipadx=85, pady=10)
        Button(fr1, text='Quit', fg='white', bg='red',
                         command=self.master.destroy).pack(ipadx=75, pady=100)

    def addFunction(self, function):
        fr1 = Frame(self, bg='#40322F')
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg='#40322F', fg='#FFF')
        lbl1.pack()
        self.domain = Entry(fr1)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        lbl2 = Label(fr1, text='Write the email', bg='#40322F', fg='#FFF')
        lbl2.pack()
        self.email = Entry(fr1)
        self.email.pack(padx=80, pady=5, ipadx=80, ipady=5)
        lbl3 = Label(fr1, text='Write the password', bg='#40322F', fg='#FFF')
        lbl3.pack()
        self.password = Entry(fr1)
        self.password.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.buttons(fr1, 50)
        self.function = function

    def knowPassword(self, function):
        def doneButtonKnow():
            domain = self.domain.get()
            knowPasswordHowto = Functions(
                self.function, domain).KnowPassword(self.privatekey.get())
            self.domain.delete(0, 'end')
            fr1 = Frame(self, bg='#40322F')
            fr1.place(x=-10, y=50)
            lbl1 = Label(fr1, text='Your password is:',
                         bg='#40322F', fg='#FFF')
            lbl1.pack(padx=155, pady=20, ipadx=5)
            lbl2 = Label(fr1, text=knowPasswordHowto,
                         bg='#40322F', fg='#FFF')
            lbl2.pack(padx=155, pady=25, ipady=40)
            self.buttons(fr1, 175, 'doneButtonKnow')
        fr1 = Frame(self, bg='#40322F')
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg='#40322F', fg='#FFF')
        lbl1.pack()
        self.domain = Entry(fr1)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.function = function
        lbl2 = Label(fr1, text='Enter your private key',
                     bg='#40322F', fg='#FFF')
        lbl2.pack(pady=5)
        self.privatekey = Entry(fr1, show='*')
        self.privatekey.pack(padx=80, pady=5, ipadx=80, ipady=5)
        donebtn = Button(fr1, text='Done!',
                         command=doneButtonKnow, fg='white', bg='green')
        donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
        returnbtn = Button(fr1, text='Return',
                           command=self.createMain, fg='black', bg='yellow')
        returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
        quitbtn = Button(fr1, text='Quit',
                         command=self.master.destroy, fg='white', bg='red')
        quitbtn.pack(pady=80, ipadx=70)

    def changeButton(self, function):
        def doneButtonDelete():
            Functions(self.function, self.domain.get(),
                      None, None, self.newpassword.get())
            self.domain.delete(0, 'end')
            self.newpassword.delete(0, 'end')
            fr1 = Frame(self, bg='#40322F')
            fr1.place(x=-10, y=50)
            lbl1 = Label(fr1, text='Password changed successfully',
                         bg='#40322F', fg='green')
            lbl1.pack(padx=145, pady=20, ipadx=5)
        self.function = function
        fr1 = Frame(self, bg='#40322F')
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg='#40322F', fg='#FFF')
        lbl1.pack()
        self.domain = Entry(fr1)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        lbl2 = Label(fr1, text='Write your new password',
                     bg='#40322F', fg='#FFF')
        lbl2.pack()
        self.newpassword = Entry(fr1)
        self.newpassword.pack(padx=80, pady=10, ipadx=80, ipady=5)
        donebtn = Button(fr1, text='Done!',
                         command=doneButtonDelete, fg='white', bg='green')
        donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
        self.buttons(fr1, 95, 'doneButtonDelete')

    def deleteFunction(self, function):
        fr1 = Frame(self, bg='#40322F')
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg='#40322F', fg='#FFF')
        lbl1.pack()
        self.domain = Entry(fr1)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.function = function
        self.buttons(fr1)

    def doneButton(self):
        self.prueba = 'prueba'
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

    def buttons(self, frame, pady=175, name=None):
        if name == None:
            donebtn = Button(frame, text='Done!',
                             command=self.doneButton, fg='white', bg='green')
            donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
            returnbtn = Button(frame, text='Return',
                               command=self.createMain, fg='black', bg='yellow')
            returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
            quitbtn = Button(frame, text='Quit',
                             command=self.master.destroy, fg='white', bg='red')
            quitbtn.pack(pady=pady, ipadx=70)
        elif name == 'doneButtonKnow':
            returnbtn = Button(frame, text='Return',
                               command=lambda: self.knowPassword('know'), fg='black', bg='yellow')
            returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
            quitbtn = Button(frame, text='Quit',
                             command=self.master.destroy, fg='white', bg='red')
            quitbtn.pack(pady=40, ipadx=80)
        elif name == 'doneButtonDelete':
            returnbtn = Button(frame, text='Return',
                               command=self.createMain, fg='black', bg='yellow')
            returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
            quitbtn = Button(frame, text='Quit',
                             command=self.master.destroy, fg='white', bg='red')
            quitbtn.pack(pady=pady, ipadx=70)


if __name__ == '__main__':
    Application

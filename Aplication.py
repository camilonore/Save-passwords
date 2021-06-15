from Functions import Functions
from tkinter import *

bg_color = '#031E25'
fg_color = '#FFF'


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=450, bg=bg_color)
        self.master = master
        self.pack()
        self.privatetime = Functions.checkprivatetime(Functions())
        if self.privatetime == True:
            self.privateKeyFrame()
        else:
            self.createMain()

    # Private key interface
    def privateKeyFrame(self):
        self.privatetime += 1
        fr1 = Frame(self, bg=bg_color)
        fr1.place(x=-10, y=20)
        Label(fr1, text="Write your private key (Don't forget it)", bg=bg_color,
              fg=fg_color).pack(padx=10, pady=40)
        self.privatekeyMain = Entry(fr1, bg=bg_color, fg=fg_color, show='*',
                                    insertbackground=fg_color)
        self.privatekeyMain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.buttons(fr1, 180, 'privatekey')

    # Main interface
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

    # Interface to add new password
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
        self.password = Entry(fr1, bg=bg_color, fg=fg_color, show='*',
                              insertbackground=fg_color)
        self.password.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.buttons(fr1, 50)
        self.function = function

    # Interface to know a password
    def knowPassword(self, function):
        def doneButtonKnow():
            domain = self.domain.get()
            knowPasswordHowto = Functions(
                self.function, domain).KnowPassword(self.privatekey.get())
            self.domain.delete(0, 'end')
            fr1 = Frame(self, bg=bg_color)
            fr1.place(x=-10, y=50)
            lbl1 = Label(fr1, text='Your password is:',
                         bg=bg_color, fg='#FFF')
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

    # Functionality of the change password button
    def changeButton(self, function):
        def doneButtonDelete():
            Functions(self.function, self.domain.get(),
                      None, None, self.newpassword.get())
            self.domain.delete(0, 'end')
            self.newpassword.delete(0, 'end')
            fr1 = Frame(self, bg=bg_color)
            fr1.place(x=-10, y=50)
            self.successFrame()
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
            fr1, bg=bg_color, fg=fg_color, show='*', insertbackground=fg_color)
        self.newpassword.pack(padx=80, pady=10, ipadx=80, ipady=5)
        donebtn = Button(fr1, text='Done!',
                         command=doneButtonDelete, fg=fg_color, bg=bg_color)
        donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
        self.buttons(fr1, 95, 'doneButtonDelete')

    # Interface to remove a password
    def deleteFunction(self, function):
        def delete():
            domain = self.domain.get()
            Functions(self.function, domain)
            self.domain.delete(0, 'end')
            self.successFrame()
        fr1 = Frame(self, bg=bg_color)
        fr1.place(x=-10, y=50)
        lbl1 = Label(fr1, text='Write the domain name',
                     bg=bg_color, fg=fg_color)
        lbl1.pack()
        self.domain = Entry(fr1, bg=bg_color, fg=fg_color,
                            insertbackground=fg_color)
        self.domain.pack(padx=80, pady=5, ipadx=80, ipady=5)
        self.function = function
        donebtn = Button(fr1, text='Done!',
                         command=delete, fg=fg_color, bg=bg_color)
        donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
        self.buttons(fr1,95,"doneButtonDelete")

    # Done button functionality

    def doneButton(self, function):
        if function == 'add':
            domain = self.domain.get()
            email = self.email.get()
            password = self.password.get()
            Functions(function, domain, email, password)
            self.domain.delete(0, 'end')
            self.email.delete(0, 'end')
            self.password.delete(0, 'end')
            self.successFrame()
        elif function == 'privatekey':
            privatekey = self.privatekeyMain.get()
            Functions(function, None, None, None, None, privatekey)
            self.privatekeyMain.delete(0, 'end')
            self.createMain()

        else:
            pass
            # domain = self.domain.get()
            # Functions(self.function, domain)
            # self.domain.delete(0, 'end')
            # self.successFrame()

    # Method for creating buttons
    def buttons(self, frame, pady=175, name=None):
        if name == None:
            donebtn = Button(frame, text='Done!',
                             command=lambda: self.doneButton('add'), fg=fg_color, bg=bg_color)
            donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
            returnbtn = Button(frame, text='Return',
                               command=self.createMain, fg=fg_color, bg=bg_color)
            returnbtn.pack(padx=80, pady=20, ipadx=55, ipady=5)
            quitbtn = Button(frame, text='Quit',
                             command=self.master.destroy, fg=fg_color, bg=bg_color)
            quitbtn.pack(pady=pady, ipadx=70)
        elif name == 'doneButtonKnow':
            returnbtn = Button(frame, text='Return',
                               command=lambda: self.knowPassword('know'), fg=fg_color, bg=bg_color)
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
            quitbtn.pack(pady=180, ipadx=70)
        elif name == 'privatekey':
            donebtn = Button(frame, text='Done!',
                             command=lambda: self.doneButton(name), fg=fg_color, bg=bg_color)
            donebtn.pack(padx=80, pady=5, ipadx=60, ipady=5)
            quitbtn = Button(frame, text='Quit',
                             command=self.master.destroy, fg=fg_color, bg=bg_color)
            quitbtn.pack(pady=pady, ipadx=70)

# Frame of action performed satisfactorily
    def successFrame(self):
        fr1 = Frame(self, bg=bg_color)
        fr1.place(x=0, y=332)
        lbl1 = Label(fr1, text="SUCCESSFULLY",
                     bg=bg_color, fg='#40D044')
        lbl1.pack(padx=155, pady=20, ipadx=5)


if __name__ == '__main__':
    Application

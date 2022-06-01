#importar bibliotecas

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import width
import database

#criar janela

jan=Tk()
jan.title("ZZ Zystems - Access")
jan.geometry("600x500")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="logos/logo.ico")

#upload logo

logo = PhotoImage(file="logos/logo.png")

#frames

LeftFrame=Frame(jan, width=200, height=300, bg="grey20", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="grey20", relief="raise")
RightFrame.pack(side=RIGHT)

#logo

LogoLabel=Label(LeftFrame, image=logo, bg="grey20")
LogoLabel.place(x=20, y=100)

#dados

UserLabel=Label(RightFrame, text="Username:", font=("Veridiana", 16), bg="grey20", fg="light grey")
UserLabel.place(x=20, y=100)

UserEntry=ttk.Entry(RightFrame, width=30)
UserEntry.place(x=130, y=105)

PassLabel = Label(RightFrame, text="Password:", font=("Veridiana", 16), bg="grey20", fg="light grey")
PassLabel.place(x=20, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=130, y=155)

#buttons

def Login():
    user = UserEntry.get()
    password = PassEntry.get()

    database.cursor.execute("""
    SELECT * FROM users 
    WHERE (user = ? AND password = ?)
    """, (user, password))
    print("Ok")
    VerifyLogin = database.cursor.fetchone()
    try:
        if (user in VerifyLogin and password in VerifyLogin):
            messagebox.showinfo(title="Info", message="Access confirmed")
        else:
            pass
    except:
        messagebox.showinfo(title="Alert", message="Email or password incorrect")


LoginButton=ttk.Button(RightFrame, text="Login", width=20, command=Login)
LoginButton.place(x=120, y=210)

def Register():
    #removendo buttons para register
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #inserindo dados de cadastro
    NameLabel=Label(RightFrame, text="Name:", font=("Veridiana", 16), bg="grey20", fg="light grey")
    NameLabel.place(x=20, y=10)

    NameEntry=ttk.Entry(RightFrame, width=35)
    NameEntry.place(x=100, y=15)

    EmailLabel = Label(RightFrame, text="Email:", font=("Veridiana", 16), bg="grey20", fg="light grey")
    EmailLabel.place(x=20, y=60)

    EmailEntry = ttk.Entry(RightFrame, width=35)
    EmailEntry.place(x=100, y=65)

    #database

    def Registerdatabase():
        name = NameEntry.get()
        email = EmailEntry.get()
        user = UserEntry.get()
        password = PassEntry.get()

        if (name == "" and email == "" and user == "" and password == ""):
            messagebox.showerror(title="Error", message="Please, fill all the fields")
        else:
            database.cursor.execute("""
            INSERT INTO users(name, email, user, password) VALUES(?, ?, ?, ?)
            """, (name, email, user, password))
            database.conn.commit()
            messagebox.showinfo(title="Registration", message="Registration complete")

    Register=ttk.Button(RightFrame, text="Register", width=20, command=Registerdatabase)
    Register.place(x=125, y=200)

    def BacktoLogin():
        #removendo dados de cadastro
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=50000)
        Back.place(x=5000)
        #trazer de volta outros dados
        LoginButton.place(x=120)
        RegisterButton.place(x=150)


    Back=ttk.Button(RightFrame, text="Back", width=20, command=BacktoLogin)
    Back.place(x=125, y=240)


RegisterButton = ttk.Button(RightFrame, text="Register", width=10, command=Register)
RegisterButton.place(x=150, y=250)

jan.mainloop()
import tkinter
import hashlib
import pygame
import re
import tkinter.messagebox as tkmb
import customtkinter as ctk
from tkinter.messagebox import showerror, showinfo
from tkinter import *

regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]w+[.]w{2,3}$'

data_user1 = []
data_user = []

root = ctk.CTk()
root.geometry('350x530')
root.configure(bg='#000000')
root.title('Login Form')

window_width = 350
window_height = 530

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

f = tkinter.Frame(bg='#000000', highlightbackground="gray", highlightthickness=2, pady=30, padx=30)

l_login = tkinter.Label(f, text='Login', font=('Elephant', 28), fg='#FFFFFF', bg='#000000')
l_UserName = tkinter.Label(f, text='UserName:', font=('ATROX normal', 18), fg='#FFFFFF', bg='#000000')
l_Password = tkinter.Label(f, text='Password:', font=('ATROX normal', 18), fg='#FFFFFF', bg='#000000')

with open('u-p.txt', 'a+') as file:
    pass


def data_append():
    u_p = open('u-p.txt', 'r')
    while True:
        line = u_p.readline()

        if not line:
            break

        data_user1.append(line.strip().split(' '))


data_append()


def data_append1():
    u_p = open('u-p.txt', 'r')
    while True:
        line = u_p.readline()

        if not line:
            break

        data_user.append(line.strip().split(' '))


data_append1()


def login():
    for i in range(len(data_user)):
        if hashlib.md5(Username_entry.get().encode()).hexdigest() in data_user[i] and hashlib.md5(
                Password_entry.get().encode()).hexdigest() in data_user[i]:
            root.destroy()
            page_3 = tkinter.Tk()
            page_3.configure(bg='#000000')
            page_3.title('Wellcome Form')
            page_3.attributes('-fullscreen', True)

            f2 = tkinter.Frame(bg='#000000', highlightbackground="gray", highlightthickness=2, pady=30, padx=30)

            lb_wellcome = tkinter.Label(f2, text=f"Wellcome \n Your Login Was \n Succesful", font=('Elephant', 28),
                                        fg='#FFFFFF', bg='#000000')
            lb_rebot = tkinter.Label(f2, text=f"Please Close The Page", font=('Elephant', 15), fg='#FFFFFF',
                                     bg='#000000')

            def close():
                tkmb.showinfo(title='Close', message='Are You Sure to Leave Us', icon='question')
                page_3.destroy()

            btn_close = tkinter.Button(f2, text='Close', font=('Limelight Regular', 16), command=close, fg='#fa0505',
                                       relief='flat')

            lb_wellcome.grid(row=0, column=0, columnspan=2, pady=40, sticky='news')
            lb_rebot.grid(row=1, column=0, pady=20, padx=60)

            btn_close.grid(row=2, column=0, padx=60)

            f2.pack(expand=1)
            return

    tkmb.showerror(title='Error', message='Your Username or Password Is not Right', icon='warning')
    return


def close():
    tkmb.showinfo(title='Close', message='Are You Sure to Leave Us', icon='question')
    root.destroy()


def info():
    showinfo(title="Creator Information",
             message=f"Email: rexlepyo@gmail.com\n Name: Amir Mahdi Goodarzi\n Phone Number: 09910807943\n Version: v0.0.1")


def register():
    root.destroy()
    register_page = tkinter.Tk()
    register_page.geometry('500x400')
    register_page.configure(bg='#000000')
    register_page.title('Regester Form')

    window_width = 350
    window_height = 500

    screen_width = register_page.winfo_screenwidth()
    screen_height = register_page.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    register_page.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

    f1 = tkinter.Frame(bg='#000000', highlightbackground="gray", highlightthickness=2, pady=30, padx=30)

    lb_regester = tkinter.Label(f1, text='Regester', font=('Elephant', 32), fg='#FFFFFF', bg='#000000')
    lb_name = tkinter.Label(f1, text='First Name:', font=('ATROX normal', '18'), fg='#FFFFFF', bg='#000000')
    lb_last_name = tkinter.Label(f1, text=' Last Name:', font=('ATROX normal', '18'), fg='#FFFFFF', bg='#000000')
    lb_password = tkinter.Label(f1, text=' Password:', font=('ATROX normal', '18'), fg='#FFFFFF', bg='#000000')
    lb_rpassword = tkinter.Label(f1, text=' Password:', font=('ATROX normal', '18'), fg='#FFFFFF', bg='#000000')
    lb_email = tkinter.Label(f1, text='      Email:', font=('ATROX normal', '18'), fg='#FFFFFF', bg='#000000')

    def close():
        tkmb.showinfo(title='Close', message='Tap Ok To Close This Page', icon='question')
        register_page.destroy()

    def is_valid_email(email):
        return re.match(regex, email) is not None

    def validate_email():

        istrue = 0

        if name_entry.get() == '':
            tkmb.showerror(title='Error', message='Please Enter Your Name', icon='warning')
        else:
            istrue += 1
        if last_name_entry.get() == '':
            tkmb.showerror(title='Error', message='Please Enter Your Last Name', icon='warning')
        else:
            istrue += 1
        if password_entry2.get() == '':
            tkmb.showerror(title='Error', message='Please Enter Your User Password', icon='warning')
        else:
            istrue += 1
        if is_valid_email(email_entry.get()):
            istrue += 1
        else:
            tkmb.showerror(title='Error', message='enter a valid email', icon='warning')

        if istrue == 3 and password_entry2.get() == rpassword_entry.get() and len(password_entry2.get()) and len(
                rpassword_entry.get()) == 8:
            file = open("u-p.txt", 'a+')
            file.write(hashlib.md5(name_entry.get().encode()).hexdigest() + ' ')
            file.write(hashlib.md5(password_entry2.get().encode()).hexdigest() + '\n')
            file.close()

            register_page.destroy()

            data_user1 = []

            root1 = tkinter.Tk()
            root1.geometry('350x530')
            root1.configure(bg='#000000')
            root1.title('Login Form')

            window_width = 350
            window_height = 530

            screen_width = root1.winfo_screenwidth()
            screen_height = root1.winfo_screenheight()

            x = (screen_width / 2) - (window_width / 2)
            y = (screen_height / 2) - (window_height / 2)

            root1.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

            f5 = tkinter.Frame(bg='#000000', highlightbackground="gray", highlightthickness=2, pady=30, padx=30)

            # login page labels fonts and bg and fg
            l_login1 = tkinter.Label(f5, text='Login', font=('Elephant', 28), fg='#FFFFFF', bg='#000000')
            l_UserName1 = tkinter.Label(f5, text='UserName:', font=('ATROX normal', 18), fg='#FFFFFF', bg='#000000')
            l_Password1 = tkinter.Label(f5, text='Password:', font=('ATROX normal', 18), fg='#FFFFFF', bg='#000000')

            def regester1():
                showerror(title='Error', message='You Regestered Befor This')
                return

            def data_append1():
                u_p = open('u-p.txt', 'r')
                while True:
                    line = u_p.readline()

                    if not line:
                        break

                    data_user1.append(line.strip().split(' '))

            data_append1()

            def close1():
                showinfo(title='Close', message='Are You Sure to Leave Us')
                root1.destroy()

            def info1():
                showinfo(title="Creator Information",
                         message=f"Email: rexlepyo@gmail.com\n Name: Amir Mahdi Goodarzi\n Phone Number: 09910807943\n Version: v0.0.1")

            def toggle_password6():
                if Password_entry1.cget('show') == '':
                    Password_entry1.config(show='+')
                    toggle_btn1.config(text='Show password')

                else:
                    Password_entry1.config(show='')
                    toggle_btn1.config(text='Hide password')

            def login1():
                for i in range(len(data_user1)):
                    if hashlib.md5(Username_entry1.get().encode()).hexdigest() in data_user1[i] and hashlib.md5(
                            Password_entry1.get().encode()).hexdigest() in data_user1[i]:
                        root1.destroy()
                        page_4 = tkinter.Tk()
                        page_4.configure(bg='#000000')
                        page_4.title('Wellcome Form')
                        page_4.attributes('-fullscreen', True)

                        f6 = tkinter.Frame(bg='#000000', highlightbackground="gray", highlightthickness=2, pady=30,
                                           padx=30)

                        lb_wellcome1 = tkinter.Label(f6, text=f"Wellcome \n Your Login Was \n Succesful",
                                                     font=('Elephant', 28), fg='#FFFFFF', bg='#000000')
                        lb_rebot1 = tkinter.Label(f6, text=f"Please Close The Page", font=('Elephant', 15),
                                                  fg='#FFFFFF', bg='#000000')

                        def close2():
                            tkmb.showinfo(title='Close', message='Are You Sure to Leave Us', icon='question')
                            page_4.destroy()

                        btn_close1 = tkinter.Button(f6, text='Close', font=('Limelight Regular', 16), command=close2,
                                                    fg='#fa0505', relief='flat')

                        lb_wellcome1.grid(row=0, column=0, columnspan=2, pady=40, sticky='news')
                        lb_rebot1.grid(row=1, column=0, pady=20, padx=60)

                        btn_close1.grid(row=2, column=0, padx=60)

                        f6.pack(expand=1)

                        return

                tkmb.showerror(title='Error', message='Your Username or Password Is not Right', icon='warning')
                return

            def play_music1():
                pygame.mixer.music.load("Secession Studios - Sundance Kid.mp3")
                pygame.mixer.music.play()

            def pause_music1():

                pygame.mixer.music.pause()

            play_button1 = Button(f5, text="Play Music", font=('Limelight Regular', 10), fg='#494949', relief='flat',
                                  command=play_music1)
            pause_btn1 = tkinter.Button(f5, text=('Pause'), font=('Limelight Regular', 10), fg='#494949', relief='flat',
                                        command=pause_music1)

            regester_btn1 = tkinter.Button(f5, text='Rege', font=('Limelight Regular', 16), command=regester1,
                                           fg='#494949', relief='flat')
            info_btn1 = tkinter.Button(f5, text='Info', font=('Limelight Regular', 16), command=info1, fg='#494949',
                                       relief='flat')
            Exsit_btn1 = tkinter.Button(f5, text='Close', font=('Limelight Regular', 16), command=close1, fg='#fa0505',
                                        relief='flat')
            Login_btn1 = tkinter.Button(f5, text='Login', font=('Limelight Regular', 16), command=login1, fg='#494949',
                                        relief='flat')
            toggle_btn1 = tkinter.Button(f5, text='Show password', font=('Limelight Regular', 10), width=0, height=0,
                                         fg='#494949', relief='flat', command=toggle_password6)

            Username_entry1 = tkinter.Entry(f5, bg='#494949', fg='#ffffff', relief='flat')
            Password_entry1 = tkinter.Entry(f5, show='+', bg='#494949', fg='#ffffff', relief='flat')

            toggle_btn1.grid(row=7, column=0, columnspan=2, pady=8)
            l_login1.grid(row=0, column=0, columnspan=2, pady=40, sticky='news')
            l_UserName1.grid(row=2, column=0)
            l_Password1.grid(row=3, column=0)

            Username_entry1.grid(row=2, column=1)
            Password_entry1.grid(row=3, column=1)

            Login_btn1.grid(row=4, column=1, columnspan=1, pady=15)
            Exsit_btn1.grid(row=5, column=1, columnspan=3)
            info_btn1.grid(row=4, column=0, columnspan=1, pady=1, ipadx=5)
            regester_btn1.grid(row=5, column=0, columnspan=1, ipadx=2)

            play_button1.grid(row=8, column=0, columnspan=2, pady=1)
            pause_btn1.grid(row=9, column=0, columnspan=2, pady=8)

            f5.pack(expand=1)

            root1.mainloop()
        else:
            tkmb.showerror(title='Error', message='Please Enter FuLL Password', icon='warning')

        if istrue == 4 and password_entry2.get() != rpassword_entry.get():
            tkmb.showerror(title='Error', message='Your Passwords Are Not The Same', icon='warning')

    def toggle_password3():
        if rpassword_entry.cget('show') == '':
            rpassword_entry.config(show='+')
            toggle_btn2.config(text='Show password')

        else:
            rpassword_entry.config(show='')
            toggle_btn2.config(text='Hide password')

        if password_entry2.cget('show') == '':
            password_entry2.config(show='+')
            toggle_btn2.config(text='Show password')

        else:
            password_entry2.config(show='')
            toggle_btn2.config(text='Hide password')

    password_entry2 = tkinter.Entry(f1, show='+', bg='#494949', fg='#ffffff', relief='flat')

    rpassword_entry = tkinter.Entry(f1, show='+', bg='#494949', fg='#ffffff', relief='flat')
    toggle_btn2 = tkinter.Button(f1, text='Show password', font=('Limelight Regular', 10), width=0, height=0,
                                 fg='#494949', relief='flat', command=toggle_password3)
    toggle_btn2.grid(row=9, column=0, columnspan=2)

    name_entry = tkinter.Entry(f1, bg='#494949', fg='#ffffff', relief='flat')
    last_name_entry = tkinter.Entry(f1, bg='#494949', fg='#ffffff', relief='flat')
    email_entry = tkinter.Entry(f1, bg='#494949', fg='#ffffff', relief='flat')
    password_entry2 = tkinter.Entry(f1, bg='#494949', fg='#ffffff', relief='flat', show='+')
    rpassword_entry = tkinter.Entry(f1, bg='#494949', fg='#ffffff', relief='flat', show='+')

    btn_regester = tkinter.Button(f1, text='Reges', font=('Limelight Regular', 16), command=validate_email,
                                  fg='#494949', relief='flat')
    btn_close = tkinter.Button(f1, text='Close', font=('Limelight Regular', 16), command=close, fg='#fa0505',
                               relief='flat')

    lb_regester.grid(row=0, column=0, columnspan=2, pady=40)
    lb_name.grid(row=3, column=0)
    lb_last_name.grid(row=4, column=0)
    lb_password.grid(row=5, column=0)
    lb_rpassword.grid(row=6, column=0)
    lb_email.grid(row=7, column=0)

    name_entry.grid(row=3, column=1)
    last_name_entry.grid(row=4, column=1)
    password_entry2.grid(row=5, column=1)
    rpassword_entry.grid(row=6, column=1)
    email_entry.grid(row=7, column=1)

    btn_regester.grid(row=8, column=0, pady=10)
    btn_close.grid(row=8, column=1, pady=10)

    f1.pack(expand=1)

    register.mainloop()


def toggle_password():
    if Password_entry.cget('show') == '':
        Password_entry.config(show='+')
        toggle_btn.config(text='Show password')

    else:
        Password_entry.config(show='')
        toggle_btn.config(text='Hide password')


pygame.mixer.init()


def play_music():
    # Load music file
    pygame.mixer.music.load("Secession Studios - Sundance Kid.mp3")

    # Play music
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


play_button = tkinter.Button(f, text="Play Music", font=('Limelight Regular', 10), fg='#494949', relief='flat',
                             command=play_music)
pause_btn = tkinter.Button(f, text='Pause', font=('Limelight Regular', 10), fg='#494949', relief='flat',
                           command=pause_music)

register_btn = tkinter.Button(f, text='Rege', font=('Limelight Regular', 16), command=register, fg='#494949',
                              relief='flat')
info_btn = tkinter.Button(f, text='Info', font=('Limelight Regular', 16), command=info, fg='#494949', relief='flat')
Exit_btn = tkinter.Button(f, text='Close', font=('Limelight Regular', 16), command=close, fg='#fa0505', relief='flat')
Login_btn = tkinter.Button(f, text='Login', font=('Limelight Regular', 16), command=login, fg='#494949', relief='flat')
toggle_btn = tkinter.Button(f, text='Show password', font=('Limelight Regular', 10), width=0, height=0, fg='#494949',
                            relief='flat', command=toggle_password)

Username_entry = tkinter.Entry(f, bg='#494949', fg='#ffffff', relief='flat')
Password_entry = tkinter.Entry(f, show='+', bg='#494949', fg='#ffffff', relief='flat')

toggle_btn.grid(row=7, column=0, columnspan=2, pady=8)
l_login.grid(row=0, column=0, columnspan=2, pady=40, sticky='news')
l_UserName.grid(row=2, column=0)
l_Password.grid(row=3, column=0)

Username_entry.grid(row=2, column=1)
Password_entry.grid(row=3, column=1)

Login_btn.grid(row=4, column=1, columnspan=1, pady=15)
Exit_btn.grid(row=5, column=1, columnspan=3)
info_btn.grid(row=4, column=0, columnspan=1, pady=1, ipadx=5)
register_btn.grid(row=5, column=0, columnspan=1, ipadx=2)

play_button.grid(row=8, column=0, columnspan=2, pady=1)
pause_btn.grid(row=9, column=0, columnspan=2, pady=8)

f.pack(expand=1)

root.mainloop()
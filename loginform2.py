import customtkinter as ctk
import hashlib
from register_form.Registerform import register_window
from CTkMessagebox import CTkMessagebox
from hover.hover import CreateToolTip


regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]w+[.]w{2,3}$'

data_user = []

# ---------------------------------------------------function's---------------------------------------------------------


u_p = open('u-p.txt', 'a+')


def data_append():
    """This function read file and add everything in data_user_register_form variable"""
    global u_p
    u_p = open('u-p.txt', 'r')
    # set a True loop to read line's of u_p file
    while True:
        line = u_p.readline()

        # if file is empty warn and break
        if not line:
            break
        # and is file was not empty its add line's in list
        data_user.append(line.strip().split(' '))


data_append()


def login_check():
    """This function check if you do not register_form do that first"""
    for i in range(len(data_user)):
        if hashlib.md5(username_entry.get().encode()).hexdigest() in data_user[i] and hashlib.md5(
                password_entry.get().encode()).hexdigest() in data_user[i]:
            login_window.destroy()

            wellcome_window = ctk.CTk()
            wellcome_window.title('Wellcome Form')

            wellcome_window_width = 700
            wellcome_window_height = 400

            wellcome_screen_width = wellcome_window.winfo_screenwidth()
            wellcome_screen_height = wellcome_window.winfo_screenheight()

            x_axis = (wellcome_screen_width / 2) - (wellcome_window_width / 2)
            y_axis = (wellcome_screen_height / 2) - (wellcome_window_height / 2)

            wellcome_window.geometry('%dx%d+%d+%d' % (wellcome_window_width, wellcome_window_height, x_axis, y_axis))

            frame_welcome_form = ctk.CTkFrame(wellcome_window)
            frame_welcome_form.pack(expand=1)

            wellcome_label = ctk.CTkLabel(frame_welcome_form, text=f"Wellcome \n Your Login Was \n Successful",
                                          font=('Elephant', 28), bg_color='#2b2b2b')
            wellcome_label.grid(row=0, column=0, columnspan=2, pady=40, sticky='news')

            close_label = ctk.CTkLabel(frame_welcome_form, text=f"Please Close The Page", font=('Elephant', 15),
                                       bg_color='#2b2b2b')
            close_label.grid(row=1, column=0, pady=20, padx=60)

            btn_close = ctk.CTkButton(frame_welcome_form, text='Close', font=('Limelight Regular', 16),
                                      command=wellcome_window.destroy, fg_color='#494949', width=10,
                                      hover_color='#707070')
            btn_close.grid(row=2, column=0, padx=60, pady=30)

            wellcome_window.mainloop()
        elif username_entry.get() == '':
            CTkMessagebox(title="Error", message="Enter your Username please", icon="cancel")
        elif password_entry.get() == '':
            CTkMessagebox(title="Error", message="Enter your Password please", icon="cancel")
        elif hashlib.md5(username_entry.get().encode()).hexdigest() not in data_user[i]:
            CTkMessagebox(title="Error", message="Username not found please register_form first", icon="cancel")
        elif hashlib.md5(password_entry.get().encode()).hexdigest() not in data_user[i]:
            CTkMessagebox(title="Error", message="Password not found please register_form first", icon="cancel")
        else:
            CTkMessagebox(title="Error", message="Something wrong", icon="cancel")

        return


def info():
    """This function have info of creator"""
    CTkMessagebox(title="Info", message="Email: Example\n"
                                        "Name: Amir REXLEP\n"
                                        "Version: v0.0.2")


def toggle_password():
    """This function change the show of password entry"""
    if password_entry.cget('show') == '':
        password_entry.configure(show='+')
        toggle_btn.configure(text='Show password')

    else:
        password_entry.configure(show='')
        toggle_btn.configure(text='Hide password')


# ---------------------------------------------------UI-----------------------------------------------------------------

login_window = ctk.CTk()
login_window.geometry('350x530')
login_window.configure(bg='#000000')
login_window.title('Login Form')

window_width = 350
window_height = 530

screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()

x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

login_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

frame_login_window = ctk.CTkFrame(login_window, corner_radius=15)
frame_login_window.pack(expand=1)

login_label = ctk.CTkLabel(frame_login_window,
                           text='Login', font=('Elephant', 70), fg_color='#2b2b2b')
login_label.grid(row=0, column=0, columnspan=2, padx=30, pady=50, sticky='news')

username_entry = ctk.CTkEntry(frame_login_window,
                              bg_color='#2b2b2b', placeholder_text="Username")
username_entry.grid(row=2, column=0, columnspan=2, pady=10)

password_entry = ctk.CTkEntry(frame_login_window,
                              show='+', bg_color='#2b2b2b', placeholder_text="Password")
password_entry.grid(row=3, column=0, columnspan=2, padx=10)

register_btn = ctk.CTkButton(frame_login_window,
                             text='Rege', font=('Britannic Bold', 16), fg_color='#494949', width=10,
                             hover_color='#707070', command=register_window.mainloop)
register_btn.grid(row=5, column=0, columnspan=1, ipadx=2)

info_btn = ctk.CTkButton(frame_login_window,
                         text='Info', font=('Britannic Bold', 16), fg_color='#494949', width=10,
                         hover_color='#707070', command=info)
info_btn.grid(row=4, column=0, columnspan=1,  pady=1, ipadx=5)

exit_btn = ctk.CTkButton(frame_login_window,
                         text='Close', font=('Britannic Bold', 16), fg_color='#fa0505', width=10,
                         hover_color='#707070', command=login_window.destroy)
exit_btn.grid(row=5, column=1, columnspan=3)

login_btn = ctk.CTkButton(frame_login_window,
                          text='Login', font=('Britannic Bold', 16), fg_color='#494949', width=10,
                          hover_color='#707070', command=login_check)
login_btn.grid(row=4, column=1, columnspan=1, pady=15)

toggle_btn = ctk.CTkButton(frame_login_window,
                           text='Show password', font=('Britannic Bold', 15), width=8, fg_color='#494949',
                           hover_color='#707070', command=toggle_password)
toggle_btn.grid(row=7, column=0, columnspan=2, pady=15)

CreateToolTip(register_btn, 'Register')
CreateToolTip(info_btn, 'Info')
CreateToolTip(exit_btn, 'Exit')
CreateToolTip(exit_btn, 'Login')
CreateToolTip(toggle_btn, 'Change')

login_window.mainloop()

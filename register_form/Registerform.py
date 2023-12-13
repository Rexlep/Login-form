import customtkinter as ctk
import hashlib
import re
from CTkMessagebox import CTkMessagebox


data_user_register_form = []

# ---------------------------------------------------function's---------------------------------------------------------


u_p = open('../u-p.txt', 'a+')


def validate_email(email):
    """This function validate your email"""
    # Define the regex pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        # if email was ok
        return True
    else:
        # if email was not ok
        return False


def data_append_register_form():
    """This function read file and add everything in data_user_register_form variable"""
    global u_p
    u_p = open('../u-p.txt', 'r')
    # set a True loop to read line's of u_p file
    while True:
        line = u_p.readline()

        # if file is empty warn and break
        if not line:
            print("u_p file is empty")
            break
        # and is file was not empty its add line's in list
        data_user_register_form.append(line.strip().split(' '))


data_append_register_form()


def write_things(username_e, password_e):
    """This function check if list is entered info's in list show an error"""
    hashed_username = hashlib.md5(username_e.encode()).hexdigest()
    hashed_password = hashlib.md5(password_e.encode()).hexdigest()

    # Check if the hashed username and password exist in data_user_register_form
    exists = False
    for data in data_user_register_form:
        if hashed_username in data and hashed_password in data and validate_email(email_entry_register_window.get()):
            exists = True
            break

    # if entered info not in list add them
    if not exists:
        with open('../u-p.txt', 'w') as file:
            # its write hashed like this 63eefbd45d89e8c91f24b609f7539942 25d55ad283aa400af464c76d713c07ad
            file.write(f"{hashed_username} {hashed_password}\n")
            CTkMessagebox(title="Success", message="Registration successful", icon="info")
    else:  # returns the True
        CTkMessagebox(title="Error", message="You are already registered", icon="cancel")


def registration():
    """This function check if entry empty or length of password is less show error"""
    # check if username not empty
    if username_entry_register_window.get() == '':
        CTkMessagebox(title="Error", message="Please enter your Name", icon="cancel")
        return
    # check if password not empty
    elif password_entry_register_window.get() == '':
        CTkMessagebox(title="Error", message="Please enter your Password", icon="cancel")
        return
    # check if repeat password not empty
    elif repeat_password_entry_register_window.get() == '':
        CTkMessagebox(title="Error", message="Please repeat your Password", icon="cancel")
        return
    # check if email not empty
    elif email_entry_register_window.get() == '':
        CTkMessagebox(title="Error", message="Please enter your Email", icon="cancel")
        return
    # check if email is valid
    elif not validate_email(email_entry_register_window.get()):  # Add email validation check
        CTkMessagebox(title="Error", message="Invalid email. Please enter a valid email address.", icon="cancel")
        return
    # check if password are same
    elif password_entry_register_window.get() != repeat_password_entry_register_window.get():
        CTkMessagebox(title="Error", message="Passwords do not match.", icon="cancel")
        return
    # check if password length is good to go
    elif len(password_entry_register_window.get()) < 8:
        CTkMessagebox(title="Error", message="Password should have at least 8 characters.", icon="cancel")
        return

    # and if everything was ok its hash info's then write them
    hashed_username = hashlib.md5(username_entry_register_window.get().encode()).hexdigest()
    hashed_password = hashlib.md5(password_entry_register_window.get().encode()).hexdigest()

    for data in data_user_register_form:
        # first check if info in file
        if hashed_username in data and hashed_password in data:
            CTkMessagebox(title="Error", message="You are already registered", icon="cancel")
            break
    else:
        # if was not write them
        write_things(username_entry_register_window.get(), password_entry_register_window.get())


def toggle_password_register_form():
    """This function change the show of password entry"""
    if password_entry_register_window.cget('show') == '' and repeat_password_entry_register_window.cget('show') == '':
        password_entry_register_window.configure(show='+')
        repeat_password_entry_register_window.configure(show='+')
        toggle_btn_register_window.configure(text='Show password')

    else:
        password_entry_register_window.configure(show='')
        repeat_password_entry_register_window.configure(show='')
        toggle_btn_register_window.configure(text='Hide password')


# ---------------------------------------------------UI-----------------------------------------------------------------


register_window = ctk.CTk()
register_window.geometry('500x400')
register_window.title('Register Form')

register_window_width = 400
register_window_height = 600

register_screen_width = register_window.winfo_screenwidth()
register_screen_height = register_window.winfo_screenheight()

x = (register_screen_width / 2) - (register_window_width / 2)
y = (register_screen_height / 2) - (register_window_height / 2)

register_window.geometry('%dx%d+%d+%d' % (register_window_width, register_window_height, x, y))

frame_register_window = ctk.CTkFrame(register_window)
frame_register_window.pack(expand=1)

register_label = ctk.CTkLabel(frame_register_window,
                              text='Register', font=('Elephant', 70), bg_color='#2b2b2b')
register_label.grid(row=0, column=0, columnspan=2, padx=10, pady=50)

username_entry_register_window = ctk.CTkEntry(frame_register_window,
                                              bg_color='#2b2b2b', placeholder_text="Username")
username_entry_register_window.grid(row=2, column=0, columnspan=2, pady=5)

password_entry_register_window = ctk.CTkEntry(frame_register_window,
                                              bg_color='#2b2b2b', show='+', placeholder_text="Password")
password_entry_register_window.grid(row=5, column=0, columnspan=2, pady=5)

repeat_password_entry_register_window = ctk.CTkEntry(frame_register_window,
                                                     bg_color='#2b2b2b', show='+', placeholder_text="Repeat password")
repeat_password_entry_register_window.grid(row=6, column=0, columnspan=2, pady=5)

email_entry_register_window = ctk.CTkEntry(frame_register_window,
                                           bg_color='#2b2b2b', placeholder_text="Email")
email_entry_register_window.grid(row=7, column=0, columnspan=2, pady=5)

info_btn_register_window = ctk.CTkButton(frame_register_window,
                                         text='Info', font=('Britannic Bold', 16), fg_color='#494949', width=10,
                                         hover_color='#707070', command=None)
info_btn_register_window.grid(row=8, column=0, columnspan=1, pady=1, ipadx=5)

register_btn_register_window = ctk.CTkButton(frame_register_window,
                                             text='Rege', font=('Britannic Bold', 16), fg_color='#494949', width=10,
                                             hover_color='#707070', command=registration)
register_btn_register_window.grid(row=9, column=0, columnspan=1, ipadx=2)

Exit_btn_register_window = ctk.CTkButton(frame_register_window,
                                         text='Close', font=('Britannic Bold', 16), fg_color='#fa0505', width=10,
                                         hover_color='#707070', command=register_window.destroy)
Exit_btn_register_window.grid(row=9, column=1, columnspan=3)

Login_btn_register_window = ctk.CTkButton(frame_register_window,
                                          text='Login', font=('Britannic Bold', 16), fg_color='#494949', width=10,
                                          hover_color='#707070', command=register_window.destroy)
Login_btn_register_window.grid(row=8, column=1, columnspan=1, pady=15)

toggle_btn_register_window = ctk.CTkButton(frame_register_window, text='Show password', font=('Britannic Bold', 15),
                                           width=8, fg_color='#494949', hover_color='#707070',
                                           command=toggle_password_register_form)
toggle_btn_register_window.grid(row=10, column=0, columnspan=2, pady=15)

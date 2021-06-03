from tkinter import *
from tkinter import messagebox

# Initializing the window
root = Tk()
# Creating a title
root.title('Authentication')
# Setting the window size
root.geometry('400x400')
# Ensuring the window size cannot be adjusted
root.resizable('False', 'False')
# Setting a background color
root.config(bg='#d177f7')

# Creating & positioning the header with a background color
header = Label(root, text='Please enter login details', bg='#bc5cd6')
header.place(relx=0.3, rely=0.1)

# Creating & positioning the username label with a background color
username = Label(root, text='Username', bg='#d177f7')
username.place(relx=0.3, rely=0.2)

# Creating & positioning the username entry point with a background color
userEntry = Entry(root, bg='#d0cbd1')
userEntry.place(relx=0.3, rely=0.3)

# Creating & positioning the password label with a background color
password = Label(root, text='Password', bg='#d177f7')
password.place(relx=0.3, rely=0.4)

# Creating & positioning the password entry point with a background color
passEntry = Entry(root, bg='#d0cbd1')
passEntry.place(relx=0.3, rely=0.5)

# Setting usernames and passwords
user_key = {'Zoe': 'green-bean', 'Adam': 'avo', 'Ronald': 'dekapaan'}


# Making the login button functional
def authenticate():
    name = userEntry.get()
    passkey = passEntry.get()
    try:
        if name == '' or passkey == '':
            messagebox.showerror(message='Please enter details')

        elif name in user_key:
            if passkey == user_key[name]:
                messagebox.showinfo(message='Successful')
            else:
                messagebox.showerror(message='Incorrect password')

        else:
            messagebox.showerror(message='Invalid username')
    except ValueError:
        messagebox.showerror('Error')


# Making the clear button functional
def delete():
    userEntry.delete(0, END)
    userEntry.focus()
    passEntry.delete(0, END)
    passEntry.focus()


# Creating & positioning the login button with a background color
loginButton = Button(root, text='Login', bg='#bc5cd6', command=authenticate)
loginButton.place(relx=0.45, rely=0.68)

# Creating & positioning the clear button with a background color
clearButton = Button(root, text='Clear', bg='#bc5cd6', command=delete)
clearButton.place(relx=0.3, rely=0.8)

# Creating & positioning the exit button with a background color
exitButton = Button(root, text='Exit', bg='#bc5cd6', command='exit')
exitButton.place(relx=0.58, rely=0.8)

root.mainloop()

from tkinter import *
from tkinter import messagebox


# Initializing the window
root = Tk()
# Creating a title
root.title('Exception handling')
# Setting the window size
root.geometry('300x200')
# Ensuring the window size cannot be adjusted
root.resizable('False', 'False')
# Setting a background color
root.config(bg='#d177f7')

# Creating & positioning the label with a background color
label = Label(root, text='Please enter amount in your account', bg='#bc5cd6')
label.place(relx=0.1, rely=0.2)

# Creating & positioning the entry point with a background color
entry = Entry(root, bg='#d0cbd1')
entry.place(relx=0.22, rely=0.4)


# Making the check button functional
def check():
    if entry.get() == '':
        messagebox.showerror('Enter an amount')

    elif entry.get() <= 3000:
        messagebox.showinfo('Congratulations! You qualify to go to Malaysia')

    else:
        messagebox.showerror('You do not qualify to go to Malaysia')


# Creating & positioning the check button with a background color
checkButton = Button(root, text='Check qualification', bg='#bc5cd6', command=check)
checkButton.place(relx=0.15, rely=0.5)

root.mainloop()
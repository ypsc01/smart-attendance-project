from tkinter import  *
import os
import sqlite3

root = Tk()
root.title("New Student Entry")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

ID = StringVar()
NAME = StringVar()

def show():
    print(NAME.get())
    con = sqlite3.connect("project.db")
    con.execute("Insert into Users values (?,?)", (int(ID.get()),NAME.get()))
    con.commit()
    con.close()
    root.destroy()


# ==============================FRAMES=========================================
Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

# ==============================LABELS=========================================
lbl_title = Label(Top, text="Enter the Details", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_id = Label(Form, text="ID:", font=('arial', 14), bd=15)
lbl_id.grid(row=0, sticky="e")
lbl_name = Label(Form, text="Name:", font=('arial', 14), bd=15)
lbl_name.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

# ==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=ID, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=NAME, font=(14))
password.grid(row=1, column=1)

# ==============================BUTTON WIDGETS=================================
btn_submit = Button(Form, text="Submit", width=45,command = show)
btn_submit.grid(pady=25, row=3, columnspan=2)
#btn_login.bind('<Return>', Login)


root.mainloop()
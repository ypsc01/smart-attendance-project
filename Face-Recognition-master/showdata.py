import tkinter as tk
from tkinter.messagebox import showinfo
import sqlite3

LARGE_FONT = ("Verdana", 12)


class Myproj(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        F = Viewlib
        frame = F(container, self)


        self.frames[F] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Viewlib)

    def show_frame(self, cont):
        frame = self.frames[cont]

        frame.tkraise()



class Viewlib(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        db = sqlite3.connect("attendance.db")
        cur = db.cursor()
        cur.execute("SELECT * from Attendance")
        Libcontect_label = tk.Label(self, text="ID - Name -    Date     - Status ", font=LARGE_FONT)
        Libcontect_label.pack(pady=10, padx=10)
        for row in cur:
            Libcontect_label = tk.Label(self, text=str(row[0])+ "   "+str(row[1])+ "   "+str(row[2])+ "     "+ str(row[3] ), font=LARGE_FONT)
            Libcontect_label.pack(pady=10, padx=10)
        # return cur.fetchall()
        # cur.close()


app = Myproj()
app.title("Attendance")
app.mainloop()
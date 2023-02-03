
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from start import start
from tkinter import *
import webbrowser


class Gui:

    def __init__(self, master: tk):
        self.master: tk = master

        self.menu_close = None
        self.files = list()
        self.destination = ""
        self.fullscreenBoolean = False
        self.img_zug = None
        self.bg_zug = None
        self.img_logo = None
        self.bg_logo = None
        self.destination2 = ""

        # Hier werden die Buttons erstellt, womit man Die Dateien wählen kann einen speicherort wählen kann und das Programm starten kann
        self.bt_dateiWaehlen = ttk.Button(self.master, text="Datei wählen", command=self.getFiles)
        self.bt_speicheortWaehlen = ttk.Button(self.master, text="Speicherort wählen", command=self.getDestination)
        self.bt_start = ttk.Button(self.master, text="Programm Starten",
                                   command=self.start)

        self.bt_speicheortWaehlen2 = ttk.Button(self.master, text="Zweiten Speicherort wählen", command=self.getDestination2)

        self.GUILayout()

    def start(self):

        # es wird vor dem Starten überprüft, ob Dateien und Speicherort ausgewählt sind
        if self.files == "" or self.files is None:
            messagebox.showerror(title="Error!!", message="Bitte Dateien Auswählen!!")
            return

        if self.destination == "":
            messagebox.showerror(title="Error!!", message="Bitte einen Speicherort Auswählen")
            return

        start(self.files, self.destination, self.destination2)

    def buttons(self):

        self.bt_dateiWaehlen.place(anchor=CENTER, relx=.5, rely=.2)
        self.bt_speicheortWaehlen.place(anchor=CENTER, relx=.5, rely=.4)
        self.bt_speicheortWaehlen2.place(anchor=CENTER, relx=.5, rely=.6)
        self.bt_start.place(anchor=CENTER, relx=.5, rely=.8)

    def GUILayout(self):
        # Hier wird der Header designt
        self.master.title("National Express Fplo Tool")
        self.master.iconbitmap("pic/national-express.ico")

        self.master.geometry("500x500")
        self.master.minsize(500, 500)

        # Hier wird der BG hinzugefügt
        self.master.config(background="#8ec9e9")

        self.img_zug = PhotoImage(file="pic/zuege_freigestellt.png")
        self.bg_zug = Label(self.master, image=self.img_zug, background='#8ec9e9', anchor="sw")
        # self.bg_zug.place(relx=.0, rely=1.0, anchor="sw")

        self.img_logo = PhotoImage(file="pic/Logo.png")
        self.bg_logo = Label(self.master, image=self.img_logo, background='#8ec9e9', anchor='se')
        self.bg_logo.place(rely=1, relx=1, anchor='se')

        self.lb_Git_Hub = ttk.Label(self.master, text="Drücke hier um die das Projekt einzusehen", background="#8ec9e9", foreground="#0056a4")
        self.lb_Git_Hub.place(relx=1, rely=0, anchor="ne")
        self.lb_Git_Hub.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/ErenAK21/Fplo"))

        self.Menu()
        self.buttons()

    def getFiles(self):
        self.files = filedialog.askopenfilenames(
            title="Bitte wählen sie die PDF Dateien aus die sie kopieren und umbenennen.",
            filetypes=[("PDF-Dateien", "*.pdf"), ("Alle Dateien", "*.*")])

    def getDestination(self):
        self.destination = filedialog.askdirectory(
            title="Bitte wählen sie den Ordner aus in dem die PDF Dateien gespeichert werden sollen.")

    def getDestination2(self):
        self.destination2 = filedialog.askdirectory(
            title="Bitte wählen sie den Ordner aus in dem die PDF Dateien gespeichert werden sollen.")

    def Menu(self):
        # im unteren Teil wird das Menü Designet
        self.menubar = tk.Menu(self.master)

        self.menu_close = tk.Menu(self.menubar)
        self.menu_close.add_command()

        self.menubar = tk.Menu(self.master)

        self.menu_Programm = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_Programm, label="Programm")

        self.menu_close = tk.Menu(self.menu_Programm)
        self.menu_Programm.add_cascade(label="Programm schließen", command=self.programmSchliessen)

        self.menu_help = tk.Menu(self.menubar)

        self.menubar.add_cascade(label="Hilfe", command=help_window)

        self.master.config(menu=self.menubar)

    def programmSchliessen(self):
        self.master.destroy()


def help_window():
    messagebox.showinfo(title="Hilfe", message="""Bei Problemen melden sie sich bei der folgende e-mail
e-mail: eren.aksu@nationalexpress.de""")

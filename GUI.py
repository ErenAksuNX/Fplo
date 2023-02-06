import tkinter.messagebox as messagebox
from start import start
from tkinter import *
import webbrowser
from setting_window import *


class Gui:

    def __init__(self, master: tk):

        self.master: tk = master
        self.files = list()
        self.destination = ""
        self.fullscreenBoolean = False
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

        self.img_logo = PhotoImage(file="pic/Logo.png")
        self.bg_logo = Label(self.master, image=self.img_logo, background='#8ec9e9', anchor='se')
        self.bg_logo.place(rely=1, relx=1, anchor='se')

        lb_Git_Hub = ttk.Label(self.master, text="Drücke hier um das Projekt einzusehen", background="#8ec9e9", foreground="#0056a4")
        lb_Git_Hub.place(relx=1, rely=0, anchor="ne")
        lb_Git_Hub.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/ErenAksuNX/Fplo"))

        self.Menu()
        self.buttons()

    def getFiles(self):
        self.files = filedialog.askopenfilenames(
            title="Bitte wählen sie die PDF Dateien aus die sie kopieren und umbenennen.",
            filetypes=[("PDF-Dateien", "*.pdf"), ("Alle Dateien", "*.*")], initialdir=get_default_input())

    def getDestination(self):
        self.destination = filedialog.askdirectory(
            title="Bitte wählen sie den Ordner aus in dem die PDF Dateien gespeichert werden sollen.", initialdir=get_default_output0())

    def getDestination2(self):
        self.destination2 = filedialog.askdirectory(
            title="Bitte wählen sie den Ordner aus in dem die PDF Dateien gespeichert werden sollen.", initialdir=get_default_output1())

    def Menu(self):
        # im unteren Teil wird das Menü Designet
        menubar = tk.Menu(self.master)

        menu_close = tk.Menu(menubar)
        menu_close.add_command()

        menubar = tk.Menu(self.master)

        menu_Programm = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_Programm, label="Programm")

        menu_Programm.add_cascade(label="Programm schließen", command=self.programmSchliessen)

        menu_Programm.add_cascade(label="Einstellungen", command=self.einstellungen)

        menubar.add_cascade(label="Hilfe", command=help_window)

        self.master.config(menu=menubar)

    def programmSchliessen(self):
        self.master.destroy()

    def einstellungen(self):
        self.master.iconify()
        Setting_Window(self.master)


def help_window():
    messagebox.showinfo(title="Hilfe", message="""Bei Problemen melden sie sich bei der folgende e-mail
e-mail: eren.aksu@nationalexpress.de""")

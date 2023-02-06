import tkinter as tk
import tkinter.ttk as ttk
from Settings import get_default_input, get_default_output0, get_default_output1, wirte_default_settings
import tkinter.filedialog as filedialog


class Setting_Window:
    def __init__(self, mother):
        self.master = tk.Tk()

        self.master.title("Einstellungen")
        self.master.iconbitmap("pic/national-express.ico")
        self.master.config(background="#8ec9e9")
        self.mother = mother
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        self.master.resizable(width=False, height=False)

        lb_standard_eingabe = ttk.Label(master=self.master, text="Standard Eingabepfad:", background="#8ec9e9",
                                        foreground="#0056a4")
        lb_standard_ausgabe1 = ttk.Label(master=self.master, text="Standard erster Outputpfad:",
                                         background="#8ec9e9", foreground="#0056a4")
        lb_standard_ausgabe2 = tk.Label(master=self.master, text="Standard zweiter Outputpfad:",
                                        background="#8ec9e9", foreground="#0056a4")

        self.en_standard_eingabe = ttk.Entry(master=self.master, width=50)
        self.en_standard_ausgabe1 = ttk.Entry(master=self.master, width=50)
        self.en_standard_ausgabe2 = ttk.Entry(master=self.master, width=50)

        bt_standard_eingabe = ttk.Button(self.master, text="Ort Wählen", command=self.eingabe_auswaehlen)
        bt_standard_ausgabe1 = ttk.Button(self.master, text="Ort Wählen", command=self.ausgabe1_auswaehlen)
        bt_standard_ausgabe2 = ttk.Button(self.master, text="Ort Wählen", command=self.ausgabe2_auswaehlen)
        bt_save = ttk.Button(master=self.master, text="Speichern", command=self.save)
        bt_close = ttk.Button(master=self.master, text="Schliessen", command=self.close)

        self.en_standard_eingabe.insert(0, get_default_input())
        self.en_standard_ausgabe1.insert(0, get_default_output0())
        self.en_standard_ausgabe2.insert(0, get_default_output1())

        lb_standard_eingabe.grid(pady=5, padx=5, row=0, column=0, sticky="W")
        lb_standard_ausgabe1.grid(pady=5, padx=5, row=1, column=0, sticky="W")
        lb_standard_ausgabe2.grid(pady=5, padx=5, row=2, column=0, sticky="W")

        self.en_standard_eingabe.grid(pady=5, padx=5, row=0, column=1, sticky="E")
        self.en_standard_ausgabe1.grid(pady=5, padx=5, row=1, column=1, sticky="E")
        self.en_standard_ausgabe2.grid(pady=5, padx=5, row=2, column=1, sticky="E")

        bt_standard_eingabe.grid(padx=5, pady=5, row=0, column=2)
        bt_standard_ausgabe1.grid(padx=5, pady=5, row=1, column=2)
        bt_standard_ausgabe2.grid(padx=5, pady=5, row=2, column=2)

        ttk.Label(self.master, text=" ", background="#8ec9e9").grid(pady=5, padx=5, row=3, column=5)

        bt_close.grid(padx=5, pady=5, row=4, column=0, sticky="W")
        bt_save.grid(pady=5, padx=5, row=4, column=2, sticky="E")

        self.master.mainloop()

    def eingabe_auswaehlen(self):
        path = filedialog.askdirectory()
        self.en_standard_eingabe.delete(0, tk.END)
        self.en_standard_eingabe.insert(0, path)

    def ausgabe1_auswaehlen(self):
        path = filedialog.askdirectory()
        self.en_standard_ausgabe1.delete(0, tk.END)
        self.en_standard_ausgabe1.insert(0, path)

    def ausgabe2_auswaehlen(self):
        path = filedialog.askdirectory()
        self.en_standard_ausgabe2.delete(0, tk.END)
        self.en_standard_ausgabe2.insert(0, path)

    def close(self):
        self.master.destroy()
        self.mother.deiconify()

    def save(self):
        wirte_default_settings(default_input=self.en_standard_eingabe.get(),
                               default_output0=self.en_standard_ausgabe1.get(),
                               default_output1=self.en_standard_ausgabe2.get())
        self.close()

import json
import tkinter
import tkinter.messagebox


def get_default_input():
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            return settings["default_input"]
    except FileNotFoundError:
        tkinter.messagebox.showerror("Fatal Error!",
                                     "Die Datei settings.json wurde nicht gefunden das Programm wird beendet")
        exit()


def get_default_output0():
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            return settings["default_output0"]
    except FileNotFoundError:
        tkinter.messagebox.showerror("Fatal Error!",
                                     "Die Datei settings.json wurde nicht gefunden das Programm wird beendet")
        exit()


def get_default_output1():
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            return settings["default_output1"]
    except FileNotFoundError:
        tkinter.messagebox.showerror("Fatal Error!",
                                     "Die Datei settings.json wurde nicht gefunden das Programm wird beendet")
        exit()


def wirte_default_settings(default_input, default_output0, default_output1):
    file = {
        "default_input": default_input,
        "default_output0": default_output0,
        "default_output1": default_output1,
    }
    try:
        with open("settings.json", "w") as f:
            json.dump(file, f, indent=4)
    except FileNotFoundError:
        tkinter.messagebox.showerror("Fatal Error!",
                                     "Die Datei settings.json wurde nicht gefunden das Programm wird beendet")
        exit()

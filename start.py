import fitz
import re
import shutil
import datetime
import os
import tkinter.messagebox


# Diese Funktion gibt einen String zurück wo die Nullen für DateTime Elemente hinzugefügt werden
def nullstring(dateTime):
    if dateTime is not None and dateTime == 0:
        return "00"
    elif dateTime is not None and dateTime < 10:
        return "0" + str(dateTime)
    elif dateTime is not None:
        return str(dateTime)


# Die get_text Funktion gibt die erste seite der PDF-Datei als String zurück
def get_text(file):
    with fitz.Document(file) as doc:
        text = doc[0].get_text()
        return text


# Die get_daum_von Funktion gibt das bis Datum zurück
def get_datum_vom(text):
    match = re.search("gültig vom [0-9]{2}.[0-9]{2}.[0-9]{4} bis ([0-9]{2}.[0-9]{2}.[0-9]{4})", text)
    if match:
        return match.group(1)
    else:
        return ""


# Die get_datum_am Funktion funktioniert wie die get_datum_vom Funktion nur mit einer anderen suche
def get_datum_am(text):
    match = re.search("Gültig am ([0-9]{2}.[0-9]{2}.[0-9]{4})", text)
    if match:
        return match.group(1)
    else:
        return ""


def copyAndRename(file, destination, date):
    date = datetime.datetime.strptime(date, "%d.%m.%Y")  # Hier wird das Datum im Datetime format gespeichert

    srcfilename = os.path.basename(file)  # Hier wird von der Ausgewählten datei der Dateien Name rausgefiltert
    filename = f"/{date.year}{nullstring(date.month)}{nullstring(date.day)}_{srcfilename}"

    shutil.copyfile(file, destination + filename)  # In dieser Zeile wird die Datei kopiert und dabei umbenannt


def start(files: list, destination: str):
    datum = ""

    # In dieser Schleife wird jede Datei, die ausgewählt ist bearbeitet
    for file in files:

        text = get_text(file)

        # Hier wird überprüft, ob es sich um eine Eintagsfliege handelt
        if "gültig vom" in text:
            datum = get_datum_vom(text)
        elif "gültig ab" in text:
            datum = get_datum_am(text)

        # Wenn kein Datum gefunden wurde, dann wird das Dokument ohne datum gespeichert
        if datum != "":
            try:
                copyAndRename(file, destination, datum)
            except PermissionError:
                tkinter.messagebox.showerror(title="Error", message=f"Der zugriff auf die Datei {os.path.basename(file)} wurde verweigert, dies kann daran Liegen das die Datei offen ist! \n Diese Datei wurde deswegen übersprungen!")
        else:
            try:
                shutil.copyfile(file, f"{destination}/_{os.path.basename(file)}")
            except PermissionError:
                tkinter.messagebox.showerror(title="Error", message=f"Der zugriff auf die Datei {os.path.basename(file)} wurde verweigert, dies kann daran Liegen das die Datei offen ist! \n Diese Datei wurde deswegen übersprungen!")

        tkinter.messagebox.showinfo("Fertig", f"Das Programm ist durchgelaufen, die Dateien wurden in dem Verzeichnis {destination} gespeichert")

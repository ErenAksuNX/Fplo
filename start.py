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
    match = re.search("gültig vom [0-9]{2}.[0-9]{2}.[0-9]{4} bis [0-9]{2}.[0-9]{2}.[0-9]{4}", text)
    if match:
        return match.group(1)
    else:
        return ""

def extract_dates(text):
    # Suchmuster für das Datumsmuster
    pattern = r"gültig vom (\d{2})\.(\d{2})\.(\d{4}) bis (\d{2})\.(\d{2})\.(\d{4})"

    # Extrahieren der Datumsangaben
    match = re.search(pattern, text)
    if match:
        start_date = datetime.datetime.strptime(match.group(1) + match.group(2) + match.group(3), "%d%m%Y").date()
        end_date = datetime.datetime.strptime(match.group(4) + match.group(5) + match.group(6), "%d%m%Y").date()
        return [start_date, end_date]
    else:
        return None


# Die get_datum_am Funktion funktioniert wie die get_datum_vom Funktion nur mit einer anderen suche
def get_datum_am(text):
    match = re.search("Gültig am ([0-9]{2}.[0-9]{2}.[0-9]{4})", text)
    if match:
        return match.group(1)
    else:
        return ""


def copyAndRename(file, destination, date):
    srcfilename = os.path.basename(file)  # Hier wird von der Ausgewählten datei der Dateien Name rausgefiltert
    datum = datetime.datetime.strptime(date, "%d.%m.%Y")  # Hier wird das Datum im Datetime format gespeichert

    if date is list:
        filename = f"/{date[0].year}-{nullstring(date[0].month)}-{nullstring(date[0].day)}_{date[1].year}-{nullstring(date[1].month)}-{nullstring(date[1].day)}_{srcfilename}"
    else:
        filename = f"/{datum.year}-{nullstring(datum.month)}-{nullstring(datum.day)}_{srcfilename}"







    shutil.copyfile(file, destination + filename)  # In dieser Zeile wird die Datei kopiert und dabei umbenannt


def start(files: list, destination: str, destination2: str):
    datum = ""

    # In dieser Schleife wird jede Datei, die ausgewählt ist bearbeitet
    for file in files:

        text = get_text(file)

        # Hier wird überprüft, ob es sich um eine Eintagsfliege handelt
        if "gültig vom" in text:
            datum = extract_dates(text)

            #datum = get_datum_vom(text)
        elif "gültig ab" in text:
            datum = get_datum_am(text)

        # Wenn kein Datum gefunden wurde, dann wird das Dokument ohne datum gespeichert
        elif datum != "" and datum is not None:
            try:
                copyAndRename(file, destination, datum)
                if destination2 != "":
                    copyAndRename(file, destination2, datum)
            except PermissionError:
                tkinter.messagebox.showerror(title="Error", message=f"Der zugriff auf die Datei {os.path.basename(file)} wurde verweigert, dies kann daran Liegen das die Datei offen ist! \n Diese Datei wurde deswegen übersprungen!")
        else:
            try:
                shutil.copyfile(file, f"{destination}/_{os.path.basename(file)}")
                if destination2 != "":
                    shutil.copyfile(file, f"{destination2}/_{os.path.basename(file)}")
            except PermissionError:
                tkinter.messagebox.showerror(title="Error", message=f"Der zugriff auf die Datei {os.path.basename(file)} wurde verweigert, dies kann daran Liegen das die Datei offen ist! \n Diese Datei wurde deswegen übersprungen!")

    if destination2 != "":
        tkinter.messagebox.showinfo("Fertig", f"Das Programm ist durchgelaufen, die Dateien wurden in dem Verzeichnis:\n{destination}\ngespeichert")
    else:
        tkinter.messagebox.showinfo("Fertig", f"Das Programm ist durchgelaufen, die Dateien wurden in dem Verzeichnis:\n{destination} \nund:\n{destination2}\ngespeichert")

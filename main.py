import os
import csv
from kivy.app import App
from kivy.uix.label import Label

def get_csv_path():
    # Busca el csv donde esté, PC o Android
    possible = [
        os.path.join(os.path.dirname(__file__), "data.csv"),
        "data.csv",
        "/storage/emulated/0/data.csv"
    ]
    for p in possible:
        if os.path.exists(p):
            return p
    return "data.csv"

class OddslotApp(App):
    def build(self):
        path = get_csv_path()
        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = list(csv.reader(f))
                rows = len(reader) - 1
                return Label(text=f"Oddslot PRO\nCSV cargado: {rows} filas\nRuta: {path}")
        except Exception as e:
            return Label(text=f"Error cargando CSV:\n{e}\nRuta probada: {path}")

OddslotApp().run()

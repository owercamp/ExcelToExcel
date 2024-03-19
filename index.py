import pandas as pd
import tkinter as tk
from Models.config import config_ids
import Models.workers_dictionary as Workers

from tkinter import filedialog


def openFile():
    myWindows = tk.Tk()
    myWindows.withdraw()

    route_path = filedialog.askopenfilename()
    myWindows.destroy()

    return route_path


print("Selecione el archivo de excel con los datos a importar.")
origin = openFile()
print(f"El documento seleccionado es: {origin}")
print("Selecione el archivo de excel a donde se va a importar los datos.")
destiny = openFile()
print(f"El documento seleccionado es: {destiny}")

origin_book = pd.ExcelFile(origin)
destiny_book = pd.ExcelFile(destiny)

sheets_book_origin = origin_book.sheet_names
sheets_book_destiny = destiny_book.sheet_names

# asignaciones de los ids correspondientes
ids = config_ids()
information = pd.DataFrame(pd.read_excel(destiny, sheet_name="RUTAS", header=2, usecols="E:F")).values
ids.assigned(information)

# creaciones de los modelos para cada hoja
model_origin = Workers.worker()
for sheet in sheets_book_origin:
    if sheet == "EMO":
        data_origin = pd.DataFrame(pd.read_excel(origin, sheet_name=sheet))
        for item in data_origin.columns:
            model_origin.info(item, data_origin.columns.get_loc(item))


model_destiny = Workers.worker()
for sheet in sheets_book_destiny:
    if sheet == "TRABAJADORES":
        data_destiny = pd.DataFrame(pd.read_excel(destiny, sheet_name=sheet, header=3))
        for item in data_destiny.columns:
            model_destiny.info(item, data_destiny.columns.get_loc(item))


# print("Modelo de origen:")
# print(f"CONTRATO ORIGEN: {model_origin.dict_worker['NOMBRE CONTRATO']}")
# print(model_origin.dict_worker)
# print("")
# print("Modelo de destino:")
# print(f"CONTRATO DESTINO: {model_destiny.dict_worker['NOMBRE CONTRATO']}")
# print(model_destiny.dict_worker)
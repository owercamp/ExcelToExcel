import pandas as pd
import tkinter as tk
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

sheets_book = origin_book.sheet_names

for sheet in sheets_book:
    if sheet == "EMO":
        data = pd.DataFrame(pd.read_excel(origin, sheet_name=sheet))
        for item in data.columns:
            if item in Workers.worker.keys():
                Workers.info(item, data.columns.get_loc(item))


myDictionary = Workers.worker

print(myDictionary)

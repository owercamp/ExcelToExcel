from collections import OrderedDict

worker = OrderedDict({
    "ESTADO": "8",
    "NOMBRE CONTRATO": "",
    "DESTINO": "",
    "CIUDAD": "",
    "INGRESO": "",
    "TIPO EXAMEN": "",
    "FECHA INGRESO": "",
    "PACIENTE": "",
    "NRO IDENTIFICACION": "",
    
})

def info(data, index):
    if data == "NOMBRE CONTRATO":
        worker["NOMBRE CONTRATO"] = index
    elif data == "DESTINO":
        worker["DESTINO"] = index
    else:
        pass
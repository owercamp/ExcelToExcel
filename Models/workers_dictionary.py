from collections import OrderedDict


class worker:

    def __init__(self):
        self.dict_worker = OrderedDict({
            "ESTADO": "",
            "NOMBRE CONTRATO": "",
            "DESTINO": "",
            "CIUDAD": "",
            "INGRESO": "",
            "TIPO EXAMEN": "",
            "FECHA INGRESO": "",
            "PACIENTE": "",
            "NRO IDENTIFICACION": "",
            "EDAD": "",
            "ESTRATO": "",
            "GENERO": "",
            "NRO HIJOS": "",
            "RAZA": "",
            "ESTADO CIVIL": "",
            "ESCOLARIDAD": "",
            "CARGO USUARIO": "",
            "LAB DURACION EN AÑOS": "",
            "FUENTE": "",
            "TIPO ACTIVIDAD": "",
            "idOrdenListaTrabajadores": "",
            "idOrden": "",
        })

    def info(self, data, index):
        if data == "ESTADO" or data == "estado":
            self.dict_worker["ESTADO"] = index
        if data == "NOMBRE CONTRATO":
            self.dict_worker["NOMBRE CONTRATO"] = index
        elif data == "DESTINO":
            self.dict_worker["DESTINO"] = index
        elif data == "CIUDAD":
            self.dict_worker["CIUDAD"] = index
        elif data == "INGRESO":
            self.dict_worker["INGRESO"] = index
        elif data == "TIPO EXAMEN":
            self.dict_worker["TIPO EXAMEN"] = index
        elif data == "FECHA INGRESO":
            self.dict_worker["FECHA INGRESO"] = index
        elif data == "PACIENTE":
            self.dict_worker["PACIENTE"] = index
        elif data == "NRO IDENTIFICACION" or data == "NRO IDENFICACION":
            self.dict_worker["NRO IDENTIFICACION"] = index
        elif data == "EDAD":
            self.dict_worker["EDAD"] = index
        elif data == "ESTRATO":
            self.dict_worker["ESTRATO"] = index
        elif data == "GENERO":
            self.dict_worker["GENERO"] = index
        elif data == "NRO HIJOS":
            self.dict_worker["NRO HIJOS"] = index
        elif data == "RAZA":
            self.dict_worker["RAZA"] = index
        elif data == "ESTADO CIVIL":
            self.dict_worker["ESTADO CIVIL"] = index
        elif data == "ESCOLARIDAD":
            self.dict_worker["ESCOLARIDAD"] = index
        elif data == "CARGO USUARIO" or data == "CARGO":
            self.dict_worker["CARGO USUARIO"] = index
        elif data == "LAB DURACION EN AÑOS":
            self.dict_worker["LAB DURACION EN AÑOS"] = index
        elif data == "FUENTE":
            self.dict_worker["FUENTE"] = index
        elif data == "TIPO ACTIVIDAD":
            self.dict_worker["TIPO ACTIVIDAD"] = index
        elif data == "idOrdenListaTrabajadores":
            self.dict_worker["idOrdenListaTrabajadores"] = index
        elif data == "idOrden":
            self.dict_worker["idOrden"] = index

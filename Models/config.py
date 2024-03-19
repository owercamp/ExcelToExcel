from collections import OrderedDict

class config_ids():
    
    def __init__(self):
        self.ids = OrderedDict({
            "idOrdenListaTrabajadores": "",
            "idEmo": "",
            "idAudiometria": "",
            "idOptometria": "",
            "idVisiometria": "",
            "idEspirometria": "",
            "idOsteomuscular": "",
            "idComplementarios": "",
            "idPsicotecnica": "",
            "idPsicosensomentrica": ""
        })

    def assigned(self, data):
        for item in data:
            for key in self.ids.keys():
                if item[0] == key:
                    self.ids[key] = item[1] + 1
            
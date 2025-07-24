import requests
from os import path
from pywspix.headers import Headers


class WSPixConsultar:
    def __init__(self, headers: Headers, url: str):
        self.__headers = Headers
        self.__url = url

    def get_headers(self):
        return self.__headers
    
    def get_consulta_url(self, idfpix: str):
        url = path.join(self.__url, idfpix)
        return url
    
    def get_verifica_url(self, idfpix: str):
        verifica_param = "?verificar=true"
        url = path.join(self.__url, idfpix, verifica_param)
        return url
    
    def consultar(self, idfpix: str, verificar=False):
        headers = self.get_headers()
        if verificar:
            url = self.get_verificar_url(idfpix)
        else:
            url = self.get_consulta_url(idfpix)
        resp = requests.get(url=url, headers=headers)
        return resp

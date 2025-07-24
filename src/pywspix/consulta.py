import requests
from os import path
from pywspix.headers import Headers


class WSPixConsulta:
    def __init__(self, headers: Headers, url: str):
        self.__headers = Headers
        self.__url = url

    def get_headers(self):
        return self.__headers.generate()
    
    def get_consulta_url(self, idfpix: str):
        url = path.join(self.__url, idfpix)
        return url
    
    def get_verificar_parameters(self):
        return {"verificar": "true"}
    
    def consultar(self, idfpix: str):
        headers = self.get_headers()
        url = self.get_consulta_url(idfpix)
        resp = requests.get(url=url, headers=headers)
        return resp.json()
    
    def verificar(self, idfpix: str):
        url = self.get_consulta_url(idfpix)
        headers = self.get_headers()
        parameters = self.get_verifica_parameters()
        resp = requests.get(url=url, headers=headers, params=parameters)
        return resp.json()        

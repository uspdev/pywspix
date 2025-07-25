import requests
from urllib.parse import urljoin
from pywspix.headers import Headers


class WSPixConsulta:
    def __init__(self, headers: Headers, url: str):
        self.__headers = Headers
        self.__url = url
        self.__uri = "/wspix/api/pix/"

    def get_headers(self):
        return self.__headers.generate()
    
    def get_consulta_url(self, idfpix: str):
        uri = f"{self.__uri}{idfpix}"
        url = urljoin(self.__url, uri)
        return url
    
    def get_verificar_parameters(self):
        return {"verificar": "true"}
    
    def consultar(self, idfpix: str):
        try:
            headers = self.get_headers()
            url = self.get_consulta_url(idfpix)
            resp = requests.get(url=url, headers=headers)
            return resp.json()
        except Exception as error:
            return error
    
    def verificar(self, idfpix: str):
        try:
            url = self.get_consulta_url(idfpix)
            headers = self.get_headers()
            parameters = self.get_verifica_parameters()
            resp = requests.get(url=url, headers=headers, params=parameters)
            return resp.json()
        except Exception as error:
            return error

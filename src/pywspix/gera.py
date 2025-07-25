import requests
from pywspix.headers import Headers
from pywspix.schemas import GerarPix


class WSPixGera:
    def __init__(self, headers: Headers, url: str):
        self.__payload = {}
        self.__headers = headers
        self.__url = url
        self.__idfpix = None

    def __validate_payload(self, **kwargs):
        validated = GerarPix(**kwargs)
        return validated
    
    def __get_headers(self):
        return self.__headers.generate()

    def __get_url(self):
        return self.__url

    def __set_idfpix(self, idfpix: str):
        self.__idfpix = idfpix

    def __get_idfpix(self):
        return self.__idfpix

    def __str__(self):
        return self.__get_idfpix

    def set_payload(self, **kwargs):
        self.__validate_payload(**kwargs)
        self.__payload = kwargs

    def get_payload(self):
        return self.__payload

    def gerar_pix(self):
        payload = self.__get_payload()
        headers = self.__get_headers()
        url = self.__get_url()
        resp = requests.post(url=url, json=payload, headers=headers)
        self.__set_idfpix(resp.json().get("idfpix"))
        return resp.json()
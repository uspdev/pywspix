import requests
from urllib.parse import urljoin
from pywspix.headers import Headers
from pywspix.schemas import GerarPix


class WSPixGera:
    def __init__(self, headers: Headers, url: str):
        self.__payload = {}
        self.__headers = headers
        self.__url = url
        self.__idfpix = None
        self.__gerar_uri = "/wspix/api/pix/gerar"

    def __validate_payload(self, **kwargs):
        validated = GerarPix(**kwargs)
        return validated
    
    def __get_headers(self):
        return self.__headers.generate()

    def __get_url(self):
        url = urljoin(self.__url, self.__gerar_uri)
        return url

    def __set_idfpix(self, pix_data: dict):
        idfpix = pix_data.get("idfpix")
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

    def request_gerar_pix(self):
        payload = self.get_payload()
        headers = self.__get_headers()
        url = self.__get_url()
        resp = requests.post(headers=headers, url=url, json=payload)
        return resp
    
    def gerar_pix(self):
        try:
            resp = self.request_gerar_pix()
            self.__set_idfpix(resp.json())
            return resp
        except Exception as error:
            return error
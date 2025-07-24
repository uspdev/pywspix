import requests
from urllib.parse import urljoin
from pydantic import BaseModel, model_validator
from datetime import datetime
from pywspix.headers import Headers


class SearchParams(BaseModel):
    dtaini: datetime
    dtafim: datetime
    docPesOrg: int = None
    nomsissvc: str = None

    @model_validator(mode='after')
    def validate_date(self):
        if self.dtafim <= self.dtaini:
            raise ValueError("dtaini deve ser menor do que dtafim")
        return self


class Lista:
    def __init__(self, baseurl: str, headers: Headers):
        self.__search_params = None
        self.__baseurl = baseurl
        self.__listar_url = "/pix/listarConcluidos"
        self.__headers = headers

    def get_listar_url(self):
        return self.__listar_url
    
    def get_base_url(self):
        return self.__baseurl

    def get_url(self):
        baseurl = self.get_base_url()
        listar_url = self.get_listar_url()
        return urljoin(baseurl, listar_url)
    
    def validate_params(self, **params):
        search_params = SearchParams(**params)
        return search_params.model_dump()

    def get_headers(self):
        return self.__headers.generate()

    def format_date(self, date: datetime):
        return date.strftime("%d/%m/%Y %H:%M:%S")

    def get_search_params(self):
        search_params = self.__search_params
        search_params["dtaini"] = self.format_date(search_params["dtaini"])
        search_params["dtafim"] = self.format_date(search_params["dtafim"])
        return search_params
    
    def set_search_params(self, **params):
        validated_params = self.validate_params(**params)
        self.__search_params = validated_params

    def listar(self):
        params = self.get_search_params()
        headers = self.get_headers()
        url = self.get_url()
        resp = requests.get(url=url, headers=headers, params=params)
        return resp



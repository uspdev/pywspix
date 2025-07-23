import requests
from typing import Literal
from validate_docbr import CPF, CNPJ
from pydantic import BaseModel, EmailStr, field_validator


class GerarPix(BaseModel):
    tipoPessoa: Literal["PF", "PJ"]
    codPesOrg: int
    docPesOrg: int
    nomePesOrg: str
    valor: float
    infoCobranca: str
    emailPesOrg: EmailStr
    expiracao: int
    codigoFonteRecurso: int
    codigoUnidadeDespesa: int
    estruturaHierarquica: str

    @field_validator("docPesOrg")
    def doc_pes_org_validator(cls, value):
        cpf = CPF()
        cnpj = CNPJ()
        if not cpf.validate(str(value)) and not cnpj.validate(str(value)):
            raise ValueError("CPF ou CNPJ inválido.")
        return value


class WSPixGerar:
    def __init__(self, user: str, password: str, url: str):
        self.__payload = {}
        self.user = user
        self.password = password
        self.url = url

    def validate_payload(self, **kwargs):
        validated = GerarPix(**kwargs)
        return validated

    def set_payload(self, **kwargs):
        self.validate_payload(**kwargs)
        self.__payload = kwargs

    def get_payload(self):
        return self.__payload
    
    def get_headers(self):
        return {
            "X-Username": self.user,
            "X-Password": self.password
        }
    
    def gerar_pix(self):
        payload = self.get_payload()
        headers = self.get_headers()
        resp = requests.post(url=self.url, json=payload, headers=headers)
        return resp.content
from datetime import datetime
from typing import Literal
from validate_docbr import CPF, CNPJ
from pydantic import (
    BaseModel,
    HttpUrl,
    EmailStr,
    model_validator,
    field_validator
)


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


class WebhookConfig(BaseModel):
    url: HttpUrl
    token: str
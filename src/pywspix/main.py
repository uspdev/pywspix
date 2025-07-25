from pywspix.gera import WSPixGera
from pywspix.headers import Headers


def run():
    url = "https://api-dev.portalservicos.usp.br/wspix/api"
    user = "iag"
    password = "teste1"
    payload = {
        "tipoPessoa": "PF",
        "codPesOrg": 3544750,
        "valor": 10.02,
        "infoCobranca": "Cobrança teste",
        "expiracao": 3600,
        "codigoFonteRecurso": 423,
        "codigoUnidadeDespesa": 1,
        "estruturaHierarquica": r"\DISTRIBUIDOR"
    }

    headers = Headers(user=user, password=password)
    gera = WSPixGera(headers=headers, url=url)
    gera.set_payload(**payload)
    resp = gera.gerar_pix()
    print(resp)
    print(str(gera))

if __name__ == "__main__":
    run()
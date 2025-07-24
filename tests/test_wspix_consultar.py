from pywspix.headers import Headers
from pywspix.consultar import WSPixConsultar


def get_consultar_obj():
    headers = Headers(user="user", password="password")
    consulta = WSPixConsultar(headers=headers, url="https://api.test")
    return consulta


def test_get_consulta_url():
    consulta = get_consultar_obj()
    assert consulta.get_consulta_url("idfpix") == "https://api.test/idfpix"


def test_get_verificar_parameters():
    consulta = get_consultar_obj()
    assert consulta.get_verificar_parameters() == {"verificar": "true"}



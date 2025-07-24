import pytest
from pydantic import ValidationError
from datetime import datetime
from pywspix.lista import Lista
from pywspix.headers import Headers


params = {
    "dtaini": datetime(2025, 7, 12, 10, 10),
    "dtafim": datetime(2025, 7, 30, 10, 10),
    "docPesOrg": 83912022089,
    "nomsissvc": "system name",
}


URL = "https://test.pix.api"


def create_lista():
    headers = Headers(user="user1", password="pass")
    lista = Lista(baseurl=URL, headers=headers)
    lista.set_search_params(**params)
    return lista


def test_set_search_params():
    lista = create_lista()
    assert lista.get_search_params() == params


def test_date_validation():
    with pytest.raises(ValidationError):
        p = params.copy()
        p["dtafim"] = datetime(2025, 6, 12, 10, 10)
        lista = create_lista()
        lista.set_search_params(**p)


def test_get_url():
    lista = create_lista()
    url = lista.get_url()
    print(url)
    assert url == "https://test.pix.api/pix/listarConcluidos"
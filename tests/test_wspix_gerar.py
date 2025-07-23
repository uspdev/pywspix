import pytest
from pydantic import ValidationError
from pywspix.gerar import WSPixGerar


payload = {
    "tipoPessoa": "PF",
    "codPesOrg": 3544750,
    "docPesOrg": 31686822090,
    "nomePesOrg": "Pessoa da Silva",
    "valor": 10.02,
    "infoCobranca": "Cobrança teste",
    "emailPesOrg": "test@test.com",
    "expiracao": 3600,
    "codigoFonteRecurso": 423,
    "codigoUnidadeDespesa": 1,
    "estruturaHierarquica": r"\DISTRIBUIDOR"
}

def assert_payload_validation(payload, key, value):
    with pytest.raises(ValidationError):
        wspixgerar = WSPixGerar(user="user", password="pass")
        data = payload.copy()
        data[key] = value
        wspixgerar.set_payload(**data)

def test_set_payload():
    wspixgerar = WSPixGerar(user="user", password="pass")
    wspixgerar.set_payload(**payload)
    assert wspixgerar.get_payload() == payload


def test_validate_tipo_pessoa_payload():
    assert_payload_validation(payload, "tipoPessoa", "DM")


def test_validate_codpesorg():
    assert_payload_validation(payload, "codPesOrg", "no_valid_value")


def test_validate_nomepesorg():
    assert_payload_validation(payload, "nomePesOrg", 1234)


def test_validate_valor():
    assert_payload_validation(payload, "valor", "no_valid_value")


def test_validate_infocobranca():
    assert_payload_validation(payload, "infoCobranca", 12345)


def test_validate_emailpesorg():
    assert_payload_validation(payload, "emailPesOrg", "@test.com")


def test_validate_espiracao():
    assert_payload_validation(payload, "expiracao", "no_valid_value")


def test_validate_codigofonterecurso():
    assert_payload_validation(payload, "codigoFonteRecurso", "no_valid_data")


def test_validate_codigounidadedespesa():
    assert_payload_validation(payload, "codigoUnidadeDespesa", "no_valid_data")


def test_validate_estruturahierarquica():
    assert_payload_validation(payload, "estruturaHierarquica", 12345)

def test_get_headers():
    wspixgerar = WSPixGerar(user="user", password="pass")
    headers = wspixgerar.get_headers()
    assert headers == {"X-Username": "user", "X-Password": "pass"}
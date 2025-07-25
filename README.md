# 📦 PyWSPix

> O PyWSPix oferece um wrapper para as funcionalidades do WSPix da USP.
> 
> ![Python](https://img.shields.io/badge/python-3.8%2B-blue)
> ![Poetry](https://img.shields.io/badge/poetry-managed-blueviolet)

---

## 🚀 Funcionalidades

- ✅ Gera um novo Pix.
- ✅ Consulta um Pix gerado.
- ✅ Lista os Pix pagos dentre de um príodo.
- ✅ Retorna a representação binária para um PFD contentdo os dados e o QrCode de um Pix gerado.
- ✅ Retorna a representação binária para uma imagem contentdo o QrCode de um Pix gerado.
- ✅ Configura o webhook da aplicação

---

## 📦 Instalação

```bash
pip install pywspix
```

### Requisitos

- Python >= 3.8

## Exemplos

### Gerar um Pix

```bash
from pywspix.gera import WSPixGera
from pywspix.headers import Headers

url = "https://api-dev.portalservicos.usp.br"
user = "usuario_do_servico"
password = "senha_do_servico"

payload = {
    "tipoPessoa": "PF",
    "codPesOrg": 3333333,
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
``` 

### Consultar um Pix
```bash
from pywspix.consulta import WSPixConsulta
from pywspix.headers import Headers

url = "https://api-dev.portalservicos.usp.br"
user = "usuario_do_servico"
password = "senha_do_servico"
headers = Headers(user=user, password=password)

consulta = WSPixConsulta(headers=headers, url=url)
resp = consulta.consultar("kjhasd98a9s8d7khd")
``` 
### Listar Concluídos
```bash
from pywspix.consulta import WSPixConsulta
from pywspix.headers import Headers

url = "https://api-dev.portalservicos.usp.br"
user = "usuario_do_servico"
password = "senha_do_servico"
headers = Headers(user=user, password=password)

search = {
    "dtaini": "2025-01-01 10:10:00",
    "dtaini": "2025-02-01 10:10:00"
}

lista = WSPixLista(headers=headers, url=url)
lista.set_search_params(**busca)
resp = lista.listar()
``` 

### Gerar QRcode ou PDF
```bash
from pywspix.file import WSPixFile
from pywspix.headers import Headers

url = "https://api-dev.portalservicos.usp.br"
user = "usuario_do_servico"
password = "senha_do_servico"
headers = Headers(user=user, password=password)

file = WSPixFile(headers=headers, url=url, idfpix="lkjasdpasopid")
qrcode = file.get_qrcode()
pdf = file.get_pdf()
``` 

### Configuração do Webhook
```bash
from pywspix.file import WSPixFile
from pywspix.headers import Headers

url = "https://api-dev.portalservicos.usp.br"
user = "usuario_do_servico"
password = "senha_do_servico"
headers = Headers(user=user, password=password)

config = {
    "url": "https://my.app.br/webhook",
    "token": "kljoiasuy0987hjkas"
}

webhook = WSPixwebhook(headers=headers, baseurl=url)
webhook.set_config(**config)
webhook.config()
``` 

## Contribuição

### Clone o repositório:

```bash
git clone https://github.com/iagsti/pywspix.git
```

### Instale as dependências:

```bash
cd pywspix
poetry install
```

### Testando:

```bash
poetry run pytest
```

### Para fazer o build do pacote

```bash
poetry build
```


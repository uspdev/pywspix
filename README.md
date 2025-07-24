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


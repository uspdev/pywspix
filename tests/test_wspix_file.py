from pywspix.file import File
from pywspix.headers import Headers


def create_file():
    headers = Headers(user="user1", password="pass")
    baseurl = "https://test.pix.api"
    file = File(baseurl=baseurl, headers=headers, idfpix="kjashd")
    return file


def test_get_pdf_url():
    file = create_file()
    url = file.get_pdf_url()
    assert url == "https://test.pix.api/pix/kjashd/pdf"


def test_get_qrcode_url():
    file = create_file()
    url = file.get_qrcode_url()
    assert url == "https://test.pix.api/pix/kjashd/qrcode"
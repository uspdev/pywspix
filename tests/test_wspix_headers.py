from pywspix.headers import Headers


def test_get_headers():
    headers = Headers(user="user1", password="testpassword")
    headers_content = headers.generate()
    assert headers_content == {"X-Username": "user1", "X-Password": "testpassword"}
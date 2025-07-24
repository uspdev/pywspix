import pytest
from pydantic import ValidationError
from pywspix.webhook import Webhook
from pywspix.headers import Headers


URL = "https://test.pix.api"


WEBHOOK_CONFIG = {
    "url": "https://app.payment.com/confirmation",
    "token": "964e7c47feeac9c4eb7450b8c8ff53e4196ee70d68910d27ccecbc777c5ab226"
}


def create_webhook():
    headers = Headers(user="user1", password="pass")
    webhook = Webhook(baseurl=URL, headers=headers)
    return webhook


def test_get_url():
    webhook = create_webhook()
    url = webhook.get_url()
    assert url == f"{URL}/pix/webhookConfig"


def test_set_config():
    webhook = create_webhook()
    config = WEBHOOK_CONFIG
    webhook.set_config(**config)
    assert webhook.get_config() == config


def test_config_validation():
    with pytest.raises(ValidationError):
        webhook = create_webhook()
        fail_config = WEBHOOK_CONFIG.copy()
        fail_config["url"] = "some.invalid.url"
        webhook.set_config(**fail_config)


def test_get_config_validation():
    with pytest.raises(ValueError):
        webhook = create_webhook()
        webhook.get_config()
import os
from typing import List
from requests import Response, post


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message


class Mailgun:

    FROM_TITLE = "Pricing Service"
    FROM_EMAIL = "do-not-reply@sandbox7d7fa713703040d1b06f6e7c09d70bbb.mailgun.org"

    @classmethod
    def send_mail(
        cls, email: List[str], subject: str, text: str, html: str = "<p></p>"
    ) -> Response:

        api_key = os.environ.get("MAILGUN_API_KEY", None)
        domain = os.environ.get("MAILGUN_DOMAIN", None)

        if api_key is None:
            raise MailgunException("Failed to load Mailgun API key.")
        if domain is None:
            raise MailgunException("Failed to load Mailgun domain")
        response = post(
            f"{domain}/messages",
            auth=("api", api_key),
            data={
                "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
                "html": html,
            },
        )
        if response.status_code != 200:
            print(response.json())
            raise MailgunException("An error ocurrer while sending e-mail.")
        return response


# Mailgun.send_mail(
#     email=["wesleyjr0101@gmail.com"],
#     subject="teste dnv bl",
#     text="Corpo do texto de teste",
# )

from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Lucas Farias",cpf="12345678901",
                    phone="71-991625771", email="lffsantos@gmail.com")
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):

        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['lffsantos@gmail.com', 'contato@eventex.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_cco(self):
        expect = ['contato@eventex.com.br']

        self.assertEqual(expect, self.email.bcc)


    def test_subscription_email_body(self):
        contents = ['Lucas Farias',
                    '12345678901',
                    '71-991625771',
                    'lffsantos@gmail.com']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
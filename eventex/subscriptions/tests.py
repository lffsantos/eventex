from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """ GET / inscrição / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')

    def test_html(self):
        """HTML must contains input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        form = self.resp.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'],list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name="Lucas Farias",cpf="12345678901",
                    phone="71-991625771", email="lffsantos@gmail.com")
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid Post should redirect to /inscricao/"""

        self.assertEqual(302, self.resp.status_code)

    def test_send_subscription_email(self):
        self.assertEqual(1,len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br','lffsantos@gmail.com']

        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Lucas Farias', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('71-991625771', email.body)
        self.assertIn('lffsantos@gmail.com', email.body)


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/',{})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class SubscribeSucessMsg(TestCase):
    def test_message(self):
        data = dict(name="Lucas Farias",cpf="12345678901",
                    phone="71-991625771", email="lffsantos@gmail.com")
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        form = SubscriptionForm()
        self.assertSequenceEqual(['name','cpf','email','phone'],list(form.fields))

    def test_cpf_is_digit(self):
        """cpf must only accept digits"""
        form = self.make_validated_form(cpf='ABCD12345678')

        code = 'digits'
        field = 'cpf'
        self.assertFormMessage(form,field,code)

    def test_cpf_has_11_digits(self):
        """Cpf must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        code = 'length'
        field = 'cpf'

        self.assertFormMessage(form,field,code)

    def test_name_must_be_capitalize(self):
        """Name must be capitalize"""
    #     LUCAS farias ,> Lucas farias
        form = self.make_validated_form(name='LUCAS farias')
        self.assertEqual('Lucas Farias', form.cleaned_data['name'])

    def assertFormMessage(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(name='lucas farias', email='lffsantos@gmail.com',
                    cpf='12345678901', phone='71-991625771')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

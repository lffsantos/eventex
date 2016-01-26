from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact
__author__ = 'lucas'


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Lucas farias',
            slug='lucas-farias',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):

        contact = Contact.objects.create( speaker=self.speaker, kind=Contact.EMAIL,
                                          value='lffsantos@gmail.com')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create( speaker=self.speaker, kind=Contact.PHONE,
                                          value='71-991625771')
        self.assertTrue(Contact.objects.exists())

    # def test_choices(self):
    #     """contact kind should be limit to E or P"""
    #     contact = Contact.objects.create(speaker=self.speaker, kind='A',
    #                                       value='B')
    #
    #     self.assertRaises(ValidationError, contact.full_clean())

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL,
                                          value='lffsantos@gmail.com')
        self.assertEqual('lffsantos@gmail.com', str(contact))
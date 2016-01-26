from django.test import TestCase
from eventex.core.models import Talk
__author__ = 'lucas'


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da palestra'
            )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_res_speakers(self):
        """talk has many speakers and vice-versa"""
        self.talk.speakers.create(name='Lucas Farias',
                                  slug='lucas-farias',
                                  website='http://www.lucasfarias.com.br')

        self.assertEqual(1, self.talk.speakers.count())

    def test_description_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_blank(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da palestra', str(self.talk))
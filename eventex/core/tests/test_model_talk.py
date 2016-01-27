from django.test import TestCase
from eventex.core.managers import PeriodManager
from eventex.core.models import Talk, Course
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


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(
            title='morning talk',
            start='11:59'
            )
        Talk.objects.create(
            title='afternoon talk',
            start='12:00'
            )

    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ['morning talk']
        self.assertQuerysetEqual(qs, expected, lambda o : o.title)

    def test_at_morning(self):
        qs = Talk.objects.at_afternoon()
        expected = ['afternoon talk']
        self.assertQuerysetEqual(qs, expected, lambda o : o.title)

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title='Título do Curso',
                                            start='09:00',
                                            description='Descrição do curso.',
                                            slots=20
                                            )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_speakers(self):
        """course has many speakers and vice-versa"""
        self.course.speakers.create(name='Lucas Farias',
                                    slug='lucas-farias',
                                    website='http://www.lucasfarias.com.br')

        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        self.assertEqual('Título do Curso', str(self.course))

    def test_manager(self):
        self.assertIsInstance(Course.objects, PeriodManager)
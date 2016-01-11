from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdmin(TestCase):
    def test_has_action(self):
        # """ Action mark_as_paid should be installed"""
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.assertIn('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        Subscription.objects.create(name='Lucas farias', cpf='12345678901',
                                    email='lffsantos@gmail.com', phone='71-991625771')

        query_set = Subscription.objects.all()

        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        model_admin.mark_as_paid(None, query_set)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
from unittest.mock import Mock
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Lucas farias', cpf='12345678901',
                                    email='lffsantos@gmail.com', phone='71-991625771')

        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)
    def test_has_action(self):
        # """ Action mark_as_paid should be installed"""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):

        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())


    def test_message(self):
        """It should a message to the user"""
        mock = self.call_action()
        mock.assert_called_with(None, '1 inscrição foi marcada como paga.')

        SubscriptionModelAdmin.message_user = mock.old_message_user

    def call_action(self):
        query_set = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, query_set)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock
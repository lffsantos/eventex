from django.core.mail.message import EmailMessage


class MailSender(EmailMessage):

    def send_email(self):
        self.send()

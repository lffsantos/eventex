from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from utils.mail_sender import MailSender

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    _send_email('Confirmação de Inscrição',
                settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'],
                'subscriptions/subscription_email.txt',
                form.cleaned_data
                )

    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')



def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def _send_email(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    send_email = MailSender(subject=subject,
                            body=body,
                            to=[to],
                            bcc=[from_],
                            from_email=from_)
    send_email.send()
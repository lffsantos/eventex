from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from utils.mail_sender import MailSender


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    subscrition = Subscription.objects.create(**form.cleaned_data)

    _send_email('Confirmação de Inscrição',
                settings.DEFAULT_FROM_EMAIL,
                subscrition.email,
                'subscriptions/subscription_email.txt',
                {'subscription': subscrition }
                )

    return HttpResponseRedirect(r('subscriptions:detail', subscrition.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


def _send_email(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    send_email = MailSender(subject=subject,
                            body=body,
                            to=[to, from_],
                            bcc=[from_],
                            from_email=from_)
    send_email.send()
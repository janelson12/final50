import twilio.twiml

import phonenumbers
from phonenumbers import format_number
from phonenumbers.phonenumberutil import NumberParseException

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from alerts.forms import SubscriberForm, UserForm
from alerts.models import Subscriber
from alerts.sms import send_sms

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        subscriber_form = SubscriberForm(request.POST)

        forms = (user_form, subscriber_form)

        if user_form.is_valid() and subscriber_form.is_valid():
            user = user_form.save()
            subscriber = subscriber_form.save(commit=False)
            subscriber.user = user
            subscriber.save()

            send_sms(subscriber.cell_phone, ("Welcome to Crimson Alerts! "
                "Text STOP to unsubscribe."))
            return redirect('success')
    else:
        forms = (UserForm(), SubscriberForm(),)

    return render(request, 'alerts/signup.html', {'forms': forms})


@csrf_exempt
def receive_sms(request):
    response = twilio.twiml.Response()
    response.message("Text STOP to unsubscribe or HELP for more options")
    return HttpResponse(response)
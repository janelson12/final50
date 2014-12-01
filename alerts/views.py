import twilio.twiml

import phonenumbers
from phonenumbers import format_number
from phonenumbers.phonenumberutil import NumberParseException

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from alerts.forms import SubscriberForm, UserForm
from alerts.models import Subscriber

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
    else:
        forms = (UserForm(), SubscriberForm(),)

    return render(request, 'alerts/signup.html', {'forms': forms})

@csrf_exempt
def receive_sms(request):
    response = twilio.twiml.Response()

    number_string = request.POST.get('From')
    if not number_string:
        return HttpResponseBadRequest("no number specified\n")

    try:
        number = phonenumbers.parse(number_string)
    except NumberParseException:
        return HttpResponseBadRequest("bad phone number\n")

    formatted_number = format_number(number, phonenumbers.PhoneNumber())


    try:
        subscriber = Subscriber.objects.get(cell_phone=formatted_number)
        response.message('Text STOP to unsubscribe')
    except Subscriber.DoesNotExist:
        response.message('You are not subscribed!')

    return HttpResponse(response)
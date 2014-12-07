#imports twillio API
import twilio.twiml

#imports python package that can format phone numbers
import phonenumbers
from phonenumbers import format_number
from phonenumbers.phonenumberutil import NumberParseException

# imports django http helper functions
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# imports subscriber and user forms and send_sms function from alerts folder
from alerts.forms import SubscriberForm, UserForm
from alerts.models import Subscriber
from alerts.sms import send_sms

def signup(request):
    #if the user tries to submit the form matches the html input info to python object fields
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        subscriber_form = SubscriberForm(request.POST)

        forms = (user_form, subscriber_form)
        #if html input translates to valid python object fields saves user info in mySQL
        if user_form.is_valid() and subscriber_form.is_valid():
            user = user_form.save()
            subscriber = subscriber_form.save(commit=False)
            subscriber.user = user
            subscriber.save()
            # for sucessful subscriptions sends welcome text after saving.
            send_sms(subscriber.cell_phone, ("Welcome to Crimson Alerts! "
                "Text STOP to unsubscribe."))
            # renders success page
            return redirect('success')
            
   # sets form blank if user doesn't input data 
    else:
        forms = (UserForm(), SubscriberForm(),)
    # renders form with notifications of any input errors 
    return render(request, 'alerts/signup.html', {'forms': forms})

# djagno said to use this on functions called by an API... unclear on what exacly it does 
# I feel like it's good for security or something tho
# Then receive_sms is a function that responds to everything but STOP and HELP ... (twillio automatically handles
# STOP and HELP
@csrf_exempt
def receive_sms(request):
    response = twilio.twiml.Response()
    response.message("Text STOP to unsubscribe or HELP for more options")
    return HttpResponse(response)

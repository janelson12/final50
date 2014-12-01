from django.conf import settings

from twilio.rest import TwilioRestClient
 
client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
 
def send_sms(to, body):
    return client.messages.create(body=body,
    	to=to,   
   	 	from_="+12678752746") # my Twilio number

#imports configuration settings 
from django.conf import settings

#imports twillio API
from twilio.rest import TwilioRestClient
 
 #Identifies my twilio account to take $$ from :( 
client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
 
 # function to send text from twillio (to is the number to be alerted, body is the message of the text)
def send_sms(to, body):
    return client.messages.create(body=body,
    	to=to,   
   	 	from_="+12678752746") # my Twilio number

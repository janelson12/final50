#django documentation said to put this file in management/commands... 

#imports classes from django
from django.core.management.base import BaseCommand, CommandError

#imports send_sms function and News/Subscriber models
from alerts.sms import send_sms
from alerts.models import News, Subscriber

# creates command for sending alerts
class Command(BaseCommand):
    help = 'Sends alerts for all new news to subscribers'

    def handle(self, *args, **options):
        news_to_send = News.objects.filter(alert_sent=False)
        subscribers = Subscriber.objects.all()

        print "Discovered {} unsent news articles".format(len(news_to_send))
        for idx, news in enumerate(news_to_send):
            print "    {}. {}".format((idx + 1), news.headline)
            news.alert_sent = True
            news.save()
        print ""

        for subscriber in subscribers:
            print "Sending to {} ({})...".format(subscriber.user.username,
                subscriber.cell_phone)
            for news in news_to_send:
                message = "BREAKING: {} {}. Reply STOP to unsubscribe."
                send_sms(subscriber.cell_phone, message.format(
                    news.headline, news.url))

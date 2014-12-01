from django import forms
from django.contrib.auth.forms import UserCreationForm

from alerts.models import Subscriber

class SubscriberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Subscriber
        exclude = ('user',)

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.label_suffix = ''

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')
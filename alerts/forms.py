# django makes these cool templates FOR YOU ALREADY!!!!!! (this is me importing them)
from django import forms
from django.contrib.auth.forms import UserCreationForm

# I made this cool alert model FOR ME ALREADY (this is me importing it)
from alerts.models import Subscriber

# Now I will do magic and edit the django form to be better b/c i'm awesome
# I'm changing the model form to base it's fields off of my subscriber model... except user (that's set automatically)
class SubscriberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        
        # dont have shit after labels in html for this lil' form
        self.label_suffix = ''
    
    class Meta:
        model = Subscriber
        exclude = ('user',)

# same as above but for user 
class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.label_suffix = ''

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')

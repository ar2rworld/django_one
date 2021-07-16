from books.models import Publisher
from django.forms import modelform_factory

from django import forms
TOPIC_CHOICES = (('general', 'General enquiry'),
  ('bug', 'Bug report'),
  ('suggestion', 'Suggestion'),)
class ContactForm(forms.Form):
  topic = forms.ChoiceField(choices=TOPIC_CHOICES)
  message = forms.CharField(widget=forms.Textarea(),initial="Your feedback")
  sender = forms.EmailField(required=False, initial='user@example.com')
  def clean_message(self):
    message = self.cleaned_data.get('message', '')
    num_words = len(message.split())
    if num_words < 4:
      raise forms.ValidationError("Not enough words!")
    if 'putin' in message.lower():
      raise forms.ValidationError("hm, wait a sec, we need to call KGB.")
    return message
PublisherForm = modelform_factory(Publisher,
  fields=('name', 'address', 'city', 'state_province', 'country', 'website'))
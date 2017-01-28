from django import forms

class NameForm(forms.Form):
    request_ID = forms.CharField(label='request ID', max_length=100, required=False)
    book_name = forms.CharField(label='Book Name', max_length=100, min_length=2, required=False)
    CHOICES = (('FA', 'FA'), ('EN', 'EN'))
    language = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())

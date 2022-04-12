from django import forms
from django.core import validators

class formName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcather=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])



    #def clean_botcatcher(self):
        #botcatcher=self.cleaned_data['botcatcher']
        #if len(botcatcher)>0:
            #raise forms.ValidationError('gotcha bot')
            #return botcatcher

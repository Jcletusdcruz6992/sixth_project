from django.shortcuts import render
from basicApp import forms



# Create your views here.
def index(request):
    return render(request,'basicApp/index.html')

def form_name(request):
    form=forms.formName()
    if request.method=='POST':
        form=forms.formName(request.POST)
        if form.is_valid():
            print('VALIDATION SUCCESS ')
            print('NAME '+form.cleaned_data['name'])
            print('EMAIL '+form.cleaned_data['email'])
            print('TEXT'+form.cleaned_data['text'])


    return render(request,'basicApp/forms_page.html',{'form':form})

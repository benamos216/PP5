from django.shortcuts import render, redirect, reverse
from . forms import SubscibersForm, MailMessageForm
from . models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame


def subscribe(request):
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('home')
    else:
        form = SubscibersForm()

    template = 'marketing/signupform.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def newsletter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('newsletter')
    else:
        form = MailMessageForm()

    template = 'marketing/newsletter.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

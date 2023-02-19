from django.shortcuts import render
from django.contrib import messages


def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        print(email)
        messages.success(request, "Email received. thank You! ") # message

    return render(request, "marketing/signupform.html")

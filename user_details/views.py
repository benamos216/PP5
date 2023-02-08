from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserDetails
from .forms import UserDetailsForm



# Create your views here.

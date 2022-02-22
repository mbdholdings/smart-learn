from django.shortcuts import render, redirect
from users.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from school.models import Grade
from .models import UserProfileInfo, Contact, Slide, Welcome, Announcement, Event
from django.views.generic import CreateView


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("Please use correct id and password")
            # return HttpResponseRedirect(reverse('register'))                
    else:
        return render(request, 'users/login.html')

 

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'users/registration.html',

                            {'registered':registered,

                            'user_form':user_form,

                            'profile_form':profile_form})
                        

class HomeView(TemplateView):

    template_name = 'users/index.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        slides = Slide.objects.all()

        grades = Grade.objects.all()

        welcome = Welcome.objects.all()

        announcement = Announcement.objects.all()

        event = Event.objects.all()


        teachers = UserProfileInfo.objects.filter(user_type='teacher')

        context['grades'] = grades

        context['teachers'] = teachers

        context['slides'] = slides

        context['welcome'] = welcome

        context['announcement'] = announcement

        context['event'] = event

        return context



class ContactView(CreateView):

    model = Contact
    fields = '__all__'

    template_name = 'users/contact.html'




from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Guitar, Pickup
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Auth imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    

class About(TemplateView):
    template_name = 'about.html'

class Tuner(TemplateView):
    template_name = 'tuner.html'

class GuitarList(TemplateView):
    template_name = 'guitarlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.request.GET.get("model")
        print('Model', model)
        if model != None:
            context["guitars"] = Guitar.objects.filter(model__icontains=model)
            context["header"] = f"Searching for {model}"
        else:
            context["guitars"] = Guitar.objects.all()
            context["header"] = "All Guitars"
        return context

@method_decorator(login_required, name='dispatch')
class Guitar_Create(CreateView):
    model = Guitar
    fields = '__all__'
    template_name = "guitar_create.html"
    # success_url = "/guitars/"
    # def get_success_url(self):
    #     return reverse('guitar_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/guitars')

class GuitarDetail(DetailView):
    model = Guitar
    template_name = "guitar_detail.html"

@method_decorator(login_required, name='dispatch')
class GuitarUpdate(UpdateView):
    model = Guitar
    fields = '__all__'
    template_name = "guitar_update.html"
    # success_url = "/guitars"
    def get_success_url(self):
        return reverse('guitar_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class GuitarDelete(DeleteView):
    model = Guitar
    template_name = "guitar_delete_confirm.html"
    success_url = "/guitars"

#Profile for the User
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    guitars = Guitar.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'guitars': guitars})

def pickups_index(request):
    pickups = Pickup.objects.all()
    return render(request, 'pickup_index.html', {'pickups': pickups})

def pickups_show(request, pickup_id):
    pickup = Pickup.objects.get(id=pickup_id)
    return render(request, 'pickup_show.html', {'pickup': pickup})

@method_decorator(login_required, name='dispatch')
class PickupCreate(CreateView):
    model = Pickup
    fields = '__all__'
    template_name = "pickup_form.html"
    success_url = '/guitars/new'

@method_decorator(login_required, name='dispatch')
class PickupUpdate(UpdateView):
    model = Pickup
    fields = ['type', 'brand', 'active']
    template_name = "pickup_update.html"
    success_url = '/pickups'

@method_decorator(login_required, name='dispatch')
class PickupDelete(DeleteView):
    model = Pickup
    template_name = "pickup_confirm_delete.html"
    success_url = '/pickups'

# Signup, Login, Logout
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Hey', user.username)
            return HttpResponseRedirect('/user/'+str(user.username))
        else:
            HttpResponse('<h1>Try again...</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/guitars')


def login_view(request):
    # if POST, then authenticate the user (submitting the username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: # it was a get request so send the emtpy login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

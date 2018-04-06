from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,View,CreateView,ListView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
from app.models import VendorListing



class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index_view'))
        else:
            return render(request, "user_create_view.html", {"form": form})
    form = UserCreationForm()
    return render(request, "user_create_view.html", {"form": form})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class IndexView(TemplateView):
    template_name = 'index.html'

class VendorListingCreateView(CreateView):
    model = VendorListing
    fields = ['vendor_name','vendor_image','vendor_email','vendor_phone','vendor_bio','todays_location','todays_hours','serving_today','truck_service','cart_service','popup_service']
    success_url = '/'
    def upload_pic(request):
        if request.method == 'POST':
            form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = VendorListing.objects.get(pk=id)
            m.model_pic = form.cleaned_data['vendor_image']
            m.save()
            return HttpResponse('image upload success')
            return HttpResponseForbidden('allowed only via POST')

class VendorListView(ListView):
    model = VendorListing

class RSSfeedView(ListView):
    model = VendorListing

class PrivacyDoc(TemplateView):
    template_name = 'privacydoc.html'

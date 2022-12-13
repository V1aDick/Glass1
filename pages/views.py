from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import CustomUser, Feedback, Record , Service
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

class indexView(TemplateView):
    template_name='index.html'

class aboutView(TemplateView):
    template_name = 'about.html'

class feedbackView(ListView):
    template_name = 'feedback.html'
    model = Feedback
    def post(self,request):
        text = request.POST.get('text')
        authorId = int(request.POST.get('id'))
        Feedback.objects.create(text=text, authorId=CustomUser.objects.get(id=authorId))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class signInView(TemplateView):
    template_name = 'signIn.html'
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print('да')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print('нет')
            return HttpResponseRedirect(request.META.get('HTTP_ORIGIN'))
class signUpView(TemplateView):
    template_name = 'signUp.html'
    def post(self,request,*args,**kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        code = request.POST.get('code')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        return HttpResponseRedirect(request.META.get('HTTP_ORIGIN'))


class recordView(ListView):
    template_name = 'record.html'
    model = Service
    def post(self,request):
        record = Record()
        record.date = request.POST.get('date')
        record.service = Service.objects.get(name=request.POST.get('goal'))
        record.comments = request.POST.get('comments')
        record.authorId = request.user
        record.save()
        return HttpResponseRedirect(request.META.get('HTTP_ORIGIN')+'/account')

class accountView(ListView):
    template_name = 'account.html'
    model = Record

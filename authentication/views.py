from django.shortcuts import render, HttpResponse, reverse
from .forms import LoginForm
from django.views.generic import View, FormView
from django.contrib.auth import login, authenticate


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(self.request, username=cd['username'], password=cd['password'])
        if user is not None:
            login(self.request, user)
        else:
            return HttpResponse('Invalid User')
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        pass

    def get_success_url(self):
        return reverse('chat:chat_app')
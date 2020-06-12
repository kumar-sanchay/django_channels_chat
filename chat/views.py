from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ChatView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'chat.html', {})
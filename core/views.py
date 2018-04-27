from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import User
# Create your views here.

class IndexView(generic.ListView):
    # context_object_name = 'latest_question_list'
    model = User
    template_name = 'core/cv.htm'

    def get_queryset(self):
        """Return the last five published questions"""
        return('-e')


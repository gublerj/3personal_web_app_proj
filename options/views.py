from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView): # TemplateView does alot by itslef
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

import script as gh

def get_hostname(request):
        gh.main()
        return HttpResponseRedirect('/')
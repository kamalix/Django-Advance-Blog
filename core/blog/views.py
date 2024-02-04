from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import Post

# Create your views here.

def indexView(request):
    '''
    a function based view to shoe index page
    '''
    context = {'name':'amani'}
    return render(request,'index.html',context)

class IndexView(TemplateView):
    """
    a class based view to shoe index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"]="kamal"
        context['posts']=Post.objects.all()
        return context


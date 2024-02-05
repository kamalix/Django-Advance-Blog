from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.

#function based view for show template
"""
def indexView(request):
    '''
    a function based view to shoe index page
    '''
    context = {'name':'amani'}
    return render(request,'index.html',context)
"""

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

'''FBV Redirect
from django.shortcuts import redirect
def RedirectToMaktab(request):
    return redirect('http://maktabkhooneh.com')
'''

class RedirectToMaktab(RedirectView):
    '''
    Redirect view sample for maktabkhooneh
    '''
    url = 'http://maktabkhooneh.com'

    def get_redirect_url(self, *args: Any, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    

class PostList(ListView):
    #model = Post
    #queryset = Post.objects.all()
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.filter(status=False)
        return posts
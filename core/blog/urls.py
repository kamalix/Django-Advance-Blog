from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


app_name = 'blog'

urlpatterns = [
    #path('cbv-index',views.IndexView.as_view(),name='cbv-index'),
    #path('go-to-maktabkhooneh/<int:pk>', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),

    path('post/',views.PostListView.as_view(),name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(),name='post-detail'),

]
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from . import api_views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', api_views.snippet_list,name='snippet-list'),
    path('snippets/<int:pk>/',api_views.snippet_detail,name='snippet-detail'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
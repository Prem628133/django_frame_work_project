from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from snippets.api_views import snippet_list, snippet_detail 
from snippets.cbv_views import SnippetList, SnippetDetail  
from snippets import views  
from snippets import mixin_views

urlpatterns = [
    path('snippets/', snippet_list, name='snippet-list'),  
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),  
    path('cbv/snippets/', SnippetList.as_view(), name='cbv-snippet-list'),  
    path('cbv/snippets/<int:pk>/', SnippetDetail.as_view(), name='cbv-snippet-detail'),
    path('users/', mixin_views.UserList.as_view()),
    path('users/<int:pk>/', mixin_views.UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
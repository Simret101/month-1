from django.urls import path
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', views.getAll),
    path('posts/<int:id>/',views.post_detail)
]
urlpatterns=format_suffix_patterns(urlpatterns)


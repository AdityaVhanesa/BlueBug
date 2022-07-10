from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='bug_index'),
    path('raise', views.RaiseBug.as_view(), name="raise_bug"),
    path('delete/<int:bugID>', views.RemoveBugView.as_view(), name='remove_bug'),
]
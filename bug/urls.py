from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='bug_index'),
    path('raise', views.RaiseBug.as_view(), name="raise_bug"),
    path('delete/<int:bugID>', views.RemoveBugView.as_view(), name='remove_bug'),
    path('edit/<int:bugID>', views.EditBugView.as_view(), name='edit_bug'),
    path('close/<int:bugID>', views.CloseBugView.as_view(), name='close_bug'),
    path('open/<int:bugID>', views.ReOpenBugView.as_view(), name='re_open_bug'),
    path('comment/<int:bugID>', views.CommentBugView.as_view(), name='comment_bug'),
]
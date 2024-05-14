from django.urls import path
from .views import Log_out, NewsView, PostDetail, Create_post, Update_post, Delete_post

urlpatterns = [
    path('post/<int:pk>/delete/', Delete_post.as_view(), name='delete_post'),
    path('post/<int:pk>/edit/', Update_post.as_view(), name='edit_post'),
    path('post/new', Create_post.as_view(), name='newpost'),
    path('', NewsView.as_view(), name='news'),
    path('post/<int:pk>', PostDetail.as_view(), name='detail_page'),
    path('logout/', Log_out, name='logout')
]

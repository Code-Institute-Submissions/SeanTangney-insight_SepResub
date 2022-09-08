from . import views
from .views import EditView
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(),
         name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create-view', views.CreateView.as_view(), name='create_view'),
    path('edit-view/<int:pk>', EditView.as_view(), name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete-post'),
    ]

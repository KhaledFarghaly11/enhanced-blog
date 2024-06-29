from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('contact/', views.contact, name='blog_contact'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_details, name='blog_post'),
    path('tag/<slug:tag_slug>/', views.home, name='post_list_by_tag'),
    path('post/<post_id>/comment', views.post_comment, name="post_comment"),
]
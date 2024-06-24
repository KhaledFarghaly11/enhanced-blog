from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('contact/', views.contact, name='blog_contact'),
    path('post/', views.post_details, name='blog_post'),

    # path('post/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='blog_post'),
    # path('post/<post_id>/comment', views.post_comment, name="post_comment"),
]
from django.shortcuts import render, get_object_or_404

from blog.models import AboutPage, ContactPage, HomePage, Post

def home(request):
  page = HomePage.objects.all()[0]
  posts = Post.objects.filter(status='PB')
  return render(request, 'blog/home.html', {'page': page, 'posts': posts})

def about(request):
  page = AboutPage.objects.all()[0]
  return render(request, 'blog/about.html', {'page': page})

def contact(request):
  page = ContactPage.objects.all()[0]
  return render(request, 'blog/contact.html', {'page': page})

def post_details(request, year, month, day, post):
  post = get_object_or_404(Post, 
                           publish__year=year,
                           publish__month=month,
                           publish__day=day,
                           slug=post, 
                           status=Post.Status.PUBLISHED)
  return render(request, 'blog/post_details.html', {'post': post})
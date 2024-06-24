from django.shortcuts import render, get_object_or_404

from blog.models import AboutPage, ContactPage, HomePage

def home(request):
  page = HomePage.objects.all()[0]
  return render(request, 'blog/home.html', {'page': page})

def about(request):
  page = AboutPage.objects.all()[0]
  return render(request, 'blog/about.html', {'page': page})

def contact(request):
  page = ContactPage.objects.all()[0]
  return render(request, 'blog/contact.html', {'page': page})

def post_details(request):
  return render(request, 'blog/post_details.html')
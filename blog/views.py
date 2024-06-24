from django.shortcuts import render, get_object_or_404

def home(request):
  return render(request, 'blog/home.html')

def about(request):
  return render(request, 'blog/about.html')

def contact(request):
  return render(request, 'blog/contact.html')

def post_details(request):
  return render(request, 'blog/post_details.html')
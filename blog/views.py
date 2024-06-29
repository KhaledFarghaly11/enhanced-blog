from django.shortcuts import render, get_object_or_404
from blog.forms import CommentForm, ContactForm
from blog.models import AboutPage, ContactPage, HomePage, Post
from taggit.models import Tag
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request, tag_slug=None):
  page = HomePage.objects.all()[0]
  post_list = Post.objects.filter(status='PB')

  tag = None

  if tag_slug:
    tag = get_object_or_404(Tag, slug=tag_slug)
    post_list = post_list.filter(tags__in=[tag])
  
  paginator = Paginator(post_list, 5)
  page_number = request.GET.get('page', 1)
  try:
      posts = paginator.page(page_number)
  except PageNotAnInteger:
      posts = paginator.page(1)
  except EmptyPage:
      posts = paginator.page(paginator.num_pages)
  return render(request, 'blog/home.html', {'page': page, 'posts': posts, 'tag':tag})

def about(request):
  page = AboutPage.objects.all()[0]
  return render(request, 'blog/about.html', {'page': page})

def contact(request):
  page = ContactPage.objects.all()[0]
  sent = False
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      subject = f"{cd['name']} sent you an email"
      message = f"{cd['name']}\'s Message:\n{cd['message']} \n {20*'-'} \n {cd['name']} \n {cd['phone']} \n {cd['email']}"
      send_mail(subject, message, cd['email'], ['khaledboob21@gmail.com'])
      sent = True
  else:
    form = ContactForm()
  return render(request, 'blog/contact.html', {'page': page, 'sent':sent})

def post_details(request, year, month, day, post):
  post = get_object_or_404(Post, 
                           publish__year=year,
                           publish__month=month,
                           publish__day=day,
                           slug=post, 
                           status=Post.Status.PUBLISHED)
  comments = post.comments.filter(active=True)
  return render(request, 'blog/post_details.html', {'post': post, 'comments': comments})

def post_comment(request, post_id):
  post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
  
  comment = None
  
  form = CommentForm(data=request.POST)

  if form.is_valid():
    comment = form.save(commit=False)
    comment.post = post
    comment.save()
    
  return render(request, 'blog/comment.html', {'comment': comment, 'form': form, 'post': post})

# def contact_view(request):
#   sent = False
#   if request.method == 'POST':
#     form = ContactForm(request.POST)
#     if form.is_valid():
#       cd = form.cleaned_data
#       subject = f"{cd['name']} sent you an email"
#       message = f"{cd['name']}\'s Message:\n{cd['message']} \n {20*'-'} \n {cd['name']} \n {cd['phone']} \n {cd['email']}"
#       send_mail(subject, message, cd['email'], ['khaledboob21@gmail.com'])
#       sent = True
#   else:
#     form = ContactForm()
#   return render(request, 'blog/contact.html', {'form': form, 'sent':sent})
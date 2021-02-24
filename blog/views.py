from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from .models import Post
from .forms import CreatePost, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
# class PostList(generic.ListView):
#     queryset = Post.objects.all().order_by('-created_on')
#     template_name = 'blog/index.html'

def post_list(request):
    if request.user.is_authenticated:
        data = Post.objects.all().order_by('-created_on')
        paginator = Paginator(data, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return (render(request, 'blog/index.html',{'data':page_obj,'name': request.user}))
    else:
        return(HttpResponseRedirect('/login/'))

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'

def post_detail(request, slug):
    post=get_object_or_404(Post, slug=slug)
    return render(request,'blog/post_detail.html',{'data':post})

def create_post(request):
    form = CreatePost(request.POST or None)
    data = Post.objects.all().order_by('-created_on')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return (render(request, 'blog/index.html',{'data':data}))
    else:
        form = CreatePost()
    return (render(request, 'blog/create.html',{'form':form}))

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = SignUpForm()
    return(render(request,'blog/signup.html',{'form':fm}))

def log_in(request):
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
        else:
            fm = AuthenticationForm()

        return(render(request,'blog/login.html',{'form':fm}))
    else:
        return(HttpResponseRedirect('/'))

def log_out(request):
    logout(request)
    return(HttpResponseRedirect('/login/'))

def update_post(request, slug):
    order = Post.objects.get(slug=slug)
    form = CreatePost(instance=order)

    if request.method == 'POST':
        form = CreatePost(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return(HttpResponseRedirect('/'))

    return(render(request, 'blog/create.html',{'form':form}))

def delete_post(request, slug):
    order = Post.objects.get(slug=slug)
    if request.method == "POST":
        order.delete()
        return(HttpResponseRedirect('/'))

    return(render(request, 'blog/delete.html', {'item':order}))

def user_list(request):
    if request.user.is_authenticated:
        data = Post.objects.filter(author = request.user).order_by('-created_on')
        paginator = Paginator(data, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return (render(request, 'blog/user_list.html',{'data':page_obj,'name': request.user}))
    else:
        return(HttpResponseRedirect('/login/'))

def search_blog(request):
    qur = request.GET.get('search')
    blogs = Post.objects.filter(title__contains = qur)
    return(render(request, 'blog/index.html', {'data':blogs}))
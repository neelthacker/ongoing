from blog.models import Post, Category
from blog.forms import CreatePost, SignUpForm, CategoryForm

from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect


def post_list(request):
    if request.user.is_authenticated:
        context = {}
        data_category = Category.objects.all()
        context['data_category'] = data_category
        if request.GET.get('category') or request.GET.get('q'):
            query = request.GET.get('q')
            query2 = request.GET.get('category')
            caterory_search = 0
            context['category_search'] = caterory_search
            if request.GET.get('q'):
                blog_query = Post.objects.filter(
                    Q(title__icontains=query) | Q(content__icontains=query))
                if request.GET.get('category'):
                    blog_query2 = Post.objects.filter(
                        Q(category__title__icontains=query2))
                    blogs = blog_query & blog_query2
                else:
                    blogs = blog_query
            elif request.GET.get('category'):
                blog_query2 = Post.objects.filter(
                    Q(category__title__icontains=query2))
                if request.GET.get('q'):
                    blog_query = Post.objects.filter(
                        Q(title__icontains=query) | Q(content__icontains=query))
                    blogs = blog_query & blog_query2
                else:
                    blogs = blog_query2
            context['category2'] = query2
            context['query'] = query
        elif request.GET.get('query_search'):
            query = request.GET.get('query_search')
            caterory_search = 0
            context['category_search2'] = caterory_search
            context['query'] = query
            blogs = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query))
            context['query'] = query
        else:
            blogs = Post.objects.all().order_by('-created_on')

        paginator = Paginator(blogs, 5)
        page_number = request.GET.get('page')
        try:
            blogs = paginator.page(page_number)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        context['blogs'] = blogs
        return (render(request, 'blog/index.html', context))
    else:
        return(HttpResponseRedirect('/login/'))


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'data': post})


def create_post(request):
    if not request.user.is_authenticated:
        return(HttpResponseRedirect('/'))
    else:
        form = CreatePost(request.POST or None)
        update = 0
        if request.method == 'POST':
            if form.is_valid():
                f = form.save(commit=False)
                f.author = request.user
                f.save()
            return(HttpResponseRedirect('/'))
        else:
            form = CreatePost()

        return (render(request, 'blog/create.html', {'form': form, 'update': update}))


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return(render(request, 'blog/signup.html', {'form': form}))


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
        return(render(request, 'blog/login.html', {'form': fm}))
    else:
        return(HttpResponseRedirect('/'))


def log_out(request):
    logout(request)
    return(HttpResponseRedirect('/login/'))


def update_post(request, slug):
    order = Post.objects.get(slug=slug)
    form = CreatePost(instance=order)
    update = 1
    if request.method == 'POST':
        form = CreatePost(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return(HttpResponseRedirect('/'))
    return(render(request, 'blog/create.html', {'form': form, 'update': update}))


def delete_post(request, slug):
    order = Post.objects.get(slug=slug)
    if request.method == "POST":
        order.delete()
        return(HttpResponseRedirect('/'))
    return(render(request, 'blog/delete.html', {'item': order}))


def user_list(request):
    if request.user.is_authenticated:
        data = Post.objects.filter(author=request.user).order_by('-created_on')
        paginator = Paginator(data, 5)
        page_number = request.GET.get('page')
        try:
            blogs = paginator.page(page_number)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        return (render(request, 'blog/user_list.html', {'data': blogs, 'name': request.user}))
    else:
        return(HttpResponseRedirect('/login/'))


def add_category(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return(HttpResponseRedirect('/'))
        return(render(request, 'blog/add_category.html'))


def ajax_search(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        ajax_blogs = Post.objects.filter(
            Q(title__icontains=url_parameter) | Q(content__icontains=url_parameter))
    else:
        ajax_blogs = Post.objects.all()

    ctx['ajax_blogs'] = ajax_blogs

    if request.is_ajax():
        html = render_to_string(
            template_name="blog/ajax-blogs-data.html",
            context={"ajax_blogs": ajax_blogs}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict)

    return (render(request, "blog/ajax_search.html", context=ctx))

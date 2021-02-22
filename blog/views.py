from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import CreatePost

# Create your views here.
# class PostList(generic.ListView):
#     queryset = Post.objects.all().order_by('-created_on')
#     template_name = 'blog/index.html'

def postlist(request):
    data = Post.objects.all().order_by('-created_on')
    return (render(request, 'blog/index.html',{'data':data}))

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'

def postdetail(request, slug):
    pass
    data = Post.objects.get(slug=slug)
    return(render(request,'blog/post_detail.html',{'data':data}))

def create_post(request):
    form = CreatePost(request.POST or None)
    data = Post.objects.all().order_by('-created_on')

    if request.method == 'POST':
        import pdb;pdb.set_trace()
        if form.is_valid():
            form.save()
        return (render(request, 'blog/index.html',{'data':data}))

    else:
        form = CreatePost()
    return (render(request, 'blog/create.html',{'form':form}))
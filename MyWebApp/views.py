from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'MyWebApp/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'MyWebApp/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('MyWebApp.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'MyWebApp/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('MyWebApp.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'MyWebApp/post_edit.html', {'form': form})
'''
#http://stackoverflow.com/questions/3124658/django-delete-object
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid(): # checks CSRF
            post.delete()
            return redirect('MyWebApp.views.post_detail.html', pk=post.pk)

    else:
        form = PostForm(instance=post)

    template_vars = {'form': form}
    return render(request, 'MyWebApp/post_detail.html', template_vars)
    '''
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CreatePostForm
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'home.html', {"posts": Post.objects.all()})


def create_post(request):
    # context = {'form': CreatePostForm()}
    context = dict()
    form = CreatePostForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect('home')

    context['form'] = form
    # context['target_url'] = reverse('home')

    return render(request, 'add_posts.html', context)


def delete(request, post_id):
    post = Post.objects.get(
        id=post_id
    )
    post.delete()
    return redirect('home')


def update(request, post_id):

    obj = get_object_or_404(Post, id=post_id)

    form = CreatePostForm(request.POST or None, instance=obj)
    context = dict()
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('home')

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)

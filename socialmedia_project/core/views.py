from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, PostForm, ProfileForm, CommentForm
from .models import Post, Like, Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment


# SIGNUP
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Don't create profile here — signal will handle it
            login(request, user)
            return redirect('feed')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('feed')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# LOGOUT
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


# FEED VIEW
@login_required
def feed_view(request):
    post_form = PostForm()
    comment_form = CommentForm()

    if request.method == 'POST':
        if 'content' in request.POST or 'image' in request.FILES:  # Post Form
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('feed')

        elif 'text' in request.POST and 'post_id' in request.POST:  # Comment Form
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.post_id = request.POST.get('post_id')
                comment.save()
                return redirect('feed')

    posts = Post.objects.all().order_by('-created_at')
    for post in posts:
        post.is_liked = Like.objects.filter(user=request.user, post=post).exists()

    return render(request, 'feed.html', {
        'post_form': post_form,
        'comment_form': comment_form,
        'posts': posts,
    })


# LIKE / UNLIKE POST
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return HttpResponseRedirect(reverse('feed'))


# EDIT POST
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


# DELETE POST
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('feed')
    return render(request, 'delete_post.html', {'post': post})


# VIEW PROFILE
@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')
    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'posts': posts
    })


# EDIT PROFILE
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

# HOME VIEW
@login_required
def home_view(request):
    return render(request, 'home.html')

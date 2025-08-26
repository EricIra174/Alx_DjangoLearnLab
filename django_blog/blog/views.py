from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView ,DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm
from taggit.models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/register.html"

@login_required
def edit_profile(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        user = request.user
        user.username = username
        user.email = email
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("edit_profile")
    return render(request, "blog/edit_profile.html")
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/User_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        posts = Post.objects.filter(Post=Post)
        return context

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    ordering = ["-published_date"]
 
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = ("blog/post_update_form.html")
    success_url = reverse_lazy("post_list")
    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete_form.html"
    success_url = reverse_lazy("post_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post deleted successfully.")
        return super().delete(request, *args, **kwargs)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
def add_comment(request, title):
    post = get_object_or_404(Post, title=title)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect("post_list", title=post.title)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form, "post": post})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_delete_form.html"
    
    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"title": self.object.post.title})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_staff
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ["content"]
    template_name = "blog/comment_update_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"title": self.object.post.title})

    def form_valid(self, form):
        messages.success(self.request, "Comment updated successfully.")
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_staff
    
class CommentListView(ListView):
    model = Comment
    template_name = "blog/comment_list.html"

    def get_queryset(self):
        post_title = self.kwargs.get("title")
        return Comment.objects.filter(post__title=post_title).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, title=self.kwargs.get("title"))
        return context
    
class CommentDetailView(DetailView):
    model = Comment
    template_name = "blog/comment_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = self.get_object()
        context['post'] = comment.post
        return context
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, title=self.kwargs.get("title"))
        messages.success(self.request, "Comment added successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"title": self.object.post.title})
    
class PostByTagListView(ListView):
    model = Post
    template_name = "blog/posts_by_tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[self.tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context
    
def search_posts(request):
    query = request.GET.get("q")
    posts = Post.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |           
            Q(content__icontains=query) |         
            Q(tags__name__icontains=query)        
        ).distinct()
    return render(request, "blog/search_results.html", {"posts": posts, "query": query})
import os
from django.views.generic import (
    DetailView, TemplateView, 
    ListView, UpdateView,
    DeleteView, CreateView
)
from django.urls import reverse_lazy

from .models import Category, Post, Comment, Likes, Subscribe
from authsystem.models import User 
from .forms import CommentCreationalFrom, PostCreationalFrom
from services.mailing_service import notificate
from services.pages_logic import (
    add_homepage_posts, 
    add_detail_context, 
    create_post, 
    create_comment,
    )


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = add_homepage_posts(context, Post)

        from server.settings import STATIC_ROOT
        print(STATIC_ROOT+'/pages/styles')

        return context
    

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category/category_list.html'
    context_object_name = 'categories'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post/post_update.html'
    fields = ['title', 'text', 'category', 'photo_preview']
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = add_detail_context(context, Likes, Comment, CommentCreationalFrom)
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        comment_text = request.POST.get('text').strip()
        if comment_text == '':
            return super().get(request, *args, **kwargs)

        create_comment(
            user=request.user, 
            comment=Comment,
            post=Post,
            pk=str(kwargs['pk']),
            text=comment_text,)
        return super().get(request, *args, **kwargs)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created']

    def get_queryset(self):
        categories = Category.objects.all()
        query = self.request.GET.get('category')
        for i in categories:
            if str(i.pk) == query:
                return Post.objects.filter(category__pk=query)
        return super().get_queryset()

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationalFrom
    template_name = 'blog/post/post_create.html'

    def post(self, request, *args, **kwargs):
        return create_post(
            get_form=self.get_form, 
            request=request,
            post=Post,
            subscribe=Subscribe,
            form_invalid=self.form_invalid
            )
    
    def get_success_url(self):
        return reverse_lazy('post_detail',kwargs={'pk': self.get_object().id})
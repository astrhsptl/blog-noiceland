from django.views.generic import ListView, TemplateView, UpdateView, DetailView
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.urls import reverse_lazy    

from .forms import UpdateUserForm
from pages.models import Post, Subscribe
from services.authentication_services import is_authenticated


User = get_user_model()


class AuthorsListView(ListView):
    model = User
    template_name = 'blog/authors/authors.html'
    context_object_name = 'authors'


class AuthorDetail(DetailView):
    model = User
    template_name = 'blog/authors/author.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = Post.objects.filter(author=context['object'].pk)
        
        paginator = Paginator(posts, 2)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['subscribers'] = Subscribe.objects.filter(author=context['object'].pk).select_related()
        context["posts"] = posts
        print(context)
        return context

class UserUpdateView(UpdateView):
    form_class = UpdateUserForm
    model = User
    template_name = "account/user_update.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user 
        posts = Post.objects.filter(author=context['object'].pk)
        
        context["posts"] = posts

        return context
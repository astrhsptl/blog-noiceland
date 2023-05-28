from django.db.models import Model
from django.shortcuts import redirect
from django.urls import reverse_lazy

def add_homepage_posts(context, model: Model):
    try:
        context['latest'] = model.objects.latest('created')
        context['popular'] = model.objects.exclude(pk=context['latest'].pk).order_by('-created')[:12]
        context['futured'] = model.objects.exclude(pk=context['latest'].pk).order_by('-created')[:12]
    except:
        context['latest'] = []
        context['popular'] = []
        context['futured'] = []
    
    return context

def add_detail_context(context, Likes, Comment, Form):
    context['likes'] = Likes.objects.filter(post=context['post']).count()
    context['comments'] = Comment.objects.filter(post=context['post'].id)
    context['comment_form'] = Form
    return context

def create_post(get_form, request, post, subscribe, form_invalid):
    form = get_form()
    if form.is_valid():
        form.cleaned_data['author'] = request.user
        post = post.objects.create(**form.cleaned_data)
        print(subscribe.objects.filter(author=request.user).select_related())
        # notificate.delay(str(request.user.pk))
        return redirect(reverse_lazy('post_detail', kwargs={'pk': post.pk}))
    else:
        return form_invalid(form)
    
def create_comment(user, comment, post, pk, text):
    comment = comment.objects.create(
        author=user,
        post=post.objects.get(pk=pk),
        text=text,)
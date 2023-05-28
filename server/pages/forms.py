from django import forms

from .models import Comment, Post, Category

class CommentCreationalFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class PostCreationalFrom(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
                                            attrs={'placeholder': 'Title'}))
    text = forms.CharField(max_length=4096, widget=forms.Textarea(
                                            attrs={'placeholder': 'Text'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Choose category", widget=forms.Select(
                                            attrs={'placeholder': 'Choose category'}, ))
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'photo_preview', 'author']

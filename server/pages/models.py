import uuid

from django.db import models
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=64)
    discription = models.CharField(max_length=256)
    photo_preview = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("category_detail", kwargs={"pk": self.id})


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=4096)
    category = models.ForeignKey(Category, models.PROTECT)
    photo_preview = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(User, models.CASCADE, related_name='author', blank=True, null=True)
    created = models.DateField(auto_now_add=True, null=True,)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.id})


class Likes(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False)
    post = models.ForeignKey(Post, models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ("Like")
        verbose_name_plural = ("Likes")

    def __str__(self):
        return str(self.user.email)
    def get_absolute_url(self):
        return reverse_lazy("like", kwargs={"pk": self.id})

class Subscribe(models.Model):
    author = models.ForeignKey(User, models.CASCADE, null=True, blank=True, related_name='user_author')
    subscriber = models.ForeignKey(User, models.CASCADE, null=True, blank=True, related_name='user_subscriber')

    class Meta:
        verbose_name = ("Subscribe")
        verbose_name_plural = ("Subscribes")

    def __str__(self):
        return str(self.subscriber.email)
    def get_absolute_url(self):
        return reverse_lazy("subscribes", kwargs={"pk": self.id})
    

class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False)
    text = models.CharField(max_length=256)
    post = models.ForeignKey(Post, models.CASCADE, null=True, blank=True, related_name='post')
    author = models.ForeignKey(User, models.CASCADE, null=True, blank=True, related_name='comment_author')
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse_lazy("comment", kwargs={"pk": self.id})
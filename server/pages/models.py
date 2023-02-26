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
        return reverse_lazy("category", kwargs={"pk": self.id})


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=4096) # next - file
    category = models.ForeignKey(Category, models.PROTECT)
    photo_preview = models.ImageField(upload_to='category/')
    author = models.ForeignKey(User, models.CASCADE)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("post", kwargs={"pk": self.id})



class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False)
    text = models.CharField(max_length=256)
    post = models.ForeignKey(Post, models.CASCADE)
    author = models.ForeignKey(User, models.CASCADE)


    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse_lazy("comment", kwargs={"pk": self.id})


from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from birthday import BirthdayField
from django.urls import reverse


class Author(models.Model):
    """The Author class is a model that extends the User model and includes additional fields
    such as avatar, name, surname, and birthday."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    avatar = models.ImageField(null=True, blank=True, upload_to="avatar/", )
    name = models.CharField(null=True, blank=True, max_length=64, )
    surname = models.CharField(null=True, blank=True, max_length=64, )
    birthday = BirthdayField(null=True, blank=True, )

    def __str__(self):
        return f"{self.user}"


class Category(models.Model):
    """The `Category` class is a Django model with a `name` attribute that represents a category and
    has a string representation of the category name."""
    name = models.CharField(max_length=64, unique=True, )

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    """This is a Django model for a blog post with fields for author, image, category, header, text, and datetime."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
    image = models.ImageField(null=False, blank=False, upload_to="images/", )
    category = models.ForeignKey(null=False, blank=False, to='Category', on_delete=models.CASCADE, )
    header = models.CharField(null=False, blank=False, max_length=150, )
    text = RichTextField(null=False, blank=False, )
    datetime = models.DateTimeField(auto_now_add=True, )

    def get_post_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.header}"


class Feedback(models.Model):
    """The Feedback class defines a model for comments on a Post by a User, including the comment text and date."""
    feedback_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="feedback_post", )
    feedback_user = models.ForeignKey(User, on_delete=models.CASCADE, )
    text = models.TextField(null=False, blank=False, )
    datetime = models.DateTimeField(auto_now_add=True, )
    user_subscribed = models.BooleanField(default=False, )

    def __str__(self):
        return f"{self.feedback_post}, " \
               f"{self.feedback_user}, " \
               f"{self.datetime}"


class SubscribeFeedback(models.Model):
    """The SubscribeFeedback class defines a model for a subscription
    relationship between a user and a feedback object."""
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='consideration',
    )
    feedback = models.ForeignKey(
        to=Feedback,
        on_delete=models.CASCADE,
        related_name='consideration',
    )

    def __str__(self):
        return f"{self.user} subscribed to {self.feedback}"

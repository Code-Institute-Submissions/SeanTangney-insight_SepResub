from .models import Comment, Post, createPostModel
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class createPostForm(forms.ModelForm):
    class Meta:
        model = createPostModel
        fields = [
            "title",
            "body",
        ]

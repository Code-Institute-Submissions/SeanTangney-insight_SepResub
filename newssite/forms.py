from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    body = forms.CharField(max_length=200)

    class Meta:

        model = Post
        fields = ('title', 'featured_image', 'body')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields[
            'featured_image'
        ].label = "Upload Your Image"

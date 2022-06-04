from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    body = forms.CharField(
        max_length=750,
        widget=forms.Textarea(),
        )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'body',)

    title = forms.CharField(max_length=100)
    body = forms.CharField(
        max_length=1500,
        widget=forms.Textarea(),
        )

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields[
            'featured_image'
        ].label = "Upload Your Image"

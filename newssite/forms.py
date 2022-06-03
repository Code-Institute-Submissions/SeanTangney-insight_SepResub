from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'body',)

    title = forms.CharField(max_length=50)
    body = forms.CharField(
        max_length=200,
        widget=forms.Textarea(),
        help_text="Write your message here!"
        )

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields[
            'featured_image'
        ].label = "Upload Your Image"

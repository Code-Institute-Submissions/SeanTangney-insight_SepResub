from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.text import slugify
from .models import Post
from .forms import CommentForm, PostForm

# Display Posts on homepage


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# Display Posts in post_detail


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
                "liked": liked
            },
        )
        return HttpResponseRedirect(reverse('post_detail'))


# Add A Like To A Post


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect(reverse('post_detail', args=[slug]))


# View for creating posts


class CreateView(CreateView):

    def get(self, request, *args, **kwargs):

        return render(
            request, "create_view.html",
            {
                "create_view": PostForm()
            },
            )

    def post(self, request, *args, **kwargs):
        create_view = PostForm(request.POST, request.FILES)

        if create_view.is_valid():
            post = create_view.save(commit=False)
            post.author = request.user
            post.slug = slugify('-'.join([post.title,
                                          str(post.author)]),
                                allow_unicode=False)
            post.save()

            messages.success(self.request, 'Thanks for Posting')
            return HttpResponseRedirect(reverse('create_view'))

        else:
            messages.error(self.request, 'Please complete required fields')
            create_view = PostForm(data=request.POST)

        return render(
            request,
            "create_view.html",
            {
                "create_view": PostForm(),
            },
        )


# Edit Posts


class EditView(UpdateView):
    """ Edit Post """
    model = Post
    template_name = 'edit_view.html'
    fields = ['title', 'body', 'featured_image']

    def get_success_url(self):
        try:
            url = self.object.get_absolute_url()
        except AttributeError:
            raise ImproperlyConfigured(
                "No URL to redirect to.  Either provide a url or define"
                " a get_absolute_url method on the Model.")
        return url


# Delete Post


def delete_post(request, post_id):
    """Deletes post"""
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect(reverse(
        'home'))

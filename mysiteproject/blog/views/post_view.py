# from django.views import generic
# from ..models.post import Post

# class PostView(generic.View):
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "blog/index.html"
#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"


from django.views.generic import ListView, DetailView
from ..models.post import Post


class PostView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    context_object_name = "post_list"  # Nome do contexto para o template


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

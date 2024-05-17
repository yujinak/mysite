from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(
    models.Model
):  # classe criada passando como argumento o Model de models, que já tem campos pré-definidos
    title = models.CharField(max_length=200, unique=True)  # título do post
    slug = models.SlugField(max_length=200, unique=True)  # identificação do post
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )  # autor
    updated_on = models.DateTimeField(auto_now=True)  # atualização
    content = models.TextField()  # o texto do post em si
    created_on = models.DateTimeField(auto_now_add=True)  # quando foi criado
    status = models.IntegerField(
        choices=STATUS, default=0
    )  # se está como rascunho ou publicado

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

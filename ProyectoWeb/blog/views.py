from django.shortcuts import render
from blog.models import Categoria, Post

# Create your views here.



def blog(request):

    posts = Post.objects.all()
    return render(request,"blog/blog.html",{"posts": posts })  #dentro de la carpeta blog , el archivo blog


def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request,"blog/categoria.html",{'categoria':categoria,'posts': posts})

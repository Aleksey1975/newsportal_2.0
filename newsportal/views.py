from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import *
from .filters import *
from .forms import *
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


def index(request):
    return render(request, 'index.html')


class ListNews(ListView):
    queryset = Post.objects.filter(type_post=news)
    ordering = '-time_created'
    template_name = 'index_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset

        return context


class ListNewsOnly(ListView):
    queryset = Post.objects.filter(type_post=news)
    ordering = '-time_created'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class ListArticles(ListView):
    queryset = Post.objects.filter(type_post=article)
    ordering = '-time_created'
    template_name = 'index_articles.html'
    context_object_name = 'articles'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class DetailNews(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['author1'] = str(post.author)
        context['admin'] = 'admin'
        context['title'] = 'Новость'


        return context


class DetailArticle(DetailView):
    model = Post
    template_name = 'one_article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['author1'] = str(post.author)
        context['admin'] = 'admin'
        context['title'] = 'Статья'

        return context



class NewsCreate( CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = 'Добавить новость'
        context['button'] = 'Добавить'
        context['title'] = 'Добавить новость'
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_post = news
        return super().form_valid(form)


class ArticleCreate( CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = 'Добавить статью'
        context['button'] = 'Добавить'
        context['title'] = 'Добавить статью'
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_post = article
        return super().form_valid(form)



class NewsEdit( UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отредактировать новость'
        context['button'] = 'Отредактировать'
        return context



class ArticleEdit( UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = 'Отредактировать статью'
        context['button'] = 'Отредактировать'
        return context


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles')









def comments(request):
    comments = Comment.objects.all()
    context = {
        'title':'Комментарии',
        'comments':comments
    }
    return render(request, 'comments.html', context)



def showcomment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    context = {
        'title':'comment',
        'comment':comment

    }
    return render(request, 'showcomment.html', context)


def showpost(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'title':post.title,
        'post':post

    }
    return render(request, 'showpost.html', context)




def like_news(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.like()
    post.save()
    return redirect('one_news', post_id)

def dislike_news(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.dislike()
    post.save()
    return redirect('one_news', post_id)

def like_article(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.like()
    post.save()
    return redirect('one_article', post_id)

def dislike_article(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.dislike()
    post.save()
    return redirect('one_article', post_id)

def like_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.like()
    comment.save()
    return redirect('showcomment', comment_id)

def dislike_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.dislike()
    comment.save()
    return redirect('showcomment', comment_id)




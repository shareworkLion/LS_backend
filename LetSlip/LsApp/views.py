from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator

# 일단 이 부분을 본인 갤러리로 두고 구현했음
def home(request):
    # posts = Post.objects.all() 
    posts = Post.objects.filter().order_by('-date')
    paginator = Paginator(posts, 6)
    pagenum = request.GET.get('page')
    posts = paginator.get_page(pagenum)
    return render(request, 'home.html', {'posts': posts})


# 새 갤러리 생성
def post_new(request):
    if request.method == 'POST' or request.method == "FILES":
        form = PostForm(request.POST, request.FILES)       
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.author = form.cleaned_data['author']
            post.category = form.cleaned_data['category']
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form':form})

# 갤러리 상세페이지
def post_detail(request, post_id):
    detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'post_detail.html', {'detail':detail}, {'comment_form':comment_form})


# 댓글 
def comment_new(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('post_detail', post_id)

# 검색
def search(request):
        keyword = request.POST.get('searched', "") 
        if keyword:
            categories = Post.objects.all()
            posts = categories.filter(category__contains=keyword)
            return render(request, 'searched.html', {'posts':posts, 'keyword':keyword})
        else:
            return render(request, 'searched.html', {})

    
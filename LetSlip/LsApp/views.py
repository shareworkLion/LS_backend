from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category, CommentReply
from .forms import PostForm, CommentForm, CommentReplyForm
from django.core.paginator import Paginator
from datetime import datetime 
from django.utils.dateformat import DateFormat
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse






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
            unfinished = form.save(commit=False)
            unfinished.author = request.user            # user 추가!
            unfinished.save()
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.body = form.cleaned_data['body']
            # post.author = form.cleaned_data['author']
            # post.category = form.cleaned_data['category']
            # form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form':form})

# 갤러리 상세페이지
def post_detail(request, post_id):
    detail = get_object_or_404(Post, pk=post_id) 
    comment_form = CommentForm()
    comment_reply_form = CommentReplyForm()
    return render(request, 'post_detail.html', {'detail':detail, 'comment_form':comment_form, 'comment_reply_form':comment_reply_form})


# 댓글 
def comment_new(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.comment_name = request.user
        finished_form.save()
        
    return redirect('post_detail', post_id)


def commentreply(request, comment_id):
    form = CommentReplyForm(request.POST)
    if form.is_valid():
        finished = form.save(commit=False)
        finished.comment_reply = get_object_or_404(Comment, pk=comment_id)
        finished.comment_reply_name = request.user
        finished.save()
        
    return redirect('post_detail', post_id=finished.comment_reply.post.id)
    
    
    # comment_reply = get_object_or_404(Comment, pk=comment_id)
    # if request.method == "POST":
    #     form = CommentReplyForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.comment_reply = comment_reply
    #         comment.comment_reply_name = request.user
    #         comment.save()
    #         return redirect('post_detail', post_id=comment.comment_reply.post.id)
    # else:
    #     form = CommentReplyForm()
    # return render(request, 'post_detail.html', {'form': form})


    
    # form = CommentReplyForm(request.POST)
    # if form.is_valid():
    #     finished = form.save(commit=False)
    #     finished.comment_reply = get_object_or_404(Comment, pk=comment_id)
    #     finished.comment_reply_name = request.user
    #     finished.save()
        
    # return redirect('post_detail', comment_id=finished.post.id)



# 검색
def search(request):
        keyword = request.POST.get('searched', "") 
        if keyword:
            categories = Post.objects.all()
            posts = categories.filter(category__contains=keyword)
            return render(request, 'searched.html', {'posts':posts, 'keyword':keyword})
        else:
            return render(request, 'searched.html', {})

# 오늘 올라온 게시물의 수
def timesave(request):
    if request.method == 'POST':
        timesave = timesave()
        timesave.save_date = request.POST.get('time')
        timesave.date = DateFormat(datetime.now()).format('Ymd')
        timesave.save()
        return HttpResponse(content_type='appliction/json')

def count_content_view(request, today):
    today = DateFormat(datetime.now()).format('Ymd')
    content = Post.objects.order_by('created')
    content_count = content.exclude(deleted = True).filter(date = today).count()
    context = {
        'newcontent' : content,
        'content_count' : content_count,
    }
    
    return render(request, context=context)

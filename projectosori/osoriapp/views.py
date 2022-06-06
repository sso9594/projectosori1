from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import CommentForm, postform,Freepostform,FreeCommentForm
from .models import Post,FreePost

def home(request):
    posts = Post.objects.filter().order_by('-date')
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request,'index.html',{'posts':posts,'freeposts':freeposts})    

def annonyboard(request):

    posts = Post.objects.filter().order_by('-date')
    return render(request,'anonyboard.html',{'posts':posts})


def fashionboard(request):  
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request,'fashionboard.html',{'freeposts':freeposts})


def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('annoyboard')
    else:
        form=postform()
    return render(request,'post_form.html',{'form':form})    

def detail(request,post_id):
    post_detail=get_object_or_404(Post,pk=post_id)
    comment_form=CommentForm() 
    return render(request,'detail.html',{'post_detail':post_detail,'comment_form':comment_form})

def new_comment(request,post_id):
    filled_form=CommentForm(request.POST)
    if filled_form.is_valid:
        finished_form=filled_form.save(commit=False)
        finished_form.post=get_object_or_404(Post,pk=post_id)
        finished_form.save()
    return redirect('detail',post_id)

def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = Freepostform(request.POST, request.FILES)
        if form.is_valid():
            unfinished=form.save(commit=False)
            unfinished.author=request.user
            unfinished.save()
            return redirect('fashionboard')
    else:
        form=Freepostform()
    return render(request,'freepost_form.html',{'form':form})    

def freedetail(request,post_id):
    post_detail=get_object_or_404(FreePost,pk=post_id)
    comment_form=FreeCommentForm() 
    return render(request,'freedetail.html',{'post_detail':post_detail,'comment_form':comment_form})

def new_freecomment(request,post_id):
    filled_form=FreeCommentForm(request.POST)
    if filled_form.is_valid:
        finished_form=filled_form.save(commit=False)
        finished_form.post=get_object_or_404(FreePost,pk=post_id)
        finished_form.save()
    return redirect('freedetail',post_id)

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')


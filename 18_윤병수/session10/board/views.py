from datetime import time
import board
from account.models import User
from board.models import Board
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.
def new(request):
    return render(request)

def create(request):
    if request.method == "POST":
        # 모델에 있는 메소드를 모두 써야한다.
        new_board = Board()
        new_board.title = request.POST['title']
        new_board.body = request.POST['body']
        new_board.pub_date = timezone.datetime.now()
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        new_board.author = user
        new_board.save()
        return redirect('home')
    else :
        # 그냥 페이지 이동
        return render(request, 'new.html')

def home(request) :
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards' : boards})

def detail(request, id):
    board = get_object_or_404(Board, pk = id)
    return render(request, 'detail.html', {'board':board})

def edit(request, id) :
    if request.method == "POST" :
        edit_board = Board.objects.get(id = id)
        edit_board.title = request.POST["title"]
        edit_board.body = request.POST["body"]
        edit_board.save()
        return redirect('detail', edit_board.id)
    else:
        board = Board.objects.get(id = id)
        return render(request, 'edit.html', {'board': board})

def delete(request, id) :
    delete_board = Board.objects.get(id = id)
    delete_board.delete()
    return redirect('home')

# Commnet 기능 

def create_comment (request, board_id) : 
    if request.method == "POST" :
        new_comment = Comment()
        # 어떤 게시글에 올라가는지. 
        new_comment.board = get_object_or_404(Board, pk = board_id)
        # 유저 가져오기 
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        new_comment.writer = user
        # 내용 저장 
        new_comment.content = request.POST['content']
        # 작성 시간 저장 
        new_comment.date = timezone.datetime.now()
        # db 에 댓글 객체 저장 
        new_comment.save()
        return redirect('detail', board_id)

def delete_comment (request, board_id, comment_id) :
     this_comment = Comment.objects.get(pk = comment_id)
     this_comment.delete()
     return redirect('detail', board_id)
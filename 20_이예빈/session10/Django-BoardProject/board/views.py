from django.shortcuts import render
import board
from account.models import User
from django.utils import timezone
from board.models import Board
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def create(request):
    # 글을 작성할 경우 POST 방식
    if request.method == "POST":
        new_board=Board()
        new_board.title=request.POST['title']
        new_board.body=request.POST['body']
        new_board.pub_date=timezone.datetime.now()
        
        # 글을 작성한(로그인한 user의 id) user의 id를 user_id 변수에 저장
        user_id=request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값을 저장
        user = User.objects.get(id=user_id)
        # 작성자 = user
        new_board.author=user
        # db에 생성된 board 객체 저장
        new_board.save()
        return redirect('home')
    
    # 단순 create 페이지로 이동할 경우 GET 방식으로 들어감
    else:
        return render(request, 'new.html')

def home(request):
    board=Board.objects.all()
    return render(request, 'home.html', {'board':board})

def detail(request, id):
    board=get_object_or_404(Board, pk=id)
    return render(request, 'detail.html', {'board':board})

def edit(request, id):
    if request.method=="POST":
        edit_board=Board.objects.get(id=id)
        edit_board.title=request.POST['title']
        edit_board.body=request.POST['body']
        edit_board.save()
        return redirect('detail', edit_board.id)
    else:
        board=Board.objects.get(id=id)
        return render(request, 'edit.html', {'board':board})
    
def delete(request,id):
    delete_board=Board.objects.get(id=id)
    delete_board.delete()
    return redirect('home')


# ----- comment -----

def create_comment(request, board_id):
    if request.method == 'POST':
        new_comment=Comment()
        new_comment.board=get_object_or_404(Board, pk=board_id)
        
        # 댓글을 작성한(로그인한 user의 id) user의 id를 user_id 변수에 저장
        user_id=request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값을 저장
        user = User.objects.get(id=user_id)
        # comment 작성자 = user
        new_comment.writer=user
        
        new_comment.content=request.POST['content']
        new_comment.created_at=timezone.datetime.now()
        
        # db에 생성된 comment 객체 저장
        new_comment.save()
        return redirect('detail', board_id)

def delete_comment(request, board_id, comment_id):
    this_comment=Comment.objects.get(pk=comment_id)
    this_comment.delete()
    return redirect('detail', board_id)
import board
from account.models import User
from django.utils import timezone
from board.models import Board
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})
    
def create(request) : 
    # 글을 작성할 경우 POST 방식으로 들어가 아래의 코드 실행. 
    if request.method == "POST" : 
        new_board = Board()
        new_board.title = request.POST['title']
        new_board.body = request.POST['body']
        new_board.pub_date = timezone.datetime.now()
        # 글을 작성한( 로그인 한 user 의 id ) user의 id 를 user_id 변수에 저장합니다. 
        user_id = request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값. 즉 글 작성자의 user 객체를 user 변수에 저장합니다. 
        user = User.objects.get(id = user_id)
        # 작성자 = user 가 됩니다. 
        new_board.author = user
        # db 에 생성된 board 객체를 저장합니다. 
        new_board.save()
        return redirect('home')
    # 단순 create 페이지로 이동할 경우 GET 방식으로 들어가 아래의 코드 실행. 
    else : 
        return render(request, 'new.html')

def detail(request, id):
    board = get_object_or_404(Board, pk = id)
    return render(request, 'detail.html', {'board':board})

def edit(request, id):
    if request.method == "POST":
        edit_board = Board.objects.get(id = id)
        edit_board.title = request.POST["title"]
        edit_board.body = request.POST["body"]
        edit_board.save()
        return redirect('detail', edit_board.id)
    else:
        board = Board.objects.get(id = id)
        return render(request, 'edit.html', {'board':board})

def delete(request, id):
    delete_board = Board.objects.get(id = id)
    delete_board.delete()
    return redirect('home')

## comment ##
def c_comment(request, board_id):
    if request.method == 'POST':
        comment = Comment()
        comment.board = get_object_or_404(Board, pk= board_id)
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        comment.author = user
        comment.content = request.POST['content']
        comment.created_at = timezone.datetime.now()
        comment.save()
        return redirect('detail', board_id)

def d_comment(request, board_id, comment_id):
    comments = Comment.objects.get(pk=comment_id)
    comments.delete()
    return redirect('detail', board_id)
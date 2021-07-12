from django.shortcuts import render, redirect, get_object_or_404
import board
from account.models import User
from django.utils import timezone
from board.models import Board
from .models import *

# Create your views here.
def home(request) :
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards' : boards})

def create(request) :
    if request.method == "POST":
        new_board = Board()
        new_board.title = request.POST["title"]
        new_board.body = request.POST["body"]
        new_board.pub_date = timezone.datetime.now()

        user_id = request.user.id

        user = User.objects.get(id = user_id)

        new_board.author = user

        new_board.save()
        return redirect('home')

    else :
        return render(request, 'new.html')


def detail(request, id) :
    board = get_object_or_404(Board, pk = id)
    return render (request, 'detail.html', {'board' : board})


def edit(request, id) :
    if request.method == "POST" :
        edit_board = Board.objects.get(id = id)
        edit_board.title = request.POST["title"]
        edit_board.body = request.POST["body"]
        edit_board.save()
        return redirect('detail', edit_board.id)
    else :
        board = Board.objects.get(id = id)
        return render(request, 'edit.html', {'board' : board})


def delete(request, id) :
    delete_board = Board.objects.get(id = id)
    delete_board.delete()
    return redirect('home')


''' Comment '''
def create_comment(request, board_id):
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.board = get_object_or_404(Board, pk = board_id)
        new_comment.content = request.POST['content']
        new_comment.created_at = timezone.datetime.now()

        user_id = request.user.id

        user = User.objects.get(id = user_id)

        new_comment.author = user

        new_comment.save()
        return redirect('detail', board_id)

def delete_comment(request, board_id, comment_id) :
    delete_comment = Comment.objects.get(pk = comment_id)
    delete_comment.delete()
    return redirect('detail', board_id)
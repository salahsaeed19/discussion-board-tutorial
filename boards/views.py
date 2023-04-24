# from django.shortcuts import render, HttpResponse
from .models import Board, Post, Topic
from django.http import HttpResponse


def home(request):
    boards = Board.objects.all()
    boards_name = []
    for board in boards:
        boards_name.append(board.name)
    response_html = "<br>".join(boards_name)
    return HttpResponse(response_html)
    # return HttpResponse("<b>Salah is Backend developer with python django #</b>")




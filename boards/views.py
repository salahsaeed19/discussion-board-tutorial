from django.shortcuts import render, HttpResponse
from .models import Board, Post, Topic


def home(request):

    boards = Board.objects.all()
    return render(request, "home.html", {'boards': boards})




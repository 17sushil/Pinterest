from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm

@login_required
def board_list(request):
    boards = Board.objects.filter(user=request.user)
    return render(request, 'boards/board_list.html', {'boards': boards})

def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    pins = board.pins.all()
    if board.is_private and board.user != request.user:
         return redirect('core:home')
    return render(request, 'boards/board_detail.html', {'board': board, 'pins': pins})

@login_required
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('boards:board_detail', board_id=board.id)
    else:
        form = BoardForm()
    return render(request, 'boards/board_form.html', {'form': form})

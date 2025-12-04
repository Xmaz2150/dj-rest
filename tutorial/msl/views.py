from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    selected_players = []
    
    if request.method == 'POST':
        selected_players = request.POST.getlist('selected_players')
    
    context = {
        'players': [
            "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace",
            "Hannah", "Isaac", "Jack", "Kathy", "Liam", "Mona", "Nina", "Oscar"
        ],
        'selected_players': selected_players
    }

    return render(request, 'index.html', context)

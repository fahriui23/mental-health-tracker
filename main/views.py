from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306212096',
        'name': 'Fahri',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
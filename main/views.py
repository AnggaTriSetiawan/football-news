from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406350614',
        'name': 'Angga Tri Setiawan',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)

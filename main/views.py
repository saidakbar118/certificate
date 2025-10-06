from django.shortcuts import render


def detail_view(request, pk):
    return render(request, "detail.html", {"pk": pk})

def index_view(request):
    return render(request, "index.html")
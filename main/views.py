from django.shortcuts import render


def detail_view(request, pk):
    return render(request, "detail.html", {"pk": pk})
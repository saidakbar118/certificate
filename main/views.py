from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # 🔹 qo‘shamiz
from .models import Certificate


def index_view(request):
    """Bosh sahifa — qidiruv formasi bilan"""
    return render(request, "index.html")


def search_view(request):
    """Qidiruv logikasi"""
    cert_number = request.GET.get("certificate")
    passport_series = request.GET.get("series")
    passport_number = request.GET.get("number")

    if not (cert_number and passport_series and passport_number):
        messages.error(request, "❗ Barcha maydonlarni to‘ldiring!")
        return redirect("index_view")

    try:
        certificate = Certificate.objects.get(
            certificate_number__iexact=cert_number.strip(),
            passport_series__iexact=passport_series.strip(),
            passport_number__iexact=passport_number.strip()
        )
        return redirect("detail_view", pk=certificate.pk)
    except Certificate.DoesNotExist:
        messages.error(request, "❌ Sertifikat topilmadi!")
        return redirect("index_view")


def detail_view(request, pk):
    """Sertifikat rasmi chiqadigan sahifa"""
    certificate = get_object_or_404(Certificate, pk=pk)
    return render(request, "detail.html", {"certificate": certificate})

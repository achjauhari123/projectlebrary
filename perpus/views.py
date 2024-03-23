from django.shortcuts import render

# Create your views here.
def buku(request):
    judul = ["Belajar Django", "Belajar bahasa inggris", "Belajar ips"]
    penulis = "ach jauhari"

    konteks = {
        'title': judul,
        'penulis': penulis,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return HttpResponse('<h1>Halaman Penerbit</h1>')
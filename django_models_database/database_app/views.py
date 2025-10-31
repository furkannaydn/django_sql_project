from django.shortcuts import render
from .import models

# English: Create your views here.
# Türkçe: View'larınızı (görünümlerinizi) burada oluşturun.

# English: This view fetches all Musician objects from the database and sends them to the index.html template.
# Türkçe: Bu view, veritabanındaki tüm Musician nesnelerini çeker ve bunları index.html şablonuna gönderir.
def index(request):
    # English: Get all records from the Musician model.
    # Türkçe: Musician modelinden tüm kayıtları al.
    musicians_data = models.Musician.objects.all()
    # English: Create a context dictionary to pass the data to the template.
    # Türkçe: Veriyi şablona göndermek için bir context sözlüğü oluştur.
    musicians_context = {'musicians': musicians_data}
    return render(request, 'database_app/index.html',context=musicians_context)
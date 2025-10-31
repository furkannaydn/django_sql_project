# django_sql_project

Django project with raw SQL usage examples

---

## Common Commands / Sık Kullanılan Komutlar

Here are some common commands used in a Django project.

Aşağıda bir Django projesinde kullanılan bazı yaygın komutlar yer almaktadır.

### English

1.  **Create database migrations:**
    ```bash
    python manage.py makemigrations
    ```
    *This command creates new migration files based on the changes you've made to your models.*

2.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
    *This command applies the migrations to the database, creating or updating the database schema.*

3.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    *This command starts the development server, usually accessible at `http://127.0.0.1:8000/`.*

4.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```
    *This command creates an admin user who can access the Django admin site.*

### Türkçe

1.  **Veritabanı göçlerini (migration) oluşturma:**
    ```bash
    python manage.py makemigrations
    ```
    *Bu komut, modellerinizde yaptığınız değişikliklere göre yeni göç dosyaları oluşturur.*

2.  **Veritabanı göçlerini uygulama:**
    ```bash
    python manage.py migrate
    ```
    *Bu komut, göçleri veritabanına uygulayarak veritabanı şemasını oluşturur veya günceller.*

3.  **Geliştirme sunucusunu çalıştırma:**
    ```bash
    python manage.py runserver
    ```
    *Bu komut, genellikle `http://127.0.0.1:8000/` adresinden erişilebilen geliştirme sunucusunu başlatır.*

4.  **Süper kullanıcı (admin) oluşturma:**
    ```bash
    python manage.py createsuperuser
    ```
    *Bu komut, Django yönetim paneline erişebilecek bir yönetici kullanıcısı oluşturur.*

---

## Django Shell (ORM) Examples / Django Shell (ORM) Örnekleri

Here are some ORM query examples run in the Django shell.

Aşağıda Django shell'de çalıştırılan bazı ORM sorgu örnekleri yer almaktadır.

### English

1.  **Start the Django shell:**
    ```bash
    python manage.py shell
    ```

2.  **Import a model:**
    ```python
    from database_app.models import Musician
    ```

3.  **Get all objects:**
    ```python
    Musician.objects.all()
    ```

4.  **Get a single object by primary key (pk):**
    ```python
    Musician.objects.get(pk=1)
    ```

5.  **Create a new object:**
    ```python
    Musician.objects.create(name="Alice", instrument="Violin", age=29)
    ```

6.  **Filter objects:**
    ```python
    # Get all musicians who play the guitar
    Musician.objects.filter(instrument="guitar").all()
    ```

7.  **Filter with complex lookups (Q objects):**
    ```python
    from django.db.models import Q
    # Get musicians who play the guitar OR are older than 30
    Musician.objects.filter(Q(instrument="guitar") | Q(age__gt=30)).all()
    ```

8.  **Filter using field lookups:**
    ```python
    # Get musicians whose name starts with 'j' (case-sensitive)
    Musician.objects.filter(name__startswith="j").all()
    ```

9.  **Filter using `in` lookup:**
    ```python
    # Get musicians whose age is in the given list
    Musician.objects.filter(age__in=[27, 34, 41]).all()
    ```

10. **Filter using `gte` (greater than or equal to):**
    ```python
    # Get musicians who are 60 years old or older
    Musician.objects.filter(age__gte=60).all()
    ```

11. **Filter using `endswith` (case-sensitive and insensitive):**
    ```python
    # Get musicians whose name ends with 's' (case-sensitive)
    Musician.objects.filter(name__endswith="s").all()
    # Get musicians whose name ends with 'S' or 's' (case-insensitive)
    Musician.objects.filter(name__iendswith="s").all()
    ```

12. **Update an object:**
    ```python
    # Get the record with pk=5
    myrecord = Musician.objects.get(pk=5)
    # Change the name
    myrecord.name = "jack nick"
    # Save the changes to the database
    myrecord.save()
    ```

13. **Delete an object:**
    ```python
    # Get the record with pk=4 and delete it
    jhon = Musician.objects.get(pk=4)
    jhon.delete()
    ```

### Türkçe

1.  **Django shell'i başlatma:**
    ```bash
    python manage.py shell
    ```

2.  **Modeli içeri aktarma:**
    ```python
    from database_app.models import Musician
    ```

3.  **Tüm nesneleri getirme:**
    ```python
    Musician.objects.all()
    ```

4.  **Birincil anahtar (pk) ile tek bir nesne getirme:**
    ```python
    Musician.objects.get(pk=1)
    ```

5.  **Yeni bir nesne oluşturma:**
    ```python
    Musician.objects.create(name="Alice", instrument="Violin", age=29)
    ```

6.  **Nesneleri filtreleme:**
    ```python
    # Gitar çalan tüm müzisyenleri getir
    Musician.objects.filter(instrument="guitar").all()
    ```

7.  **Karmaşık sorgularla filtreleme (Q nesneleri):**
    ```python
    from django.db.models import Q
    # Gitar çalan VEYA 30 yaşından büyük olan müzisyenleri getir
    Musician.objects.filter(Q(instrument="guitar") | Q(age__gt=30)).all()
    ```

8.  **Alan sorgularını kullanarak filtreleme:**
    ```python
    # Adı 'j' ile başlayan müzisyenleri getir (büyük/küçük harfe duyarlı)
    Musician.objects.filter(name__startswith="j").all()
    ```

9.  **`in` sorgusunu kullanarak filtreleme:**
    ```python
    # Yaşı verilen listedeki değerlerden biri olan müzisyenleri getir
    Musician.objects.filter(age__in=[27, 34, 41]).all()
    ```

10. **`gte` (büyük veya eşit) ile filtreleme:**
    ```python
    # 60 yaşında veya daha büyük olan müzisyenleri getir
    Musician.objects.filter(age__gte=60).all()
    ```

11. **`endswith` (büyük/küçük harfe duyarlı ve duyarsız) ile filtreleme:**
    ```python
    # Adı 's' ile biten müzisyenleri getir (büyük/küçük harfe duyarlı)
    Musician.objects.filter(name__endswith="s").all()
    # Adı 'S' veya 's' ile biten müzisyenleri getir (büyük/küçük harfe duyarsız)
    Musician.objects.filter(name__iendswith="s").all()
    ```

12. **Bir nesneyi güncelleme:**
    ```python
    # pk=5 olan kaydı getir
    myrecord = Musician.objects.get(pk=5)
    # İsmi değiştir
    myrecord.name = "jack nick"
    # Değişiklikleri veritabanına kaydet
    myrecord.save()
    ```

13. **Bir nesneyi silme:**
    ```python
    # pk=4 olan kaydı getir ve sil
    jhon = Musician.objects.get(pk=4)
    jhon.delete()
    ```
---


## Field Lookups Reference / Alan Sorguları Referansı

A reference for common field lookups used in Django's ORM `filter()` method.

Django ORM'in `filter()` metodunda kullanılan yaygın alan sorguları için bir referans.

| Keyword / Anahtar Kelime | Description / Açıklama |
| :--- | :--- |
| `contains` | Contains the phrase |
| `icontains` | Same as `contains`, but case-insensitive |
| `date` | Matches a date |
| `day` | Matches a date (day of month, 1-31) (for dates) |
| `endswith` | Ends with |
| `iendswith` | Same as `endswith`, but case-insensitive |
| `exact` | An exact match |
| `iexact` | Same as `exact`, but case-insensitive |
| `in` | Matches one of the values |
| `isnull` | Matches `NULL` values |
| `gt` | Greater than |
| `gte` | Greater than, or equal to |
| `hour` | Matches an hour (for datetimes) |
| `lt` | Less than |
| `lte` | Less than, or equal to |
| `minute` | Matches a minute (for datetimes) |
| `month` | Matches a month (for dates) |
| `quarter` | Matches a quarter of the year (1-4) (for dates) |
| `range` | Match between |
| `regex` | Matches a regular expression |
| `iregex` | Same as `regex`, but case-insensitive |
| `second` | Matches a second (for datetimes) |
| `startswith` | Starts with |
| `istartswith` | Same as `startswith`, but case-insensitive |
| `time` | Matches a time (for datetimes) |
| `week` | Matches a week number (1-53) (for dates) |
| `week_day` | Matches a day of week (1-7) where 1 is Sunday |
| `iso_week_day` | Matches an ISO 8601 day of week (1-7) where 1 is Monday |
| `year` | Matches a year (for dates) |
| `iso_year` | Matches an ISO 8601 year (for dates) |
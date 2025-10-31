from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
# English: Here you define the data models for your application.
# Türkçe: Uygulamanız için veri modellerini burada tanımlarsınız.


# English: Represents a musician with their name, instrument, and age.
# Türkçe: Bir müzisyeni adı, enstrümanı ve yaşı ile temsil eder.
class Musician(models.Model):
    # English: The name of the musician. Max length is 100 characters.
    # Türkçe: Müzisyenin adı. Maksimum uzunluk 100 karakterdir.
    name=models.CharField(max_length=100)

    # English: The instrument the musician plays. Max length is 40 characters.
    # Türkçe: Müzisyenin çaldığı enstrüman. Maksimum uzunluk 40 karakterdir.
    instrument=models.CharField(max_length=40)

    # English: The age of the musician. Must be between 0 and 120.
    # Türkçe: Müzisyenin yaşı. 0 ile 120 arasında olmalıdır.
    age=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])

    # English: The salary of the musician. Must be a positive value, defaults to 0.
    # Türkçe: Müzisyenin maaşı. Pozitif bir değer olmalıdır, varsayılan olarak 0'dır.
    salary=models.IntegerField(default=0,validators=[MinValueValidator(0)])

    # English: Returns a string representation of the Musician object, useful for the admin panel and debugging.
    # Türkçe: Musician nesnesinin bir dize temsilini döndürür, admin paneli ve hata ayıklama için kullanışlıdır.
    def __str__(self):
        return f"Name: {self.name}, Instrument: {self.instrument}, Age: {self.age}, Salary: {self.salary}"

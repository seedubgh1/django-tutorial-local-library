import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

import django
django.setup()

from catalog.models import Book, Genre
import random

books = Book.objects.all()

genres = [g.__str__() for g in Genre.objects.all()]
genres = [_ for _ in range(1,len(genres)+1)]

print('Genres:',genres)
for b in books:
    if not b.genre.all():
        b.genre = random.choice(genres)
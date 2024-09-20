import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

import django
django.setup()

from django.contrib.auth.models import User
from catalog.models import Author, Book, BookInstance, Genre, Language
import random

from faker import Faker
fake = Faker()

publishing_imprints = [
    "Penguin Random House",
    "HarperCollins",
    "Simon & Schuster",
    "Macmillan",
    "Hachette Livre",
    "Bloomsbury Publishing",
    "Oxford University Press",
    "Cambridge University Press",
    "Scholastic Corporation",
    "Wiley",
    "Pearson Education",
    "Elsevier",
    "Springer Nature",
    "MIT Press",
    "Houghton Mifflin Harcourt",
    "Random House",
    "Vintage Books",
    "Puffin Books",
    "Scribner",
    "Ballantine Books",
    "Little, Brown and Company",
    "Doubleday",
    "Knopf",
    "Pantheon Books",
    "Allen Lane",
    "Viking Press",
    "Faber and Faber",
    "Penguin Books",
    "Grove Press",
    "Bloomsbury USA",
]

genres = ['Fantasy', 'Science Fiction', 'Drama', 'Horror', 'Humor']

def generate_random_book_title():
    adjectives = ['Fantastic', 'Mysterious', 'Whimsical', 'Enchanting', 'Intriguing', 'Captivating', 'Bewitched', 'Curious', 'Surreal', 'Unforgettable']
    nouns = ['Adventure', 'Secrets', 'Journey', 'Dreams', 'Mist', 'Legacy', 'Whisper', 'Labyrinth', 'Echoes', 'Infinity']

    d_random_bk = {}
    
    d_random_bk['adjective'] = random.choice(adjectives)
    d_random_bk['noun'] = random.choice(nouns)
    d_random_bk['first_name'] = fake.first_name()
    d_random_bk['last_name'] = fake.last_name()
    d_random_bk['full_name'] = ' '.join([d_random_bk['first_name'],d_random_bk['last_name']])
    d_random_bk['title'] = f"The {d_random_bk['adjective']} {d_random_bk['noun']} of {d_random_bk['first_name']} {d_random_bk['last_name']}"
    d_random_bk['summary'] = f"{d_random_bk['full_name']} embarks on a thrilling adventure in '{d_random_bk['title']}', a mesmerizing tale that merges fantasy and reality.  Journey through the enchanting realms of magic and mystery as our protagonist uncovers the {d_random_bk['adjective'].lower()} {d_random_bk['noun'].lower()}.  Prepare to be captivated by a world where destiny intertwines with ancient prophecies and where nothing is as it seems."

    d_random_bk['isbn'] = fake.isbn13()

    return d_random_bk

def create_books(num_bks=1):
    
    for _ in range(num_bks):
        # Create a random author
        auth_nm = fake.name().split()
        author = Author.objects.create(
            first_name=f'{auth_nm[0]}',
            last_name=f'{auth_nm[1]}',
            date_of_birth=fake.date_of_birth(minimum_age=27,
                                             maximum_age=80).strftime('%Y-%m-%d')
        )

        # Create a book
        book_details = generate_random_book_title()
        
        book = Book.objects.create(
            title=f"{book_details['title']}",
            summary=f"{book_details['summary']}",
            isbn=f"{book_details['isbn']}",
            author=author,
            # genre = genre.set(random.choice(genres)),
            # genre = random.choice(Genre.objects.all()),
            language = random.choice(Language.objects.all())
        )

        book.genre.add(random.choice(Genre.objects.all()))

        # Create three book instances for each book
        pub_imp = random.choice(publishing_imprints)
        for i in range(3):
            BookInstance.objects.create(
                book=book,
                imprint=f'{pub_imp}-{i}',
                due_back=None,
                status='a',
            )

if __name__ == '__main__':
    create_books()
    print('Books created successfully!')

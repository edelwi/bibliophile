from datetime import date

from django.test import TestCase
from website.models import Genre
from website.models.author import Author
from website.models.book import Book
from website.models.work import Work

from website.tests.fixtures import create_book, create_genre, create_author, create_work


class GenreTestCase(TestCase):
    def setUp(self):
        create_genre(name="horror", comment="very scary")
        create_genre(name="adventure",)

    def test_genres(self):
        horror = Genre.objects.get(name="horror")
        adventure = Genre.objects.get(name="adventure")
        self.assertEqual(horror.comment, "very scary")
        self.assertIsNone(adventure.comment)
        self.assertEqual(str(horror), "horror")


class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(name="unknown")
        create_author()

    def test_authors(self):
        unknown = Author.objects.get(name="unknown")
        hemingway = Author.objects.get(name="Ernest Miller Hemingway")

        self.assertEqual(unknown.name, "unknown")
        self.assertEqual(hemingway.name, "Ernest Miller Hemingway")

        self.assertIsNone(unknown.birth_date)
        self.assertEqual(hemingway.birth_date, date(1899, 7, 21))

        self.assertIsNone(unknown.death_date)
        self.assertEqual(hemingway.death_date, date(1961, 7, 2))

        self.assertIsNone(unknown.comment)
        self.assertEqual(
            hemingway.comment,
            "американский писатель, военный корреспондент, "
            "лауреат Нобелевской премии по литературе 1954 года",
        )

        self.assertIsNone(unknown.biography)
        self.assertEqual(
            hemingway.biography,
            "Эрнест Хемингуэй родился 21 июля 1899 года в привилегированном "
            "пригороде Чикаго — "
            "деревне Ок-Парк (Иллинойс, США). Его отец Кларенс Эдмонт Хемингуэй (1871—1928) был "
            "врачом, а мать, Грейс Эрнестин Холл-Хемингуэй (1872—1951) — оперной певицей. Родители оба "
            "получили хорошее образование и в консервативной общине Ок-Парка пользовались отличной "
            "репутацией.",
        )

        self.assertEqual(str(hemingway), "Ernest Miller Hemingway")


class WorkTestCase(TestCase):
    def setUp(self):
        hemingway = create_author()
        adventure = create_genre(
            name="adventure",
        )
        old_man_and_sea = create_work(genre=adventure)
        old_man_and_sea.authors.set([hemingway])

    def test_works(self):
        old_man = Work.objects.get(title="The Old Man and the Sea")
        self.assertEqual(old_man.title, "The Old Man and the Sea")
        self.assertEqual(str(old_man), "The Old Man and the Sea")


class BookTestCase(TestCase):
    def setUp(self):
        create_book()

    def test_books(self):
        old_man = Book.objects.get(title="The Old Man and the Sea")
        self.assertEqual(old_man.title, "The Old Man and the Sea")
        self.assertEqual(str(old_man), "The Old Man and the Sea")

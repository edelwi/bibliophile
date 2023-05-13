from datetime import date

from django.test import TestCase
from website.models import Genre
from website.models.author import Author
from website.models.book import Book
from website.models.work import Work


class GenreTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(name="horror", comment="very scary")
        Genre.objects.create(
            name="adventure",
        )

    def test_genres(self):
        horror = Genre.objects.get(name="horror")
        adventure = Genre.objects.get(name="adventure")
        self.assertEqual(horror.comment, "very scary")
        self.assertIsNone(adventure.comment)
        self.assertEqual(str(horror), "horror")


class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(name="unknown")
        Author.objects.create(
            name="Ernest Miller Hemingway",
            birth_date="1899-07-21",
            death_date="1961-07-02",
            comment="американский писатель, военный корреспондент, лауреат Нобелевской премии по литературе 1954 года",
            biography="Эрнест Хемингуэй родился 21 июля 1899 года в привилегированном пригороде Чикаго — "
            "деревне Ок-Парк (Иллинойс, США)[3]. Его отец Кларенс Эдмонт Хемингуэй (1871—1928) был "
            "врачом, а мать, Грейс Эрнестин Холл-Хемингуэй (1872—1951) — оперной певицей. Родители оба "
            "получили хорошее образование и в консервативной общине Ок-Парка пользовались отличной "
            "репутацией.",
        )

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
            "деревне Ок-Парк (Иллинойс, США)[3]. Его отец Кларенс Эдмонт Хемингуэй (1871—1928) был "
            "врачом, а мать, Грейс Эрнестин Холл-Хемингуэй (1872—1951) — оперной певицей. Родители оба "
            "получили хорошее образование и в консервативной общине Ок-Парка пользовались отличной "
            "репутацией.",
        )

        self.assertEqual(str(hemingway), "Ernest Miller Hemingway")


class WorkTestCase(TestCase):
    def setUp(self):
        hemingway = Author.objects.create(
            name="Ernest Miller Hemingway",
            birth_date="1899-07-21",
            death_date="1961-07-02",
            comment="американский писатель, военный корреспондент, лауреат Нобелевской премии по литературе 1954 года",
            biography="Эрнест Хемингуэй родился 21 июля 1899 года в привилегированном пригороде Чикаго — "
            "деревне Ок-Парк (Иллинойс, США). Его отец Кларенс Эдмонт Хемингуэй (1871—1928) был "
            "врачом, а мать, Грейс Эрнестин Холл-Хемингуэй (1872—1951) — оперной певицей. Родители оба "
            "получили хорошее образование и в консервативной общине Ок-Парка пользовались отличной "
            "репутацией.",
        )
        adventure = Genre.objects.create(
            name="adventure",
        )
        old_man_and_sea = Work.objects.create(
            title="The Old Man and the Sea",
            publication_date="1952-09-01",
            genre=adventure,
            summary="повесть американского писателя Эрнеста Хемингуэя, написанная в Бимини "
            "(Багамские острова) и вышедшая в 1952 году. Последнее известное "
            "художественное произведение Хемингуэя, опубликованное при его жизни. "
            "Рассказывает историю старика Сантьяго, кубинского рыбака, о его борьбе "
            "в открытом море с гигантским марлином, который стал самой большой "
            "добычей в его жизни.",
            comment="чувствуется рука мастера",
        )
        old_man_and_sea.authors.set([hemingway])

    def test_works(self):
        old_man = Work.objects.get(title="The Old Man and the Sea")
        self.assertEqual(old_man.title, "The Old Man and the Sea")
        self.assertEqual(str(old_man), "The Old Man and the Sea")


"""    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=1000, null=True, blank=True)
    isbn = models.CharField("ISBN", max_length=20, null=True, blank=True)
    media_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=PAPER)
    pages_number = models.IntegerField("number of pages", null=True, blank=True)
    publishing_year = models.IntegerField("the year of publishing", null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    translator = models.CharField(max_length=100, null=True, blank=True)
    works = models.ManyToManyField(Work)
    publisher = models.CharField("publishing house", max_length=200, null=True, blank=True)"""


class BookTestCase(TestCase):
    def setUp(self):
        hemingway = Author.objects.create(
            name="Ernest Miller Hemingway",
            birth_date="1899-07-21",
            death_date="1961-07-02",
            comment="американский писатель, военный корреспондент, лауреат Нобелевской премии по литературе 1954 года",
            biography="Эрнест Хемингуэй родился 21 июля 1899 года в привилегированном пригороде Чикаго — "
            "деревне Ок-Парк (Иллинойс, США). Его отец Кларенс Эдмонт Хемингуэй (1871—1928) был "
            "врачом, а мать, Грейс Эрнестин Холл-Хемингуэй (1872—1951) — оперной певицей. Родители оба "
            "получили хорошее образование и в консервативной общине Ок-Парка пользовались отличной "
            "репутацией.",
        )
        adventure = Genre.objects.create(
            name="adventure",
        )
        old_man_and_sea = Work.objects.create(
            title="The Old Man and the Sea",
            publication_date="1952-09-01",
            genre=adventure,
            summary="повесть американского писателя Эрнеста Хемингуэя, написанная в Бимини "
            "(Багамские острова) и вышедшая в 1952 году. Последнее известное "
            "художественное произведение Хемингуэя, опубликованное при его жизни. "
            "Рассказывает историю старика Сантьяго, кубинского рыбака, о его борьбе "
            "в открытом море с гигантским марлином, который стал самой большой "
            "добычей в его жизни.",
            comment="чувствуется рука мастера",
        )
        old_man_and_sea.authors.set([hemingway])

        old_man_book = Book.objects.create(
            title="The Old Man and the Sea",
            isbn="no idea",
            pages_number=55,  # no idea too
            publishing_year=1952,
            comment="опубликовали на страницах журнала «Life» 1 сентября 1952 года. "
            "Пять миллионов экземпляров журнала были распроданы за два дня.",
            description="Книжная версия также вышла 1 сентября 1952 года, она имела тираж 50 000 "
            "экземпляров и содержала чёрно-белые иллюстрации Чарльза Танниклиффа и Реймонда Шеппарда.",
            publisher="Charles Scribner's Sons",
        )
        old_man_book.works.set([old_man_and_sea])

    def test_books(self):
        old_man = Book.objects.get(title="The Old Man and the Sea")
        self.assertEqual(old_man.title, "The Old Man and the Sea")
        self.assertEqual(str(old_man), "The Old Man and the Sea")

from django.test import TestCase
from django.urls import reverse

from website.tests.fixtures import create_genre, create_author, create_work, create_book


class GenresViewTests(TestCase):
    def test_no_genres(self):
        response = self.client.get(reverse("genre-list"))
        self.assertEqual(response.status_code, 200)
        # print(f"{response=} {response.context=}")
        self.assertContains(response, "")
        self.assertQuerySetEqual(response.context["object_list"], [])

    def test_genres(self):
        genre1 = create_genre(name="adventure", comment=None)
        response = self.client.get(reverse("genre-list"))
        self.assertQuerySetEqual(
            response.context["object_list"],
            [
                genre1,
            ],
        )


class AuthorsViewTests(TestCase):
    def test_no_authors(self):
        response = self.client.get(reverse("author-list"))
        self.assertEqual(response.status_code, 200)
        # print(f"{response=} {response.context=}")
        self.assertContains(response, "")
        self.assertQuerySetEqual(response.context["object_list"], [])

    def test_authors(self):
        author = create_author()
        response = self.client.get(reverse("author-list"))
        self.assertQuerySetEqual(
            response.context["object_list"],
            [
                author,
            ],
        )

    def test_author_detail(self):
        author = create_author()
        response = self.client.get(reverse("author-detail", kwargs={"pk": author.pk}))
        self.assertContains(response, author.name)
        self.assertContains(response, author.biography)


class WorkViewTests(TestCase):
    def setUp(self) -> None:
        self.hemingway = create_author()
        self.adventure = create_genre("adventure")
        self.old_man_and_sea = create_work(genre=self.adventure)
        self.old_man_and_sea.authors.set([self.hemingway])

    def test_author_works(self):
        response = self.client.get(
            reverse("work-author-list", kwargs={"pk": self.hemingway.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context["object_list"],
            [
                self.old_man_and_sea,
            ],
        )

    def test_genre_works(self):
        response = self.client.get(
            reverse("work-genre-list", kwargs={"pk": self.adventure.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context["object_list"],
            [
                self.old_man_and_sea,
            ],
        )

    def test_work_detail(self):
        response = self.client.get(
            reverse("work-detail", kwargs={"pk": self.old_man_and_sea.pk})
        )
        self.assertContains(response, self.old_man_and_sea.title)
        self.assertContains(response, self.old_man_and_sea.summary)


class BookViewTests(TestCase):

    def test_no_books(self):
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
        self.assertQuerySetEqual(response.context["object_list"], [])

    def test_books(self):
        book = create_book()
        response = self.client.get(reverse("book-list"))
        self.assertQuerySetEqual(
            response.context["object_list"],
            [
                book,
            ],
        )

    def test_book_detail(self):
        book = create_book()
        response = self.client.get(
            reverse("book-detail", kwargs={"pk": book.pk})
        )
        self.assertContains(response, book.title)
        self.assertContains(response, book.media_type)

from website.models.author import Author
from website.models.book import Book
from website.models.genre import Genre
from website.models.work import Work


def create_genre(name="adventure", comment=None):
    return Genre.objects.create(name=name, comment=comment)

def create_author():
    return Author.objects.create(
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

def create_work(genre):
    return Work.objects.create(
        title="The Old Man and the Sea",
        publication_date="1952-09-01",
        genre=genre,
        summary="повесть американского писателя Эрнеста Хемингуэя, написанная в Бимини "
                "(Багамские острова) и вышедшая в 1952 году. Последнее известное "
                "художественное произведение Хемингуэя, опубликованное при его жизни. "
                "Рассказывает историю старика Сантьяго, кубинского рыбака, о его борьбе "
                "в открытом море с гигантским марлином, который стал самой большой "
                "добычей в его жизни.",
        comment="чувствуется рука мастера",
    )

def create_book():
    hemingway = create_author()
    adventure = create_genre("adventure")
    old_man_and_sea = create_work(genre=adventure)
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
    return old_man_book
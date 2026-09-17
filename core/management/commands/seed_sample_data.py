from django.core.management.base import BaseCommand

from core.models import Author, AuthorProfile, Book


class Command(BaseCommand):
    help = "Create the sample Authors, Profiles, Books, and co-author relationships."

    def handle(self, *args, **options):
        AuthorProfile.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()

        author_data = [
            ("Ursula K. Le Guin", "ursula@example.com", "https://ursulakleguin.com"),
            ("Octavia E. Butler", "octavia@example.com", "https://www.octaviabutler.com"),
            ("Susanna Clarke", "susanna@example.com", "https://susannaclarke.co.uk"),
            ("Neil Gaiman", "neil@example.com", "https://neilgaiman.com"),
            ("Terry Pratchett", "terry@example.com", "https://terrypratchett.com"),
        ]
        authors = {}
        for name, email, website in author_data:
            author = Author.objects.create(name=name, email=email)
            AuthorProfile.objects.create(
                author=author,
                website=website,
                bio=f"A sample profile for {name}.",
            )
            authors[name] = author

        books = [
            ("The Left Hand of Darkness", 1969, "Ursula K. Le Guin", []),
            ("The Dispossessed", 1974, "Ursula K. Le Guin", []),
            ("Kindred", 1979, "Octavia E. Butler", []),
            ("Parable of the Sower", 1993, "Octavia E. Butler", []),
            ("Piranesi", 2020, "Susanna Clarke", []),
            ("Good Omens", 1990, "Neil Gaiman", ["Terry Pratchett"]),
        ]
        for title, year, author_name, co_author_names in books:
            book = Book.objects.create(
                title=title,
                published_year=year,
                author=authors[author_name],
            )
            book.co_authors.set(
                [authors[name] for name in co_author_names]
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {Author.objects.count()} authors and {Book.objects.count()} books."
            )
        )

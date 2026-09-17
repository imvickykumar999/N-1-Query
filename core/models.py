from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile for {self.author.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.PositiveIntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
    )
    co_authors = models.ManyToManyField(
        Author,
        related_name="coauthored_books",
        blank=True,
    )

    def __str__(self):
        return self.title

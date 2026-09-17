from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection

from .models import Author, Book


def home(request):
    """Render the lesson with live data loaded using eager relationships."""
    books = list(
        Book.objects.select_related("author")
        .prefetch_related("co_authors")
        .order_by("title")
    )
    authors = list(
        Author.objects.select_related("profile")
        .prefetch_related("books")
        .order_by("name")
    )
    return render(
        request,
        "index.html",
        {
            "books": books,
            "authors": authors,
            "book_count": len(books),
            "author_count": len(authors),
        },
    )


def sample_data(request):
    """Return live SQLite data and query counts for quick API inspection."""
    query_count_before = len(connection.queries)
    books = Book.objects.select_related("author").prefetch_related("co_authors")
    payload = [
        {
            "title": book.title,
            "author": book.author.name,
            "co_authors": [author.name for author in book.co_authors.all()],
        }
        for book in books
    ]
    return JsonResponse(
        {
            "database": "SQLite",
            "book_count": len(payload),
            "queries_used": len(connection.queries) - query_count_before,
            "books": payload,
        }
    )

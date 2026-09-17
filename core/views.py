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


def run_query(request):
    """Run one of the safe, predefined ORM lessons for the browser console."""
    example = request.GET.get("example", "foreign")
    query_count_before = len(connection.queries)

    if example == "foreign":
        rows = [
            f"{book.title} by {book.author.name}"
            for book in Book.objects.select_related("author").order_by("title")
        ]
        strategy = 'Book.objects.select_related("author")'
    elif example == "one":
        rows = [
            f"{author.name} -> {author.profile.website}"
            for author in Author.objects.select_related("profile").order_by("name")
        ]
        strategy = 'Author.objects.select_related("profile")'
    elif example == "many":
        rows = [
            f"{book.title}: {', '.join(author.name for author in book.co_authors.all()) or '(no co-authors)'}"
            for book in Book.objects.prefetch_related("co_authors").order_by("title")
        ]
        strategy = 'Book.objects.prefetch_related("co_authors")'
    elif example == "reverse":
        rows = [
            f"{author.name}: {', '.join(book.title for book in author.books.all()) or '(no books)'}"
            for author in Author.objects.prefetch_related("books").order_by("name")
        ]
        strategy = 'Author.objects.prefetch_related("books")'
    else:
        return JsonResponse({"error": "Unknown relationship example."}, status=400)

    return JsonResponse(
        {
            "example": example,
            "strategy": strategy,
            "queries_used": len(connection.queries) - query_count_before,
            "rows": rows,
        }
    )

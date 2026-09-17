# N+1 Query Lab

A small Django project that demonstrates the N+1 query problem with real SQLite data.

## Setup

```powershell
C:/Users/surface/AppData/Local/Programs/Python/Python313/python.exe -m pip install -r requirements.txt
C:/Users/surface/AppData/Local/Programs/Python/Python313/python.exe manage.py migrate
C:/Users/surface/AppData/Local/Programs/Python/Python313/python.exe manage.py seed_sample_data
C:/Users/surface/AppData/Local/Programs/Python/Python313/python.exe manage.py runserver
```

Open http://127.0.0.1:8000/ for the interactive guide. The live JSON endpoint is available at http://127.0.0.1:8000/api/sample-data/.

## Models

- `Book.author` is a `ForeignKey`, demonstrated with `select_related("author")`.
- `Author.profile` is a `OneToOneField`, demonstrated with `select_related("profile")`.
- `Book.co_authors` is a `ManyToManyField`, demonstrated with `prefetch_related("co_authors")`.
- `Author.books` is the reverse `ForeignKey` relationship, demonstrated with `prefetch_related("books")`.
# N-1-Query
The N+1 query problem happens when accessing related objects in a loop triggers a separate database query for every row.

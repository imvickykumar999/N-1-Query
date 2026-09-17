# N+1 Query Lab

An interactive Django lesson for understanding and fixing the N+1 query problem with `select_related()` and `prefetch_related()`. It includes real SQLite sample data for Books, Authors, profiles, many-to-many co-authors, and reverse relationships.

## Docker Hub

The public image is available at [Docker Hub](https://hub.docker.com/r/imvickykumar999/n-1-query):

```text
imvickykumar999/n-1-query:latest
```

### Pull the image

Install and start Docker Desktop or Docker Engine, then pull the latest image:

```bash
docker pull imvickykumar999/n-1-query:latest
```

### Run the container

The simplest command publishes the app on port `8000`:

```bash
docker run -d \
	--name n1query-lab \
	-p 8000:8000 \
	imvickykumar999/n-1-query:latest
```

Open the app at [http://localhost:8000/](http://localhost:8000/).

The container entrypoint automatically:

1. Applies Django migrations.
2. Seeds the sample Authors and Books when the database is empty.
3. Starts the configured application command.

### Keep SQLite data between containers

Mount a named volume at `/app` so the SQLite database survives container removal:

```bash
docker volume create n1query-data

docker run -d \
	--name n1query-lab \
	-p 8000:8000 \
	-v n1query-data:/data \
	-e DATABASE_PATH=/data/db.sqlite3 \
	imvickykumar999/n-1-query:latest
```

### Run with Gunicorn

Gunicorn is included in the image. Use it instead of the default Django development server when running the container behind a reverse proxy:

```bash
docker run -d \
	--name n1query-lab \
	-p 8000:8000 \
	imvickykumar999/n-1-query:latest \
	gunicorn n1query.wsgi:application --bind 0.0.0.0:8000 --workers 2
```

### Configure the container

The Django settings accept these environment variables:

| Variable | Example | Purpose |
| --- | --- | --- |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated allowed hosts. |
| `SECRET_KEY` | `replace-with-a-secret` | Django signing key. Set this outside local development. |
| `DEBUG` | `False` | Disable Django debug mode. |
| `DATABASE_PATH` | `/data/db.sqlite3` | Optional SQLite database path. |

Example:

```bash
docker run -d \
	--name n1query-lab \
	-p 8000:8000 \
	-e DEBUG=False \
	-e ALLOWED_HOSTS=localhost,127.0.0.1 \
	-e SECRET_KEY=replace-with-a-long-random-value \
	imvickykumar999/n-1-query:latest
```

### Check the container

```bash
docker ps
docker logs -f n1query-lab
curl http://localhost:8000/
curl http://localhost:8000/api/sample-data/
```

The Docker image includes a health check for the homepage. Inspect it with:

```bash
docker inspect --format='{{json .State.Health}}' n1query-lab
```

### Stop and remove the container

```bash
docker stop n1query-lab
docker rm n1query-lab
```

## Admin

Open [http://localhost:8000/admin/](http://localhost:8000/admin/) after starting the container. Create an administrator inside the running container when needed:

```bash
docker exec -it n1query-lab python manage.py createsuperuser
```

Do not use a shared default password in a public deployment.

## Local Django setup

```powershell
C:/Users/surface/AppData/Local/Programs/Python/Python313/python.exe -m pip install -r requirements.txt
C:/Users/surface/AppData/Local/Programs/Python/Python313/python.exe manage.py migrate
C:/Users/surface/AppData/Local/Programs/Python/Python313/python.exe manage.py seed_sample_data
C:/Users/surface/AppData/Local/Programs/Python/Python313/python.exe manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the interactive guide. The live JSON endpoints are available at `/api/sample-data/` and `/api/run-query/?example=foreign`.

## Build the image locally

```bash
docker build -t n-1-query:local .
docker run -d --name n1query-local -p 8000:8000 n-1-query:local
```

## Models

- `Book.author` is a `ForeignKey`, demonstrated with `select_related("author")`.
- `Author.profile` is a `OneToOneField`, demonstrated with `select_related("profile")`.
- `Book.co_authors` is a `ManyToManyField`, demonstrated with `prefetch_related("co_authors")`.
- `Author.books` is the reverse `ForeignKey` relationship, demonstrated with `prefetch_related("books")`.


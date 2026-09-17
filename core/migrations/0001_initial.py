from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="AuthorProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("website", models.URLField(blank=True)),
                ("bio", models.TextField(blank=True)),
                ("author", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="profile", to="core.author")),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("published_year", models.PositiveIntegerField()),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="books", to="core.author")),
                ("co_authors", models.ManyToManyField(blank=True, related_name="coauthored_books", to="core.author")),
            ],
        ),
    ]

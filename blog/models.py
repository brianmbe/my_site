from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)
    excerpt = models.TextField()
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return f"{self.title}"

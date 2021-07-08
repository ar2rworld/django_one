from pathlib import Path
from django.db import models

#https://forum.djangoproject.com/t/upload-to-must-be-a-relative-path/3806/2
def get_img_upload_path(instance, filename):
    return f'{Path(__file__).resolve().parent}/images/{filename}'

# Create your models here.
class Publisher(models.Model):
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=50)
  city = models.CharField(max_length=60)
  state_province = models.CharField(max_length=30)
  country = models.CharField(max_length=50)
  website = models.URLField()
  def __str__(self):
    return f'{self.name}, {self.address} {self.city}'
  class Meta:
    ordering = ["name"]
  class Admin:
    pass
class Author(models.Model):
  salutation = models.CharField(max_length=10)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=40)
  email = models.EmailField()
  headshot = models.ImageField(upload_to=get_img_upload_path)
  def __str__(self):
    return '%s %s' % (self.first_name, self.last_name)
  class Admin:
    pass
class Book(models.Model):
  title = models.CharField(max_length=100)
  authors = models.ManyToManyField(Author)
  publisher = models.ForeignKey(Publisher, models.CASCADE)
  publication_date = models.DateField()
  def __str__(self):
    return self.title
  
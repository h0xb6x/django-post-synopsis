from django.db import models


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    synopsis = models.OneToOneField('Synopsis', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Synopsis(models.Model):
    text = models.TextField()


class Category(models.Model):
    category = models.CharField(max_length=255)

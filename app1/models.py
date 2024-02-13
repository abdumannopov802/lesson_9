from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    author = models.CharField(db_column='author', max_length=100, blank=False)
    year = models.IntegerField(db_column='year',blank=False, default=2000)
    liked = models.ManyToManyField(User, default=None, related_name='liked', blank=True)
    disliked = models.ManyToManyField(User, default=None, related_name='disliked', blank=True)

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
    
    @property
    def number_of_likes(self):
        return self.liked.all().count()
    
    @property
    def number_of_dislikes(self):
        return self.liked.all().count()


    def get_absolute_url(self):
        return reverse('book-list', args=[str(self.pk)])

LIKE_CHOICES = (
    ('like', 'like'),
    ('unlike', 'unlike'),
)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)

    def __str__(self) -> str:
        return str(self.book)
    
DISLIKE_CHOICES = (
    ('dislike', 'dislike'),
    ('undislike', 'undislike'),
)
    
class DisLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)

    def __str__(self) -> str:
        return str(self.book)
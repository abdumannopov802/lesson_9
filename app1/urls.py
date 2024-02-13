
from .views import *
from django.urls import path

urlpatterns = [    
    path('', bookList, name='book-list'),
    path('book-create', bookCreate, name='book-create'),
    path('book-update/<int:id>', bookUpdate, name='book-update'),
    path('book-delete/<int:id>', bookDelete, name='book-delete'),
    path('book-detail/<int:id>', bookDetail, name='book-detail'),
    # path('blogpost-like/<int:pk>', BlogPostLike, name="blogpost_like"),
    path('like/', book_like, name="like-post"),
    path('dislike/', book_dislike, name="dislike-post"),
]
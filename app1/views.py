from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def bookList(request):  
    books = Book.objects.all()  
    user = request.user
    return render(request,"book-list.html", context={'books':books, 'user':user})  

def bookCreate(request):  
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
            form.save() 
            model = form.instance
            return redirect('book-list')  
    else:  
        form = BookForm()  
    return render(request,'book-create.html',{'form':form})  

def bookUpdate(request, id):  
    # book = get_list_or_404(Book, id=id)
    book = Book.objects.get(id=id)
    form = BookForm(initial={'title': book.title, 'description': book.description, 'author': book.author, 'year': book.year})
    if request.method == "POST":  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():  
            form.save() 
            model = form.instance
            return redirect('book-list') 
    return render(request,'book-update.html',{'form':form})  

def bookDelete(request, id):
    # book = get_list_or_404(Book, id=id)
    book = Book.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('book-list')

def bookDetail(request, id):
    book = Book.objects.get(id=id) 
    return render(request,'book-detail.html', {'book': book})

def book_like(request):
    # book = Book.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Book.objects.get(id=post_id)

        if user not in post_obj.liked.all():
            post_obj.liked.add(user)
            if user in post_obj.disliked.all():
                post_obj.disliked.remove(user)
        else:
            post_obj.liked.remove(user)

        like, created = Like.objects.get_or_create(user=user, book_id=post_id)

        if not created:
            if like.value == 'like':
                like.value = 'unlike'
            else:
                like.value = 'like'
            
        like.save()
    return redirect('book-list')


def book_dislike(request):
    # book = Book.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Book.objects.get(id=post_id)

        if user not in post_obj.disliked.all():
            post_obj.disliked.add(user)
            if user in post_obj.liked.all():
                post_obj.liked.remove(user)
        else:
            post_obj.disliked.remove(user)

        dislike, createdd = DisLike.objects.get_or_create(user=user, book_id=post_id)

        if not createdd:
            if dislike.value == 'like':
                dislike.value = 'unlike'
            else:
                dislike.value = 'like'
            
        dislike.save()
    return redirect('book-list')

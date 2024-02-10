from django.shortcuts import render, redirect, get_list_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def bookList(request):  
    books = Book.objects.all()  
    return render(request,"book-list.html",{'books':books})  

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
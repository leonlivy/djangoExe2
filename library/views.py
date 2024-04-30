from django.shortcuts import render,get_object_or_404,redirect
from .models import Book, Author
from .forms import BookForm, AuthorForm

def book_list(request):
    books =Book.objects.all()
    return render(request,'library/book_list.html',{'books':books})
def book_detail(request):
    book =get_object_or_404(Book,pk=pk)
    return render(request, 'library/book_detail.html',{'books':book})
def book_create(request):
    if request.method=='POST':
        form =BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm()
    return render (request, 'library/BookForm.html',{'form':form})

def book_update(request):
    book =get_object_or_404(Book, pk=pk)
    if request.method =='POST':
        form =BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else: 
        form =BookForm(instance=book) 
    return render(request,'library/book_form.html',{'form':form})

def book_delete(request):
    book =get_object_or_404(Book, pk=pk)
    if request.method =='POST':
        book.delete()
        return redirect('book_list')
    return render (request, 'library/book_cofirm_delete.html',{'book':book})


from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)


def books_years(request, slug):
    template = 'books/books_years.html'
    text = f'Book of: {slug}'
    books = Book.objects.all()
    print(books)
    # if books['pub_date'] == slug:
    #     pfint()
    paginator = Paginator(books, 25)
    page_obj = paginator.get_page(paginator)
    context = {
        'page_obj': page_obj,
        'text': text,
    }
    return render(request, template, context=context)
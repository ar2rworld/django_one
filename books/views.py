from django.shortcuts import render
from django.db.models import Q
from books.models import Book

def search(request):
  query = request.GET.get('q', '')
  if query:
    qset = (Q(title__icontains=query) |
      Q(authors__first_name__icontains=query)|
      Q(authors__last_name__icontains=query))
    results = Book.objects.filter(qset).distinct()
  else:
    results = []
  return render("books/search.html", {
    "results": results,
    "query": query
  })
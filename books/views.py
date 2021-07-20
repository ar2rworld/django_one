from books.models import Author, Publisher
from django.shortcuts import render
from django.db.models import Q
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from books.forms import PublisherForm

def search(request):
  query = request.GET.get('q', '')
  if query:
    qset = (Q(title__icontains=query) |
      Q(authors__first_name__icontains=query)|
      Q(authors__last_name__icontains=query))
    results = Book.objects.filter(qset).distinct()
  else:
    results = []
  return render(request, "books/search.html", {
    "results": results,
    "query": query
  })
def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      topic = form.cleaned_data['topic']
      message = form.cleaned_data['message']
      #sender = form.get('sender', 'noreply@example.com')
      sender = form.cleaned_data['sender']
      #print(topic, message, sender)
      '''send_mail(    'Feedback from your site, topic: %s' % topic,
        message,
        sender,
        ['ar2r.world@gmail.com'])'''
      return render(request, 'books/thanks.html', {'topic':topic, 'message':message, 'sender': sender})
    else:
      HttpResponseRedirect('/')
  else:
    form = ContactForm()
  return render(request, 'books/contact.html', {'form': form})

def thanks(request):
  return render(request, 'books/thanks.html', {})

def add_publisher(request):
  form = PublisherForm()
  if request.method == 'POST':
    form = PublisherForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_publisher/thanks/')
    else:
      form = PublisherForm()
  return render(request, 'books/add_publisher.html', {'form': form})

def books(request):
  books=Book.objects.all()
  return render(request, 'books/books_archive.html',{'books':books})

def year_archive(request, year):
  books=Book.objects.filter(publication_date__range=[year+'-01-01', year+'-12-31'])
  return render(request, 'books/books_archive.html',{'year':year, 'books':books})

def add_model(request, model, action, salutation, first_name, last_name, email, headshot):
  if model.lower() == 'author':
    if action == 'add':
      a=Author(salutation=salutation, first_name=first_name, last_name=last_name, email=email, headshot=headshot)
      a.save()
  return render(request, 'books/thanks.html', {'model': model, 'action': action, 'first_name':first_name})
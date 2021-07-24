from django.http import HttpResponse
import csv
from django.db.models import Expression

from books.models import Author, Publisher, User
from django.shortcuts import redirect, render
from django.db.models import Q
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail
from django.utils import timezone
from django.http import HttpResponseRedirect
from books.forms import PublisherForm

from django.views.generic.list import ListView

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

def login(request):
  try:
    username = request.POST['username']
    password = request.POST['password']
    type = request.POST['type']
    status = ''
    if type == 'registration':
      if not User.objects.filter(username=username):
        User.objects.create(username=username, password=password, )
      else:
        status = 'yes'
    n_users = User.objects.count()
    return render(request, 'books/login.html', {'n_users' : n_users, 'status' : status})
  except Exception as e:
    print(e)
    return render(request, 'books/login.html', {'status': e})

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

class publisher_list_view(ListView):
  model=Publisher
  paginate_by=10
  queryset=Publisher.objects.all()
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['now'] = timezone.now()
      context['extra'] = 'ola!'
      return context

def book_content_archive(request):
  if not request.GET:
    #image_data = open("C:/Users/Artur/Documents/GitHub/django_one/django_one/books/images/78950.jpg", "rb").read()
    return render(request, 'books/book_content_archive.html') #HttpResponse(image_data, content_type="image/png")
  else:
    if request.GET['csv']=='books':
      # Create the HttpResponse object with the appropriate CSV header.
      response = HttpResponse(content_type='text/csv')
      response['Content-Disposition'] = 'attachment; filename=books.csv'
      # Create the CSV writer using the HttpResponse as the "file"
      writer = csv.writer(response)
      writer.writerow(['title', 'authors', 'publisher', 'publication_date'])
      for o in Book.objects.all():
          writer.writerow([o.title, o.authors, o.publisher, o.publication_date])
      return response
    else:
      return render(request, 'books/book_content_archive.html')
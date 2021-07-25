#from django_one.books import views
from django import template
from django.http import HttpResponse, JsonResponse
from django.template import Template,Context
import requests as req
import datetime
from django_one.static.css.style import style
from django.template.loader import get_template
from books.models import Publisher, Book, Author, Statistics, User
#from django.contrib.auth.models import User

coinsTemplate=Template(
  """
  <div class='coinsTemplate yellowBackColor'><div class="tcontainer"><div class="ticker-wrap"><div class="ticker-move">
    {% for i in arr %}
      <div class='ticker-item coin'>
        <img style="width:25px; height:25px; border-radius: 7px; border: 3px green solid" src="{{i.item.small}}"><br>
        {{i.item.symbol}}<br>
        <i>BTC</i>:<span>{{i.item.price_btc}}</span>
      </div>
    {% endfor %}

  </div></div></div></div>""")

def getTrendingTemplate():
  call=req.get("https://api.coingecko.com/api/v3/search/trending")
  jsonData=call.json()['coins']
  print("Coins count: ", len(jsonData))
  return coinsTemplate.render(Context({'arr':jsonData}))

def update_views_counter():
  stats_table=Statistics.objects.all()
  if len(stats_table)>0:
    views=stats_table[0]#.get(id=0)
    #print('views:', views.views+1)
    views.views+=1
    views.save()

def homeView(request):
  update_views_counter()
  template = get_template('body.html').render({'numberOfComrades': User.objects.count(),
  'views': Statistics.objects.all()[0],
  'username' : request.COOKIES.get('username')})
  trending='<i>here should be made an API call and data displayed asynchronally</i>'#getTrendingTemplate()

  return HttpResponse(template)

def time(request):
  html=get_template('current_datetime.html').render({})
  return HttpResponse(html)

def book_store(request):
  t=get_template('book_store.html')
  html=t.render({'publishers':Publisher.objects.all(),
    'books':Book.objects.all(),
    'authors':Author.objects.all()})
  return HttpResponse(html)

def stats(request):
  stats_table=Statistics.objects.all()
  views_count=0
  if len(stats_table)==1:
    views_count=stats_table.get(id=0).views
  return JsonResponse({'views':views_count})

def footerTemplate():
  #the thing is that i need to render this template(footer) 
  #every time with main_base.html template and pass data about views
  #but i don't wanna copy the same text of request to /stats/
  #in every view, so i want to make a function which will be executed every
  #time component main_base.html is rendered to get data of views
  #to render it in footer part 
  pass
'''didnt used here:
locals()
{% include %}
'''
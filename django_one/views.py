from django import template
from django.http import HttpResponse
from django.template import Template,Context
import requests as req
import datetime
from django_one.static.css.style import style
from django.template.loader import get_template
from books.models import Publisher

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



def homeView(request):  
  template = get_template('body.html').render({'numberOfComrades': '1'})
  trending='<i>here should be made an API call and data displayed asynchronally</i>'#getTrendingTemplate()
  return HttpResponse(template)

def time(request):
  html=get_template('current_datetime.html').render({})
  return HttpResponse(html)

def publishersView(request):
  t=get_template('publishers.html')
  html=t.render({'publishers':Publisher.objects.all()})
  return HttpResponse(html)

'''didnt used here:
locals()
{% include %}
'''
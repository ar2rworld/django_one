from django import template
from django.http import HttpResponse
from django.template import Template,Context
import requests as req
import datetime
from django_one.static.css.style import style
from django.template.loader import get_template


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
  #kostil
  styleFile = open('django_one/static/css/style.css')
  style = styleFile.read()
  styleFile.close()
  
  template = get_template('body.html').render({'numberOfComrades': '1'})

  trending='<i>here should be made an API call and data displayed asynchronally</i>'#getTrendingTemplate()
  
  homeHeader=Template('''
  <link rel="stylesheet"  href="django_one/static/css/style.css">
  <title>Django_one</title>
  <style>''' +style+'''</style>''')

  footer = get_template('footer.html').render({'data':'This is a bottom part',
    'phone': 7777777777,
    'email': 'ar2r.world@gmail.com',
    'website': 'http://ec2-3-141-45-250.us-east-2.compute.amazonaws.com'})
  html = homeHeader.render(Context({}))+\
  """
  <html><body class='greenBackColor'>
    <div class='awesome whiteBackColor'>
      <h2>Django_one</h2>
      <div class='miniMenu'>
        <button>Login</button><br>
        <button>Register</button><br>
      </div>
    </div>
    """+ trending + template + footer +"""
  </body></html>"""

  return HttpResponse(html)

  '''didnt used here:
  locals()
  {% include %}
  '''
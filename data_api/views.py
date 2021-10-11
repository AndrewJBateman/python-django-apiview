from django.shortcuts import render
import requests
API_KEY = ''

def home(request):
  country = request.GET.get('country')
  category = request.GET.get('category')

  if country:
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'

  elif category:
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}'

  else:
    url = f'https://newsapi.org/v2/top-headlines?country=fr&category=Technology&apiKey={API_KEY}'

  response = requests.get(url)
  data = response.json()
  articles = data['articles']

  context = {
    'articles' : articles
  }

  return render(request, 'data_api/home.html', context)
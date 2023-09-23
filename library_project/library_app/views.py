from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests

def search_books(request):
    if request.method == 'POST':
        query = request.POST['search_query']
        response = requests.get(f'https://openlibrary.org/search.json?q={query}')
        data = response.json()
        books = data.get('docs', [])
        return render(request, 'library_app/search_results.html', {'books': books})
    return render(request, 'library_app/search_form.html')
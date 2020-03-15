from django.shortcuts import render
from search.business import search_and_parsing


# Create your views here.

def search_page(request):
    return render(request, 'search/main/index.html')


def search_result(request):
    if request.method == 'POST':
        query = request.POST['query']
        result = search_and_parsing(query)
        print(result)
        return render(request, 'search/result/index.html', {'result': result})
    else:
        return render(request, '405.html')

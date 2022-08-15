from django.shortcuts import render, redirect
from .models import FeelPost
from .forms import FeelPostForm
import requests

def feelpost(request):
    if request.method == 'POST' or request.method == "FILES":
            form = FeelPostForm(request.POST, request.FILES)
            searchword = request.POST.get('post_detail')       
            if form.is_valid():
                url = 'https://127.0.0.1:8000/post_detail'
                response = requests.get(url)
                resdata = response.text
                with open('feeling.txt', 'w', encoding='utf-8') as feeltxt:
                    feeltxt.write(resdata)
                return render(request, 'feelpost.html', {'resdata':resdata})
    else:
        form = FeelPostForm()
        url = 'https://127.0.0.1:8000/post_detail'
        response = requests.get(url)
        resdata = response.text
        return render(request, 'feelpost.html', {'resdata':resdata, 'form':form})

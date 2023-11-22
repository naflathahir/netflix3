from django.shortcuts import render
import requests
def index(request) :
    

    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1" 

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0OWQwMTI4ODMyZTQ0MzNhOThlMTZlOGJhNWEzYjgyMiIsInN1YiI6IjY1MzIyNWJlNDgxMzgyMDBlMjg5NjA4NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.b9bMG7X0dU5c__6-ki61WhQQrMl1FHGWM4IMBEDp3Kk"
     }

    response = requests.get(url, headers=headers)

    
    posts = response.json()
    data = posts['results']
    context = {
        "data":data
    }
    return render(request,"index.html",context)

# Create your views here.

from django.shortcuts import render
import requests
from django.contrib import messages
# Create your views here.
def shaowindex(request):

    return render(request,"index.html")


def search(request):
    sss = request.POST.get("s1")
    print(sss)
    search_url = 'http://www.omdbapi.com/?apikey=51d961ff&'
    params = {'s': sss,

              "r": "json"

              }

    r=requests.get(search_url,params)
    print(r.text)

    results = r.json()["Search"]
    print(results)
    movies=[]
    for x in results:

        movie_data={
        'title':x['Title'],
        'year':x['Year'],
        'imdb':x['imdbID'],
        'poster':x['Poster'],
        'type':x['Type']
        }
        movies.append(movie_data)



    contxt={
                "movies":movies
        }

    return render(request,"search_data.html",contxt)



# def search_data(request):
#     return render(request,"search_data.html")
def view_movie_info(request):
    s1=request.GET.get("no")
    search_url = 'http://www.omdbapi.com/?apikey=51d961ff&'
    params = {'i': s1,

              "r": "json",
              "plot":"full"

              }

    r = requests.get(search_url, params)
    movie_info={
    'title':r.json()["Title"],
    'year':r.json()["Year"],
    'released':r.json()["Released"],
    'genre':r.json()["Genre"],
    'director':r.json()["Director"],
    'writer':r.json()["Writer"],
    'poster':r.json()["Poster"],
    "rating":r.json()["imdbRating"],
    "plot":r.json()["Plot"]

    }
    return render(request,"view_movie_info.html",movie_info)
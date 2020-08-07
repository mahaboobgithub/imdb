from django.shortcuts import render
import requests

# Create your views here.
def shaowindex(request):

    return render(request,"index.html")


def search(request):
    sss = request.POST.get("s1")
    print(sss)
    search_url = 'http://www.omdbapi.com/?apikey=51d961ff&'
    params = {'s': sss,
              "type": "movie",
              "r": "json"

              }

    r=requests.get(search_url,params)
    print(r.text)

    title=(r.json()["Search"][0]["Title"])
    year=(r.json()["Search"][0]["Year"])
    imbd=(r.json()["Search"][0]["imdbID"])
    poster=(r.json()["Search"][0]["Poster"])
    movie_data={
        "title":title,
        "year":year,
        "imdb":imbd,
        "poster":poster
    }



    return render(request,"search_data.html",movie_data)


# def search_data(request):
#     return render(request,"search_data.html")
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.db.models import F
import requests

from .models import Staff, Movies


# Create your views here.

def index(request):
    movies = Movies.objects.all()
    search_keyword = request.GET.get('search', '')

    if search_keyword:
        movies = movies.filter(title_kor__icontains=search_keyword)

    paginator = Paginator(movies, 8)
    page = request.GET.get('page')
    paginated_movies = paginator.get_page(page)
    return render(request, 'index.html', {'movies': paginated_movies})


def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:

        # movie의 튜플 저장
        new_movie = Movies()
        new_movie.title_kor = movie['title_kor']
        new_movie.title_eng = movie['title_eng']
        new_movie.poster_url = movie['poster_url']
        new_movie.rating_aud = movie['rating_aud']
        new_movie.rating_cri = movie['rating_cri']
        new_movie.rating_net = movie['rating_net']
        new_movie.genre = movie['genre']
        new_movie.showtimes = movie['showtimes']
        new_movie.release_date = movie['release_date']
        new_movie.rate = movie['rate']
        new_movie.summary = movie['summary']
        new_movie.save()

        staffs = movie['staff']
        # movie의 먼저 저장
        for staff in staffs:
            new_staff = Staff()
            new_staff.name = staff['name']
            new_staff.role = staff['role']
            new_staff.image_url = staff['image_url']
            new_staff.movie = Movies.objects.get(pk=new_movie.id)
            new_staff.save()
    return redirect('index')


# def search(request):
#     movies = Movies.objects.filter(title_kor=search)
#     return redirect(request, 'index.html', {'movies': movies})

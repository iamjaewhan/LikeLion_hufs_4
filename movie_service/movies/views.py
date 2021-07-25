from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

import requests

from .models import Staff, Movies, Comment
from .forms import CommentForm
import requests
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    movies = Movies.objects.all()
    search_keyword = request.GET.get('search', '')
    if search_keyword:
        movies = movies.filter(title_kor__icontains=search_keyword)
    paginator = Paginator(movies, 8)
    page = request.GET.get('page')
    paginated_movies = paginator.get_page(page)
    if search_keyword:
        return render(request, 'index.html', {'movies': paginated_movies, 'search_keyword': search_keyword})
    else:
        return render(request, 'index.html', {'movies': paginated_movies})


def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
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
        for staff in staffs:
            new_staff = Staff()
            new_staff.name = staff['name']
            new_staff.role = staff['role']
            new_staff.image_url = staff['image_url']
            new_staff.movie = Movies.objects.get(pk=new_movie.id)
            new_staff.save()
    return redirect('index')

        
def detail(request, id):
    movie = Movies.objects.get(id=id)
    staffs = Staff.objects.filter(movie=movie)

    for staff in staffs:
        print(staff)
    comment_form = CommentForm()
    comments = Comment.objects.filter(movie=movie)
    if comments:
        total = 0
        for comment in comments:
            total += int(comment.rate)
        if total != 0:
            rate = round(total/len(comments), 2)
        else:
            rate = 0
    else:
        rate = "아직 평가가 없습니다."
    return render(request, 'detail.html', {'movie': movie, 'staffs': staffs, 'comments': comments, 'rate': rate})


@login_required(login_url='account:login')
def comment(request, id):
    movie = get_object_or_404(Movies, pk=id)
    comments = Comment.objects.filter(movie=movie)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.commenter = request.user
            new_comment.movie = movie
            new_comment.save()
            return redirect('movies:detail', id)
        else:
            form = CommentForm()
        return redirect('movies:detail', id)

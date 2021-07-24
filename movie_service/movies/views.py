from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import requests

from .models import Staff, Movies,Comment
from .forms import CommentForm




# Create your views here.

def index(request):
    return render(request,'index.html')


def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        new_movie=Movies()
        new_movie.title_kor=movie['title_kor']
        new_movie.title_eng=movie['title_eng']
        new_movie.poster_url=movie['poster_url']
        new_movie.rating_aud=movie['rating_aud']
        new_movie.rating_cri=movie['rating_cri']
        new_movie.rating_net=movie['rating_net']
        new_movie.genre=movie['genre']
        new_movie.showtimes=movie['showtimes']
        new_movie.release_date=movie['release_date']
        new_movie.rate=movie['rate']
        new_movie.summary=movie['summary']
        new_movie.save()
        
        staffs=movie['staff']
        for staff in staffs:
            new_staff=Staff()
            new_staff.name=staff['name']
            new_staff.role=staff['role']
            new_staff.image_url=staff['image_url']
            new_staff.movie=Movies.objects.get(pk=new_movie.id)
            new_staff.save()
    return redirect('index')

@login_required
def comment(request,id):
    movie=get_object_or_404(Movies,pk=id)
    comments=Comment.objects.filter(movie=movie)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid:
            new_comment=form.save(commit=False)
            new_comment=request.user
            new_comment.save()
            return redirect('#디테일페이지 url',id)
        else:
            form=CommentForm()
        return redirect('#디테일페이지#',ㅑㅇ)


        
def detail(request, id):
    movie = Movies.objects.get(id=id)
    staffs = Staff.objects.filter(movie=movie)
    return render(request, 'detail.html', {'movie': movie, 'staffs': staffs})

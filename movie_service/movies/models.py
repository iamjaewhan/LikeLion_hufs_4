from django.db import models

# Create your models here.
class Movies(models.Model):
    title_kor=models.CharField(max_length=50)
    title_eng=models.CharField(max_length=50)
    poster_url=models.CharField(max_length=300)
    rating_aud=models.CharField(max_length=50)
    rating_cri=models.CharField(max_length=50)
    rating_net=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    showtimes=models.CharField(max_length=50)
    release_date=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    summary=models.TextField()
    ##staff=models.ForeignKey(Staff,null=True,on_delete=models.CASCADE)

    def summary(self):
        return self.summary[:100]

class Staff(models.Model):
    name=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    image_url=models.CharField(max_length=300)
    movie=models.ForeignKey(Movies,null=True, on_delete=models.CASCADE)
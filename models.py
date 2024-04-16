from django.db import models
from django.contrib.auth.models import User
from .validators import validate_phone_no
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator

# Create your models here.

class movie(models.Model):
    title=models.CharField(max_length=100)
    blog_date=models.DateField()
    poster=models.ImageField(upload_to='movie')
    release_date=models.DateField()
    story=models.TextField()
    review=models.TextField()
    movie_rating=models.DecimalField(max_digits=5,decimal_places=1)


    def __str__(self):
        return self.title


class comments(models.Model):
    user=models.CharField(max_length=30)
    comment=models.TextField()
    comment_date=models.DateField(auto_now=True)
    user_rating=models.DecimalField(max_digits=5,decimal_places=1)
    review=models.ForeignKey(movie,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user


class RegisterModel(User):
    phone_no=models.PositiveBigIntegerField(validators=[MinValueValidator(10),MaxValueValidator(10),validate_phone_no])
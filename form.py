from django import forms
from .models import movie,comments
from .models import RegisterModel
from .validators import validatename,validate_username
from django.forms import ValidationError
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator

class moviereviewform(forms.ModelForm):
    class Meta:
        model=movie
        fields='__all__'
        widgets={'release_date':forms.DateInput(attrs={'type':'date'}),'blog_date':forms.DateInput(attrs={'type':'date'})}


class commentform(forms.ModelForm):
    class Meta:
        model=comments
        exclude=['comment_date']
        widgets={'review':forms.HiddenInput} 


class Registerform1(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields=['first_name','last_name','username','password','phone_no']
        widgets={'password':forms.PasswordInput}
        validators=[validatename,validate_username]


class RegisterForm(Registerform1):
    validators=[validatename,validate_username]
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.CharField(max_length=500, required=True)
    gender = forms.ChoiceField( choices=User.GENDERS, required=True)
    phone = forms.CharField(max_length=15, required=True)
    description = forms.CharField( max_length=500, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2','bio','phone','description')

    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.bio = self.cleaned_data["bio"]
        user.gender = self.cleaned_data["gender"]
        user.phone = self.cleaned_data["phone"]
        user.description = self.cleaned_data["description"]
        print(user.gender)
        if commit:
            user.save()
        return user
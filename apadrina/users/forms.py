from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class SignUpForm(UserCreationForm):
    gênero = forms.ChoiceField( choices=User.GENDERS, required=True)
    celular = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','celular', 'gênero')

    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.gender = self.cleaned_data["gênero"]
        user.phone = self.cleaned_data["celular"]
        print(user.gender)
        if commit:
            user.save()
        return user
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    """
    Кастомная форма регистрации пользователя с дополнительным полем email
    Custom user registration form with additional email field
    """
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Email'})
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def clean_email(self):
        """
        Валидация поля email на уникальность
        Validating the email field for uniqueness
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким email уже существует')
        return email


    def save(self, commit=True):
        """
        Сохраняет пользователя с присвоением email
        Saves the user with the assigned email
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

import re
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
        Валидация поля email
        Validating the email field
        """
        email = self.cleaned_data.get('email')
        email = email.strip()
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            raise ValidationError('Введите корректный email адрес')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким email уже существует')
        return email


    def clean_username(self):
        """
        Валидация никнейма пользователя
        User nickname validation
        """
        username = self.cleaned_data.get('username')
        username = username.strip()
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError(
                'Имя пользователя содержит недопустимые символы')

        if len(username) < 3:
            raise ValidationError('Имя пользователя слишком короткое')

        if len(username) > 20:
            raise ValidationError('Имя пользователя слишком длинное')
            
        forbidden_names = ['admin', 'root', 'superuser', 'moderator']
        if username.lower() in forbidden_names:
            raise ValidationError('Это имя пользователя запрещено')
            
        return username


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


class ProfileEditForm(forms.ModelForm):
    """
    Форма редактирования профиля пользователя
    User profile editing form
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


    def clean_username(self):
        """
        Валидация никнейма пользователя
        User nickname validation
        """
        username = self.cleaned_data['username']
        username = username.strip()
        if User.objects.exclude(
                pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует')
    
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError(
                'Имя пользователя содержит недопустимые символы')

        if len(username) < 3:
            raise ValidationError('Имя пользователя слишком короткое')

        if len(username) > 20:
            raise ValidationError('Имя пользователя слишком длинное')
    
        forbidden_names = ['admin', 'root', 'superuser', 'moderator']
        if username.lower() in forbidden_names:
            raise ValidationError('Это имя пользователя запрещено')
    
        return username

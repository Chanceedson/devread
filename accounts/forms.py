from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        validators=[EmailValidator(message='Please enter a valid email address.')],
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'you@example.com'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'Username'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'Password (minimum 8 characters)'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self) -> str:
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required.')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email

    def clean_username(self) -> str:
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Username is required.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_password1(self) -> str:
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise forms.ValidationError('Password is required.')
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password1

    def clean_password2(self) -> str:
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError('Please confirm your password.')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'you@example.com'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'Password'
        })
    )


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'Username'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'Email'
        })
    )
    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'Last Name'
        })
    )
    bio = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'Tell us about yourself',
            'rows': 4
        })
    )
    github_username = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'GitHub username'
        })
    )
    website = forms.URLField(
        max_length=100,
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'https://example.com'
        })
    )
    primary_techstack = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'placeholder': 'e.g. Python/Django, JavaScript/React'
        })
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'block w-full px-4 py-2.5 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-primary focus:border-primary',
            'accept': 'image/*'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'github_username', 'website', 'primary_techstack', 'avatar']

    def clean_email(self) -> str:
        email = self.cleaned_data.get('email')
        user = self.instance
        if User.objects.filter(email=email).exclude(pk=user.pk).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    def clean_username(self) -> str:
        username = self.cleaned_data.get('username')
        user = self.instance
        if User.objects.filter(username=username).exclude(pk=user.pk).exists():
            raise forms.ValidationError('This username is already taken.')
        return username




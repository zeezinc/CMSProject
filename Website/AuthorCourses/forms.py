from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Document, AllContents


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "*Required",
                "class": "form-control"
            }
        )
    )

    username = forms.CharField(
        label='Username',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "*Required",
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "*Required",
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "*Required",
                "class": "form-control"
            }
        )
    )

    number = forms.CharField(
        label='Phone Number',
        required=True,
        max_length=10,
        min_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "*Required",
                'pattern': '[0-9]+',
                'title': 'Enter numbers Only '
            }
        )
    )

    pincode = forms.CharField(
        required=True,
        max_length=6,
        min_length=6,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "*Required",
                'pattern': '[0-9]+',
                'title': 'Enter numbers Only '
            }
        )
    )

    full_name = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "*Required",
                'pattern': '^([a-zA-Z]{2,}\\s[a-zA-Z]{2,}\\s?([a-zA-Z]{1,})?)',
                'title': 'Enter First Name and Last Name '
            }
        )
    )

    address = forms.CharField(
        label='Address',
        max_length=100,
        min_length=5,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    city = forms.CharField(
        label='City',
        max_length=30,
        min_length=3,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    state = forms.CharField(
        label='State',
        max_length=30,
        min_length=5,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    country = forms.CharField(
        label='Country',
        max_length=30,
        min_length=5,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'full_name', 'number', 'address', 'city', 'pincode',
                  'state', 'country')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')


class ContentForm(forms.ModelForm):
    class Meta:
        model = AllContents
        fields = '__all__'
        labels = {
            'contentName': 'Title',
            'contentBody': 'Body',
            'contentSummary': 'Summary',
            'category': 'Category',
            'doc': 'Document',
            'author': 'Author',
        }

    def __init__(self, *args, **kwargs):
        self.entry = kwargs.pop('entry')  # the content entry instance
        super().__init__(*args, **kwargs)

    def save(self):
        cont = super().save(commit=False)
        cont.entry = self.entry
        cont.save()
        return cont

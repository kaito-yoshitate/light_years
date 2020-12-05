from django import forms
from graivtation.models import User, Lonliness


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'who_is')
        labels = {
            'name'   : 'お名前',
            'who_is' : '自己紹介'
        }
        help_texts = {
            'name'   : '名前を書く',
            'who_is' : '自己紹介を書く'
        }


class SubmitForm(forms.ModelForm):
    class Meta:
        model = Lonliness
        fields = ('content')
        labels = {
            'content'  : 'さみしさ'
        }
        help_texts = {
            'content'  : 'さみしさを書く'
        }

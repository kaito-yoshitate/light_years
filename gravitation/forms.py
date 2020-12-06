from django import forms
from gravitation.models import User, Lonliness


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'who_is', 'mail')
        labels = {
            'name'   : 'お名前',
            'who_is' : '自己紹介',
            'mail'   : 'メールアドレス'
        }
        help_texts = {
            'name'   : '名前を書く',
            'who_is' : '自己紹介を書く',
            'mail'   : 'メールアドレスをいれる'
        }


class SubmitForm(forms.ModelForm):
    class Meta:
        model = Lonliness
        fields = ('content',)
        labels = {
            'content'  : 'さみしさ'
        }
        help_texts = {
            'content'  : 'さみしさを書く'
        }

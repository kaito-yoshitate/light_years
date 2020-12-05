from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from graivtation.models import User, Lonliness, Reaction
from graivtation.forms import RegisterForm, SubmitForm


def register_user(request):
    """
    ユーザ登録
    """
    params = {'message': '', 'form': None}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_prev_lonliness')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    return render(request, 'gravitation/html/register.html', params)

@login_required
def display_prev_lonliness(request):
    """
    前の人の『さみしさ』を表示する
    """
    latest_lonliness = Lonliness.objects.latest('content')
    return render(request,
                  'gravitation/html/lonliness.html',
                  {'lonliness' : latest_lonliness})

@login_required
def submit_own_lonliness(request):
    """
    自身の『さみしさ』を投稿する
    """
    params = {'message': '', 'form': None}

    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('check_reaction_for_me')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    return render(request, 'gravitation/html/submit.html', params)

@login_required
def check_reaction_for_me(request):
    """
    自身に付与されたリアクションを確認する
    """


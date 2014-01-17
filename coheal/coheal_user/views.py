#-*- coding: utf-8 -*-

from django.shortcuts import render


def connexion(request):
    return render(request, 'coheal_user/connexion.html')

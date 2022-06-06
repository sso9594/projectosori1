# 수정 중인 코드 주석 처리하였음

from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

from outfit.models import mixxo_model
from outfit.models import musinsa_model
from outfit.models import spao_model


def home(request):
    posts = mixxo_model.objects.all()
    return render(request,'index.html',{'posts':posts})
    
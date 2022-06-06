# 수정 중인 코드 주석 처리하였음

from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import os
import lxml

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "osori.settings")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import django
django.setup()

from outfit.models import mixxo_model
from outfit.models import musinsa_model
from outfit.models import spao_model


musinsa = "https://www.musinsa.com/mz/brandsnap?p=1"
mixxo = "https://www.mixxo.com"
spao = "https://www.spao.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}


def get_request(url):

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

# musinsa

# 이미지 링크 스크래핑 함수


def get_musinsa_images():
    soup = get_request(musinsa)
    list_items = soup.select('div.articleImg>a>img')
    list_images = [i.attrs['src'] for i in list_items[:3]]
    return list_images

# 링크 스크래핑 함수


def get_musinsa_links():
    soup = get_request(musinsa)
    list_items = soup.select('div.articleImg>a')
    list_links = ["https://www.musinsa.com" + i.attrs['href']
                  for i in list_items[:3]]

    return list_links

# 무신사 크롤링 함수


def get_musinsa_data():

    result = []
    i = 0
    list_links = get_musinsa_links()
    list_images = get_musinsa_images()

    for link, image in zip(list_links, list_images):
        i += 1

        musinsa_obj = {
            'musinsa_image': image,
            'musinsa_link': link,
            'musinsa_key': i
        }
        result.append(musinsa_obj)

    return result

# mixxo


def get_mixxo_images():
    # 상품 이미지 링크
    soup = get_request(mixxo)
    list_items = soup.select('div.prdImg>a>img')
    list_images = ["https:" + i.attrs['src'] for i in list_items[:3]]
    return list_images


def get_mixxo_links():
    # 상품 url
    soup = get_request(mixxo)
    list_items = soup.select('div.prdImg>a')
    list_links = ["https:" + i.attrs['href'] for i in list_items[:3]]
    return list_links

# 미쏘 크롤링 함수


def get_mixxo_data():

    result = []
    i = 0
    list_links = get_mixxo_links()
    list_images = get_mixxo_images()

    for link, image in zip(list_links, list_images):
        i += 1

        mixxo_obj = {
            'mixxo_image': image,
            'mixxo_link': link,
            'mixxo_key': i
        }
        result.append(mixxo_obj)

    return result

# spao


def get_spao_images():
    # 상품 이미지 링크
    soup = get_request(spao)
    list_items = soup.select('div.prdImg>a>img')
    list_images = ["https:" + i.attrs['src'] for i in list_items[:3]]
    return list_images


def get_spao_links():
    # 상품 url
    soup = get_request(spao)
    list_items = soup.select('div.prdImg>a')
    list_links = ["https:" + i.attrs['href'] for i in list_items[:3]]
    return list_links

# 스파오 크롤링 함수


def get_spao_data():

    result = []
    i = 0
    list_links = get_spao_links()
    list_images = get_spao_images()

    for link, image in zip(list_links, list_images):
        i += 1

        spao_obj = {
            'spao_image': image,
            'spao_link': link,
            'spao_key': i
        }
        result.append(spao_obj)

    return result


# insert data into sqlite
if __name__ == '__main__':
    musinsa_data = get_musinsa_data()
    mixxo_data = get_mixxo_data()
    spao_data = get_spao_data()

    # musinsa object
    for item in musinsa_data:
        musinsa_model(musinsa_image=item['musinsa_image'],
                musinsa_link=item['musinsa_link'], musinsa_key=item['musinsa_key']).save()

    # for item in mixxo_data:
    for item in mixxo_data:
        mixxo_model(mixxo_image=item['mixxo_image'],
              mixxo_link=item['mixxo_link'], mixxo_key=item['mixxo_key']).save()

    # for item in spao_data:
    for item in spao_data:
        spao_model(spao_image=item['spao_image'],
             spao_link=item['spao_link'], spao_key=item['spao_key']).save()

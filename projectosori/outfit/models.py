from django.db import models

# Create your models here.

class musinsa_model(models.Model):
    musinsa_key = models.IntegerField(primary_key = True)
    musinsa_image = models.TextField()
    musinsa_link = models.TextField()

    class Meta:
        db_table = 'musinsa'

class mixxo_model(models.Model):
    mixxo_key = models.IntegerField(primary_key = True)
    mixxo_image = models.TextField()
    mixxo_link = models.TextField()

    class Meta:
        db_table = 'mixxo'

class spao_model(models.Model):
    spao_key = models.IntegerField(primary_key = True)
    spao_image = models.TextField()
    spao_link = models.TextField()

    class Meta:
        db_table = 'spao'


class musinsa_rank(models.Model):
    musinsa_rank_key = models.IntegerField(primary_key = True)
    musinsa_rank_name = models.CharField(max_length= 100)
    musinsa_rank_link = models.TextField()

    class Meta:
        db_table = 'musinsa_rank'

class mixxo_rank(models.Model):
    mixxo_rank_key = models.IntegerField(primary_key = True)
    mixxo_rank_name = models.CharField(max_length=100)
    mixxo_rank_link = models.TextField()

    class Meta:
        db_table = 'mixxo_rank'

class spao_rank(models.Model):
    spao_rank_key= models.IntegerField(primary_key = True)
    spao_rank_name = models.CharField(max_length=100)
    spao_rank_link = models.TextField()

    class Meta:
        db_table = 'spao_rank'





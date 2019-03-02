from django.db import models


# Create your models here.
class Issuer(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Reward(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Card(models.Model):
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reward = models.ForeignKey(Reward, on_delete=models.PROTECT)

    class Meta:
        unique_together = (('issuer', 'name'),)


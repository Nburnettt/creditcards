from django.db import models


# Create your models here.
class Issuer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Reward(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reward = models.ForeignKey(Reward, on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.issuer.name, self.name)

    class Meta:
        unique_together = (('issuer', 'name'),)


class RewardEarningRate(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    points_everything = models.IntegerField(default=1)
    points_travel = models.IntegerField(default=1)
    points_flights = models.IntegerField(default=1)
    points_us_dining = models.IntegerField(default=1)
    points_gas = models.IntegerField(default=1)
    points_grocery = models.IntegerField(default=1)
    points_amazon = models.IntegerField(default=1)
    points_hotel = models.IntegerField(default=1)

    def __str__(self):
        return '{} {} earnings on {}'.format(self.card.issuer.name, self.card.name, self.card.reward.name)



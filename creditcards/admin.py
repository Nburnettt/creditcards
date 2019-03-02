from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Issuer)
admin.site.register(Reward)
admin.site.register(Card)
admin.site.register(RewardEarningRate)
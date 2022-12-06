from django.contrib import admin

from django.contrib.auth.models import User

from main_app.models import Individual, Business, Job_Post, Review


# Register your models here.


admin.site.register(Individual)
admin.site.register(Job_Post)
admin.site.register(Business)
admin.site.register(Review)

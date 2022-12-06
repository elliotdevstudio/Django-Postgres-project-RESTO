from django.contrib import admin

from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import Individual, Business, Job_Post, Review

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Business
    can_delete = False
    verbose_plural_name = 'business'

class ProfileInline(admin.StackedInline):
    model = Individual
    can_delete = False
    verbose_plural_name = 'individual'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.register(Business) 
admin.site.register(Job_Post)
admin.site.register(Individual)
admin.site.register(Review)


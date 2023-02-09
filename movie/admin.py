from django.contrib import admin
from .models import Movie, Comment, Review


admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Review)
# Register your models here.

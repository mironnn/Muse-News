from django.contrib import admin

# Register your models here.

from rest_app.models import Post

admin.site.register(Post)

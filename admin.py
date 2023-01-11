from django.contrib import admin
from .models import Post

# in this file we define which models should be displayed in our admin site.

# we want to display our admin
admin.site.register(Post)

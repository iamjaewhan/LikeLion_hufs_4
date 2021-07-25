from django.contrib import admin
from .models import Staff,Movies, Comment
from account.models import User



# Register your models here.

admin.site.register(Staff)
admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Comment)

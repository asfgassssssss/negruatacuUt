from django.contrib import admin

# Register your models here.
from .models import TheBestBooks

class TheBestBooksAdmin(admin.ModelAdmin):
    list_display = ('id','Author','DateOfBirth','Cost')

admin.site.register(TheBestBooks, TheBestBooksAdmin)
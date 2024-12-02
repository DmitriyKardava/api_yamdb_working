from django.contrib import admin

from .models import ReviewUser


class ReviewUserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "email")


admin.site.register(ReviewUser, ReviewUserAdmin)

from django.contrib import admin

from .models import Travel


class TravelInlineAdmin(admin.TabularInline):
    model = Travel
    extra = 0

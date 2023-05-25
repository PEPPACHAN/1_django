from django.contrib import admin
from .models import *


# class UsersInLine(admin.TabularInline):
#     model = Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
    fields = [('email', 'password')]
    # inlines = [UsersInLine]
    # fieldsets = (
    #     (None, {
    #         'fields': ('book', 'imprint', 'id')
    #     }),
    #     ('Availability', {
    #         'fields': ('status', 'due_back')
    #     }),
    # )
    # pass

admin.site.register(Users, UsersAdmin)

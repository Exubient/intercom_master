from django.contrib import admin

# Register your models here.

from .models import AdminTable, Conversation, Conversation_part, User, Date, usedConvo, medianTable

class _AdminTable(admin.ModelAdmin):
    list_display = ['id','adminName', "convoCount", "realCount", "averageResponseSum", "firstCount", "firstResponseSum", "medianResponseSum"]


class _usedConvo(admin.ModelAdmin):
    list_display = ['id','author', "partType","created_at", "body"]

class _medianTable(admin.ModelAdmin):
    list_display = ['adminLink','responseTime']


admin.site.register(AdminTable, _AdminTable)
admin.site.register(usedConvo, _usedConvo)
admin.site.register(medianTable, _medianTable)
# admin.site.register(Conversation)
# admin.site.register(Conversation_part)
# admin.site.register(User)
# admin.site.register(Date)


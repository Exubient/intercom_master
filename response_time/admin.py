from django.contrib import admin

# Register your models here.

from .models import AdminTable, Conversation, Conversation_part, User, Date, usedConvo

class _AdminTable(admin.ModelAdmin):
    list_display = ['id','adminName', "convoCount", "realCount", "firstCount", "firstResponseSum", "averageResponseSum", "medianResponseSum"]


class _usedConvo(admin.ModelAdmin):
    list_display = ['id','author', "created_at", "body"]


admin.site.register(AdminTable, _AdminTable)
admin.site.register(usedConvo, _usedConvo)
admin.site.register(Conversation)
admin.site.register(Conversation_part)
admin.site.register(User)
admin.site.register(Date)


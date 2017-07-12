from django.contrib import admin

from django.contrib import admin


# Register your models here.

from .models import AdminTable, TeamTable, usedConvo, medianTable

class UnitInline(admin.TabularInline):
    model = AdminTable

class _AdminTable(admin.ModelAdmin):
    list_display = ['adminName', "teamLink", "convoCount", "realCount", "averageResponseSum", "averageResponse", "firstCount", "firstResponseSum", "firstResponse", "medianResponse"]

class _TeamTable(admin.ModelAdmin):
	list_display = ['id', 'teamName', 'convoCount', 'realCount', 'averageResponseSum', 'firstCount', 'firstResponseSum', 'firstResponse', 'averageResponse']
	inlines = [ UnitInline ]
class _usedConvo(admin.ModelAdmin):
    list_display = ['id','author', "partType","created_at", "body"]

class _medianTable(admin.ModelAdmin):
    list_display = ['adminLink','responseTime']



admin.site.register(AdminTable, _AdminTable)
admin.site.register(usedConvo, _usedConvo)
admin.site.register(medianTable, _medianTable)
admin.site.register(TeamTable, _TeamTable)



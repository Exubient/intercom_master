from django.contrib import admin

# Register your models here.

from .models import Admin, Conversation, Conversation_part, AdminHour, User, Date


admin.site.register(Admin)
admin.site.register(Conversation)
admin.site.register(Conversation_part)
admin.site.register(AdminHour)
admin.site.register(User)
admin.site.register(Date)


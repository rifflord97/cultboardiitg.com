from django.contrib import admin
from .models import About, Team, Upcoming_Events


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return Poll.objects.all().count() == 0

    admin.site.register(About)


admin.site.register(Team)
admin.site.register(Upcoming_Events)


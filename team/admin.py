from django.contrib import admin
from .models import Ev_Manager, Events_Team, Chairman, Club_Secy, GenSec


admin.site.register(Chairman)
admin.site.register(GenSec)
admin.site.register(Ev_Manager)
admin.site.register(Events_Team)
admin.site.register(Club_Secy)

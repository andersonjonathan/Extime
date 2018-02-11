from django.contrib import admin
from .models import Event, Klass, Entry, Result


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('name', 'date')


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    exclude = ("event", )


admin.site.register(Event, EventAdmin)
admin.site.register(Klass)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Result)

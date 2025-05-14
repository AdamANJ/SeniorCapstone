from django.contrib import admin
from personal.models import (
	textContainer,
	imageContainer,
	Speaker,
	Highlighted_Speaker,
	registration,
	events
	)

# Register your models here.

@admin.register(textContainer)
class textContainerAdmin(admin.ModelAdmin):
	listDisplay = ('title','text','order')
	editable = ('order',)

admin.site.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
	listDisplay = ("image","first_name","last_name","specialty","bio","order")
	editable = ('order')


admin.site.register(Highlighted_Speaker)
class highlightAdmin(admin.ModelAdmin):
	listDisplay = ("image","first_name","last_name","specialty","bio","order")
	editable = ('order')


admin.site.register(events)
class eventsAdmin(admin.ModelAdmin):
	listDisplay = ("time","name","info","order")
	editable = ('order')	

admin.site.register(imageContainer)
admin.site.register(registration)

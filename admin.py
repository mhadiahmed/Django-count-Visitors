from django.contrib import admin
from .models import ObjectViewed
# Register your models here.

class ObjectViewedAdmin(admin.ModelAdmin):
	'''
		Admin View for ObjectViewed
	'''
	list_display = ('user','content_type','timestamp',)

admin.site.register(ObjectViewed, ObjectViewedAdmin)
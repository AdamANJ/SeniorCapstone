from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ('email', 'first_name', 'last_name')
	search_fields = ('email', 'first_name', 'last_name')
	readonly_fields = ('date_joined', 'last_login')

admin.site.register(Account, AccountAdmin)
from django.contrib import admin
from .models import Issue
from django.contrib.auth.models import Group


# Register your models here.
#admin.site.register(Issue)
admin.site.site_header= 'FLASK ADMINISTRATOR'

class IssueAdmin(admin.ModelAdmin):
    fields = ('title','desc','img','resolution','user','example_inc','show')
    list_filter=('show',)





admin.site.register(Issue,IssueAdmin)

from django.contrib import admin
from .models import EnterData
from django.contrib.auth.models import User
# Register your models here.

class EnterDataAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super(EnterDataAdmin, self).get_fields(request, obj)
        if request.user.is_superuser:
            fields= ('work_exp','german_grade','bachelors_percent')
        else:
            fields =('work_exp','german_grade')
        return fields


admin.site.register(EnterData,EnterDataAdmin)

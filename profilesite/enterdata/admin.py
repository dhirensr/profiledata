from django.contrib import admin
from .models import EnterData,HintsData
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import AdminSite
from django.conf.urls import url
from django.urls import path
from . import views

# Register your models here.


class EnterDataAdmin(admin.ModelAdmin):
    class Meta:
        model=EnterData
        fields=('hints',)
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'add/',
                self.admin_site.admin_view(views.testdata),name='enterdata_enterdata_add'),
            path(r'<path:object_id>/change/',
                self.admin_site.admin_view(views.testdataedit),name='enterdata_enterdata_change'),]
        return my_urls + urls
    def get_fields(self, request, obj=None):
        fields = super(EnterDataAdmin, self).get_fields(request, obj)
        if request.user.is_superuser:
            fields= ('work_exp','german_grade','bachelors_percent','hints')
        else:
            fields =('work_exp','german_grade','hints')
        return fields



# class EnterDataForm (forms.ModelForm):
#     extra_field= forms.CharField(required=False)
#     extra_field2 = forms.CharField(required=False)
#     def save(self, commit=True):
#         a= super(EnterDataForm, self).save(commit=commit)
#         extra_field = self.cleaned_data.get('extra_field', None)
#         extra_field2 = self.cleaned_data.get('extra_field2', None)
#         a.hints= [extra_field,extra_field2]
#         a.save()
#         return a

# class EnterDataAdmin(admin.ModelAdmin):
#     form = EnterDataForm
#     fieldsets = (
#         (None, {
#             'fields': ('work_exp', 'semester', 'extra_field','extra_field2',),
#         }),
#     )

#     def get_form(self,request,obj=None,**kwargs):
#         form = super(EnterDataAdmin, self).get_form(request, obj, **kwargs)
#         if obj:
#             form.base_fields['extra_field'].initial = obj.hints[0]
#             form.base_fields['extra_field2'].initial = obj.hints[1]
#         return form
#     #super(MyVehiclesAdmin, self).save_model(request, obj, form, change)

admin.site.register(EnterData,EnterDataAdmin)

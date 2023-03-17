from django.contrib import admin
from home.models import Gujarat_hospital,Gujarat_Ngo,Appointment
from import_export.admin import ImportExportModelAdmin
from import_export import resources


#gujarat
class Gujarat_hospitalResources(resources.ModelResource):
    class Meta:
        model = Gujarat_hospital

class Gujarat_hospitalAdmin(ImportExportModelAdmin):
    resource_class = Gujarat_hospitalResources


admin.site.register(Gujarat_hospital,Gujarat_hospitalAdmin)


class Gujarat_NgoResources(resources.ModelResource):
    class Meta:
        model = Gujarat_Ngo

class Gujarat_NgoAdmin(ImportExportModelAdmin):
    resource_class = Gujarat_NgoResources


admin.site.register(Gujarat_Ngo,Gujarat_NgoAdmin)

admin.site.register(Appointment)
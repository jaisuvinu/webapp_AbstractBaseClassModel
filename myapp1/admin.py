from django.contrib import admin
from myapp1.models import RegularEmployee,ContractEmployee

# Register your models here.

admin.site.register(RegularEmployee)
admin.site.register(ContractEmployee)
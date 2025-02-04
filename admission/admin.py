from django.contrib import admin
from .models import Department,Program,Student,Category,Caste, Religion, Quota,Scholarship,Reason, TransferCertificate,ProgramLevel

# Register your models here.
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Caste)
admin.site.register(Religion)
admin.site.register(Quota)
admin.site.register(Scholarship)
admin.site.register(Reason)
admin.site.register(TransferCertificate)
admin.site.register(ProgramLevel)


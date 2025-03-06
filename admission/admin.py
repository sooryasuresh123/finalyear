from django.contrib import admin
<<<<<<< HEAD
from .models import Department,Program,Student,Category,Caste, Religion, Quota,Scholarship,Reason, TransferCertificate,ProgramLevel,Role,ScholarshipType,Board,Pathway,DocType
=======
from .models import Department,Program,Student,Category,Caste, Religion, Quota,Scholarship,Reason, TransferCertificate,ProgramLevel,Role,ScholarshipType,Board,Pathway,Teacher
>>>>>>> d91fe44 (upto dashboard)

# Register your models here.
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Caste)
admin.site.register(Religion)
admin.site.register(Quota)
admin.site.register(Reason)
admin.site.register(TransferCertificate)
admin.site.register(ProgramLevel)
admin.site.register(Role) 
# admin.site.register(User) 
admin.site.register(Scholarship)
admin.site.register(ScholarshipType)
admin.site.register(Board)
<<<<<<< HEAD
admin.site.register(DocType)
=======
admin.site.register(Teacher)
>>>>>>> d91fe44 (upto dashboard)
admin.site.register(Pathway)





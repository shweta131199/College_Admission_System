from django.contrib import admin
from .models import Application, Notice, Detail,Hostel_Application, Product

admin.site.register(Product)
admin.site.register(Application)
admin.site.register(Hostel_Application)
admin.site.register(Notice)
admin.site.register(Detail)



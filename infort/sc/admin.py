from django.contrib import admin
from .models import *


admin.site.register(Vendor)
admin.site.register(Schematic)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Device)
admin.site.register(Stage)
admin.site.register(Service_list)

# prepopulated_fields = {'slug':('title')}
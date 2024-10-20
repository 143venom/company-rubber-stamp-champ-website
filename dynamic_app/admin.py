from django.contrib import admin
from .models import *

admin.site.site_header = 'Companyrubberstampchamp Admin'
admin.site.site_title = 'stampchamp Admin panel'
admin.site.index_title = 'welcome stampchamp Admin panel'

# Register your models here.
admin.site.register(User)
admin.site.register(Slider)
admin.site.register(Quote)
admin.site.register(Testimonial)
admin.site.register(PrintingServices)
admin.site.register(ItServices)
admin.site.register(PhotographyServices)
admin.site.register(GetItServices)
admin.site.register(GetPhotographyServices)

